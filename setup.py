from setuptools import setup

APP = ['tk-wbs-ip.py']
APP_NAME = 'WbsIP'
DATA_FILES = ['icon.png']
OPTIONS = {'iconfile': 'icon.png'} #.icns

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
