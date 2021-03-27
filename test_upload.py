import requests
import os, shutil

import sys
import urllib
from urllib.parse import quote_plus


def make_archive(source, destination):
    base = os.path.basename(destination)
    name = base.split('.')[0]
    format = base.split('.')[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    shutil.make_archive(name, format, archive_from, archive_to)
    shutil.move('%s.%s' % (name, format), destination)


# xxxxxx
if __name__ == '__main__':
    project_name = 'blogserver'
    project_dir = '../BlogDjangoServer'
    try:
        make_archive(os.path.join(os.getcwd(), project_dir),
                     'default.zip')
        files = {'file': open('default.zip', 'rb')}
        values = {}
        pre = quote_plus('cd BlogDjangoServer && sh kill.sh')
        aft = quote_plus('cd BlogDjangoServer && sh run.sh')
        r = requests.post(
            f'http://kuroweb.cf:8083/upload?pre={pre}&aft={aft}&app=' + f'{project_name}&token={sys.argv[1]}',
            files=files,
            data=values)
    except Exception as e:
        exit(str(e))
