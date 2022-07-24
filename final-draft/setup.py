from setuptools import setup
# 
''' pip install -U -r requirements.txt ''' # !!!TURN YOUR ATTENTION!!!
# 
APP = ['tk_wbs_IP.py']
APP_NAME = 'WbsIPv2'
DATA_FILES = ['wbs_IP.py','icon.png']
OPTIONS = {'iconfile': 'icon.png'} #.icns

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
