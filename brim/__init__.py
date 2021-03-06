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

"""
This is the core package for Brim.Net Python-based applications. It
provides some reusable utility code and provides brimd, a launcher
offering ease of deployment of WSGI applications (currently just
using the Eventlet WSGI server) and maintaining background daemons.
"""

__all__ = ['version_info', 'version']

#: Version information ``(major, minor, revision)``.
version_info = (0, 3, 0)
#: Version string ``'major.minor.revision'``.
version = '.'.join(map(str, version_info))
