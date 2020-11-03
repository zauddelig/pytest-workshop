"""
Fixtures are functions that help us writing tests.

They can be used for different scopes,
 like encapsulate common logic or allow the system to rollback side effects.
The code encapsulated by the fixture will run at the beginning of each test,
 if we are not saying it otherwise.

In this test we will check the default fixtures.

* cache - returns a cache object that can persist
    state between testing sessions.

* capsys - enables text capturing of writes to sys.stdout/sys.stderr.

* capsysbinary - enable bytes capturing of writes to sys.stdout/sys.stderr.

* monkeypatch - provides helper methods to modify objects or os.environ.

* tmpdir - returns a temporary directory path object which is unique \
    to each test function invocation.

"""
# we will import time to emulate a complex operation, like visiting a website.
import time
from unittest import mock


class ComplexClass:
    """ This object will be used to test monkeypatching """
    number = 1
    cache = {}

    def method(self):
        return self.number


class TestMonkeyPatch:

    def teardown_method(self):
        """ As you can see the test will not affect the original class. """
        assert ComplexClass.number == 1
        assert ComplexClass.cache == {}
        assert ComplexClass().method() == 1

    def test_attribute(self, monkeypatch):
        """
        We can patch an attribute.
        """
        monkeypatch.setattr(ComplexClass, 'number', 2)
        assert ComplexClass().method() == 2

    def test_method(self, monkeypatch):
        """
        We can patch a method
        """
        monkeypatch.setattr(ComplexClass, 'method', mock.Mock(return_value=2))
        assert ComplexClass().method() == 2

    def test_setitem(self, monkeypatch):
        """
        We can even patch a dictionary
        """
        monkeypatch.setitem(ComplexClass.cache, 'test', 2)
        assert ComplexClass.cache == {'test': 2}


class WebFetcher:
    """
    This class emulates a web fetcher, it makes an HTTP request
    and returns the response text
    """
    def __init__(self, link: str):
        self.link = link

    def _fetch(self) -> bytes:
        time.sleep(5)
        return b'Hello World!'

    def fetch(self) -> str:
        return self._fetch().decode('utf-8')


def test_monkeypatch(monkeypatch):
    """
    Monkeypatch a fixtures.
    """
    web_fetcher = WebFetcher('https://example.com')
    web_fetcher
