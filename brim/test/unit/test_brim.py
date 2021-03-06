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

from unittest import main, TestCase

import brim


class TestBrim(TestCase):

    def test_version_info(self):
        self.assertEquals(len(brim.version_info), 3)
        self.assertTrue(isinstance(brim.version_info[0], int))
        self.assertTrue(isinstance(brim.version_info[1], int))
        self.assertTrue(isinstance(brim.version_info[2], int))

    def test_version(self):
        self.assertTrue(isinstance(brim.version, str))
        self.assertEquals(brim.version, '.'.join(map(str, brim.version_info)))


if __name__ == '__main__':
    main()
