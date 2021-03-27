def latex():
    import library.ml as ml
    import time
    encoded = ml.url_encode('a_{x+1}^{4x^{8+10}}')
    url = f'http://chart.apis.google.com/chart?cht=tx&chl={encoded}&chs=250'
    import requests
    file_name = 'temp_'+str(time.time()) + '.png'
    r = requests.get(url)
    with open(file_name, 'wb+') as p:
        p.write(r.content)
        p.close()
    import shutil
    shutil.move(file_name, 'abc.png')


if __name__ == '__main__':
    latex()
