from setuptools import setup

setup(
    name='DiscUtils',
    version='1.7.91',
    py_modules=['DiscUtils'],
    install_requires=[
        'requests',
        'websocket-client',
        'websockets',
        'asyncio',
        'colorama'
    ]
)