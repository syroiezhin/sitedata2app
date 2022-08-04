from setuptools import setup
 
''' pip install -U -r requirements.txt '''

APP_NAME = 'URL2IP'
APP = ['tk_wbs_IP.py']

DATA_FILES = ['wbs_IP.py','icon.png']
OPTIONS = {'iconfile': 'icon.png'}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    setup_requires=['py2app'],
    options={'py2app': OPTIONS},

    version='1.0',
    description='site data search',
    long_description="Getting IP and information about the site knowing the url address",

    author='@NEU3RON',
    license="Syroiezhin",
    author_email='v.syroiezhin@gmail.com',
    url="https://github.com/syroiezhin",
)