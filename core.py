import logging
import json
from os import path, mkdir
from flask import Flask
from sys import platform

if not path.exists('./logs/'):
    mkdir('./logs')

if platform.startswith('linux'):
    dwebp = path.join('lib_dwebp', 'linux', 'dwebp')
elif platform == 'win32':
    dwebp = path.join('lib_dwebp', 'win', 'dwebp.exe')
elif platform == 'debian':
    dwebp = path.join('lib_dwebp', 'osx', 'dwebp')
else:
    raise OSError('Invalid operation system')

logging.basicConfig(filename='logs/w2j.log', level=logging.INFO,
                    format=u'%(asctime)-15s | [%(name)s] %(levelname)s => %(message)s')
logger = logging.getLogger('root')

# Config
config = json.load(open('config.json', 'r'))

# API
app = Flask(__name__)
