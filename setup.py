from setuptools import setup

setup(
    name='AutoCacheClearer',
    version='1.0',
    scripts=['clear.py'],
    description='auto cache clear Linux servers.',
    author='Mr.Mili',
    author_email='miladjalali1388@gmail.com',
    packages=[],
    install_requires=[
        'schedule',
    ],
)
