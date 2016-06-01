#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2013 Andreas Arvidsson
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(
    name='BlocketWatch',
    version='0.1.0',
    author='Andreas Arvidsson',
    author_email='andreas.arvidson@gmail.com',
    packages=['blocketwatch', 'blocketwatch.test'],
    scripts=['bin/blocket_watch.py'],
    url='https://github.com/chip2n/blocket-watch',
    license='LICENSE.txt',
    description='Monitor Blocket.se',
    long_description=open('README.rst').read(),
    install_requires=[
        "PyYaml >= 3.0",
        "Requests >= 1.2.0",
        "BeautifulSoup4 >= 4.1.3",
    ],
)
