# blog后端设计
|数据库 |字段| |||||||
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
article_comments_table|commentId|comment_json|time13
article_table|article_id|user_id
数据库表

## 通用数据响应设计

代码目录结构如下
```yaml
api:
 - api.py
controller:
 - sql_controller.py
libray:
 - sql.py
 - intelligent_response.py
```

### api.py
```python
# 读取sql_controller中的所有函数并注册
types = init_types(sql_controller)
def blog(r: HttpRequest):
    params = ml.extract_url_param_dict(r.get_full_path())
    r = intelligent_response(types, params)
    return r


def init_types(pkg):
    x = {}
    mem = getmembers(pkg, isfunction)
    for i in mem:
        x[i[0]] = i[1]
    return x
```
### sql_controller.py
**这里和下面那个intelligent_response.py是最神奇的地方!**
查询一个文章的信息，返回json实体，仅仅需要一个简单的sql语句
```python
def get_article_content(article_id):
    return exec_sql('''
    select article_content from article_table where article_id=?
    ''', article_id)
```
如果查询单个结果，默认会返回一个dict

如果查询多个结果，默认会返回一个list

这一点和sql的特点非常一致，如果想要禁用这个特点，比如文章列表查询，结果为1条自然不希望它成为dict类型，可以用```single_result_detection```
```python
exec_sql('''
    select * from article_table
    ''', user_name, single_result_detection=False)
```

如果想要对```exec_sql```结果以py对象用python稍加处理，可以用可选参数，返回的就不再是json
```python
exec_sql('select * from user_info_table where user_name=? ', u, json_str=False)
```
### intelligent_response.py


通过paramdict来判断需要调用的参数类型，并且逐个检查函数所需要的各个参数是否存在，如果不存在，则返回失败信息

如果调用成功，则调用上面sqlcontroller中的函数语句
```python
def intelligent_response(constrains, param_dict):
    if param_dict.__contains__('type'):
        if constrains.__contains__(param_dict['type']):
            vars_needed = constrains[param_dict['type']].__code__.co_varnames[:
                                                                              constrains[param_dict[
                                                                                  'type']].__code__.co_argcount]
            allowed = True
            params = []
            for var in vars_needed:
                if param_dict.__contains__(var):
                    params.append(ml.url_decode(param_dict[var]))
                else:
                    ml.error_log(f'param {var} is not contained')
                    allowed = False
            if allowed:
                return HttpCrossDomainResponse(constrains[param_dict['type']](*params))
            else:
                return HttpFailure()
        else:
            ml.error_log(f'this type {param_dict["type"]} is not defined')
            return HttpFailure()
    else:
        ml.error_log('param not contains "type"')
        return HttpFailure()
```
