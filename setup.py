from setuptools import setup

def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
    name='DiscUtils',
    version='1.8.0',
    author="mosaiyka",
    author_email="artmonuzartemonuz@gmail.com",
    description="Библиотека для юзер-ботов дискорд",
    long_description=readme(),
     long_description_content_type='text/markdown',
    url="https://github.com/mosaiyka/DiscUtils",
    py_modules=['DiscUtils'],
    install_requires=[
        'requests',
        'websocket-client',
        'websockets',
        'asyncio',
        'colorama'
    ],
    keywords="discord discum discord.py-self DiscUtils discutils DiscordUtils description"
)