#!/usr/bin/python
# Copyright 2012 Gregory Holt
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

import brim


setup(name='brim', version=brim.version,
      description='Brim.Net Core Package', author='Gregory Holt',
      author_email='brim@brim.net', url='http://gholt.github.com/brim/',
      packages=['brim'], requires=['eventlet(>=0.9.16)'],
      scripts=['bin/brimd'])
