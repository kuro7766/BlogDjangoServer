vps持续集成部署

免费CI服务:

- 华为云
- circleCI (推荐)
- github action (推荐)

以github action为例

CI仓库https://github.com/marketplace

CI生成的可执行文件可以通过某种方式提交到服务器上，可以ssh直接登录文件，也可以通过http端口提交。但是必须注意验证，如果我们把密文卸载ci配置文件里，github其他人都会看见。

这就需要点开工程，增加secret变量

![](http://kuroweb.cf/picture/1616769707592.jpg)

然后action会自动去这里面找变量值

以一个ssh登录代码为例

```yaml
name: CI

on: [push]

jobs:
  deploy:
    if: github.ref == 'refs/heads/master'
    runs-on: [ubuntu-latest]
    steps:
      - uses: actions/checkout@v1
      - name: Push to server
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_IP }}
          username: ${{ secrets.SERVER_USERNAME }}
          password: ${{ secrets.SERVER_PASSWORD }}
          script: cd ${{ secrets.PROJECT_PATH }} && git pull
```

如果是自建http文件接收，也可以用这个办法存密钥。

