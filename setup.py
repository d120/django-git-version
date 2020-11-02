import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-git-version',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='django ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/d120/django-git-version',
    author='Daniel Seiler',
    author_email='daniel.seiler@fachschaft.informatik.tu-darmstadt.de',
    install_requires=[
        'django<4',
        'gitpython',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
