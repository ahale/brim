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

from StringIO import StringIO
from unittest import main, TestCase

from brim import daemon_sample
from brim.conf import Conf


class FakeLogger(object):

    def __init__(self):
        self.info_calls = []

    def info(self, args):
        self.info_calls.append(args)


class FakeServer(object):

    def __init__(self):
        self.logger = FakeLogger()


class FakeStats(object):

    def __init__(self):
        self.stats = {}

    def get(self, name):
        return self.stats.get(name, 0)

    def set(self, name, value):
        self.stats[name] = value

    def incr(self, name):
        self.stats[name] = self.stats.get(name, 0) + 1


class TestDaemonSample(TestCase):

    def test_init_attrs(self):
        s = daemon_sample.DaemonSample('test', {})
        self.assertEquals(getattr(s, 'testattr', None), None)
        s = daemon_sample.DaemonSample('test', {'testattr': 1})
        self.assertEquals(getattr(s, 'testattr', None), 1)

    def test_call(self):
        sleep_calls = []

        def _sleep(*args):
            sleep_calls.append(args)
            if len(sleep_calls) == 3:
                raise Exception('testexit')

        def _time():
            return 123

        fake_server = FakeServer()
        fake_stats = FakeStats()
        s = daemon_sample.DaemonSample('test', {'interval': 60})
        orig_sleep = daemon_sample.sleep
        orig_time = daemon_sample.time
        exc = None
        try:
            daemon_sample.sleep = _sleep
            daemon_sample.time = _time
            s(fake_server, fake_stats)
        except Exception, err:
            exc = err
        finally:
            daemon_sample.sleep = orig_sleep
            daemon_sample.time = orig_time
        self.assertEquals(str(exc), 'testexit')
        self.assertEquals(sleep_calls, [(60,)] * 3)
        self.assertEquals(
            fake_server.logger.info_calls,
            ['test sample daemon log line 1',
             'test sample daemon log line 2',
             'test sample daemon log line 3'])
        self.assertEquals(fake_stats.get('last_run'), 123)
        self.assertEquals(fake_stats.get('iterations'), 3)

    def test_parse_conf(self):
        c = daemon_sample.DaemonSample.parse_conf('test', Conf({}))
        self.assertEquals(c, {'interval': 60})
        c = daemon_sample.DaemonSample.parse_conf(
            'test', Conf({'test': {'interval': 123}}))
        self.assertEquals(c, {'interval': 123})
        c = daemon_sample.DaemonSample.parse_conf(
            'test', Conf({'test2': {'interval': 123}}))
        self.assertEquals(c, {'interval': 60})

    def test_stats_conf(self):
        self.assertEquals(daemon_sample.DaemonSample.stats_conf(
            'test', {'interval': 60}), ['iterations', 'last_run'])


if __name__ == '__main__':
    main()
