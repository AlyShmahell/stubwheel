from setuptools import setup, find_packages

setup(
    name='stubwheel',
    version='1.0.0',
    url='https://github.com/AlyShmahell/stubwheel',
    author='AlyShmahell',
    author_email='',
    description='a script that reserves a project name on PyPi',
    packages=find_packages(),    
    install_requires=['twine >= 3.2.0'],
)