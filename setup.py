#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='asyncapns',
    version='0.1',
    description='An efficient APNs Client Library for Python/asyncio',
    long_description=open('README.rst').read(),
    platforms="all",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 5 - Production/Stable',
    ],
    license='Apache License, Version 2.0',
    author='Aidan He',
    author_email='erhuabushuo@gmail.com',
    url='https://github.com/erhuabushuo/asyncapns',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'h2==3.1.0',
        'pyOpenSSL>=17.5.0',
    ]
)
