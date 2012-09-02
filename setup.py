#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='chinese_pinyin',
    version='0.1',
    packages=['chinese_pinyin'],
    package_data = {
        'chinese_pinyin': ['*.dat'],
    },
    include_package_data = True,
    author='jiedan',
    author_email='lxb429@gmail.com',
    license='MIT License',
    description="translate chinese hanzi to pinyin",
    keywords ='chinese hanzi',
    url='https://github.com/jiedan/chinese_pinyin',
)