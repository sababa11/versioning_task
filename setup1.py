#!/usr/bin/env python

from setuptools import setup

setup(
    name='Versioning Task',
    version='0.1',
    description='Python Versioning Task',
    author='Adam Ta',
    author_email='notrelevant@mail.net',
    url='https://github.com/sababa11/versioning_task.git',
    install_requires=['boto3==1.14.51', 'requests==2.24.0'],
    packages=['p1', 'p2'],
    package_dir={'p1': 'src1/p1', 'p2': 'src2/p2'}
    )

print("OK")
