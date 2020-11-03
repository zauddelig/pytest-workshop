








```
-> ██████╗ ██╗   ██╗████████╗███████╗███████╗████████╗ <-
-> ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝ <-
-> ██████╔╝ ╚████╔╝    ██║   █████╗  ███████╗   ██║    <-
-> ██╔═══╝   ╚██╔╝     ██║   ██╔══╝  ╚════██║   ██║    <-
-> ██║        ██║      ██║   ███████╗███████║   ██║    <-
-> ╚═╝        ╚═╝      ╚═╝   ╚══════╝╚══════╝   ╚═╝    <-
≈-> "Framework that makes building simple and scalable tests easy." <-
```
Readme taken from https://github.com/cm-tm

---

-> # Highlights <-


\* *Simple/clear* - yet so flexible that the test suits can scale to 
                 become complex.
  
\* *Insightful*   - test results give detail description of which test failed 
                 at which point.

\* *Documented*   - 200+ pages of well-written documentation for your 
                 reading pleasure.

\* *Extensible*   - plugins add extra functionality, e.g. new fixtures.

\* *Popular*      - makes staying in touch with the open-source world easier.

---

-> # Basics: test discovery <-


Files in the given path prefixed with *test_* and inside them functions
prefixed with *test_* or suffixed with *\_test*.

* tests
    - models
        - ignored_by_pytest.py
        - test_group.py
        
        `def group_exists_test():`
        `    pass`
        
        - test_user.py:
        
        `def test_user_assigned_to_group():`
        `    pass`


---

-> # Basics: assertions <-

Unlike in the built-in unit test library, assertions are made 
purely using *assert* statement/keyword. This makes tests much cleaner and 
easier to write because there is no guessing whether to use clunky
*self.assertNotAlmostEqual()* or identically looking
*self.assertNotAlmostEquals()*.

~~~
def test_one_means_one():
    expected = 1
    actual = 4
    assert expected == 1
    assert expected == actual, "Went for a beer, had more"
~~~

## Result
================================== FAILURES ===================================
_____________________________ test_one_means_one __________________________________

\    def test_one_means_one\(\):
\        expected = 1
\        actual = 4
\        assert expected == 1
\>       assert expected == actual, "Went for a beer, had more"
*E       AssertionError: Went for a beer, had more*
*E       assert 1 == 4*

test.py:5: AssertionError
===================== 1 failed, 0 passed in 0.39 seconds ======================

---

-> # Basics: running tests <-


*\$ pytest \[options\] \[directory or file\]*


## Some of the useful options

*--lf*          - rerun only the tests that failed at the last run.
*--setup-only*  - runs fixtures without tests and displays the execution order
                of fixtures' setup/teardown as well as execution order of 
                tests with various inputs. 
*--maxfail=N*   - exit after first N failures or errors.
*-x*            - exit instantly on first error or failed test.
*-k EXPRESSION* - python expression to run only matching tests,
\                e.g. 'test_user or test_group', 'not test_group`
*-m MARK*       - only run tests matching given mark expression.

---

-> # Advanced: built-in marks <-


Marks are metadata for test functions.
They are applied using *@pytest.mark.MARK_NAME* decorator.


\* *skip*        - always skip a test function.

\* *skipif*      - skip a test function if a certain condition is (not) met,
                e.g. *@pytest.mark.skipif(sys.version_info < (3, 7))*

\* *usefixtures* - invokes fixture even though a test doesn't declare it 
                as its parameter.

\* *parametrize* - perform multiple calls to the same test function with 
                different input.

---

-> # Advanced: "parametrize" mark <-


*parametrize* mark causes the test function to be called multiple times
with different input value. The main benefit is cleaner test code
(no need for a loop within the test) and better understanding of all
the test calls that would be made


## Syntax with a single parameter

*@pytest.mark.parametrize\('param', \[1, 2\]\)*


## Syntax with multiple parameters

*@pytest.mark.parametrize\('param_a,param_b', \[\(1, 2\), \(3, 4\)\]\)*

---

-> # Advanced: "parametrize" mark <-


## Example

~~~
from app import something
    
@pytest.mark.parametrize('value,expected', [(0, False), (1, True)])
def test_result(value, expected):
    assert something(value) is expected
~~~

*$ pytest --collect-only ./tests* would give us an insight on which tests
would be run, how many times and with which input value without
actually running the tests themselves.


## Result

\========================= test session starts ================================
\collected 2 items
\<Module test.py>
\  <Function test_result[0-False]>
\  <Function test_result[0-True]>
\===================== no tests ran in 0.01 seconds ===========================

---

-> # Advanced: custom marks <-


Other custom values can be used to mark tests.
This can be useful for grouping tests and executing them using the *-m* flag:

~~~
@pytest.mark.slow
def test_providers():
    pass
~~~

*$ pytest -m 'not slow' ./tests*

---

-> # Advanced: testing expected failures <-


Tests should be written not only to assert that something works as expected
but that it also fails as expected. This often involves that an exception
is raised under particular circumstances.

In pytest an assertion that the tested code raises an exception can
be done using *pytest.raises(Exception)* context manager.

## Example

~~~
def test_user_exists_failure():
    with pytest.raises(Exception):
        User.exists(id=666)
~~~

---

-> # Advanced: fixtures <-


Fixtures are the pinnacle of pytest. They are objects called before a test 
starts and their result injected into the test functions as 
a parameter of the same name.

Moreover they are capable of performing a rollback at the end of test execution
and are therefore a replacement for *setUp/tearDown* methods of the built-in
unit tests's *TestCase* class.

## Notable built-in fixture

\* *cache*        - returns a cache object that can persist state between 
                 testing sessions.

\* *capsys*       - enables text capturing of writes to _sys.stdout/sys.stderr_.

\* *capsysbinary* - enable bytes capturing of writes to _sys.stdout/sys.stderr_.

\* *monkeypatch*  - provides helper methods to modify objects or os.environ.

\* *tmpdir*       - returns a temporary directory path object which is unique
\                 to each test function invocation.

---

-> # Advanced: fixtures - monkeypatching <-


Sometimes we need to test code which:

\* *Depends on particular state not easy to reproduce*

\* *Calls external services* - e.g. an API of a provider that we use.

...and we need to avoid tests not being reproducible due to changing
state or due to dependency on external services. This can be avoided by 
*monkeypatching* such code and making sure it always works in a pre-defined
state.

There are (at least) 2 options how monkeypatching can be applied in pytest:

\* *Built-in monkeypatch fixture*

\* *pytest-mock plugin*

---

-> # Advanced: fixtures - monkeypatching with built-in fixture <-


The built-in *monkeypatch* fixture provides a simple way to replace or set
properties with a custom code.

~~~
from app.models import User
from unittest.mock import MagicMock
    
def test_user_exists_success(monkeypatch):
    mocker = MagicMock()
    mocker.in_ldap.return_value = True
    
    monkeypatch.setattr('app.models.user.LDAP', mocker)
    monkeypatch.setenv('AUTH_LDAP', 'example.com')
    
    assert User.exists(id=123) is True
~~~

---

-> # Advanced: fixtures - monkeypatching with pytest-mock <-


pytest-mock is a pytest plugin that introduces a *mocker* fixture which is
a thin-wrapper around the patching API provided by the *unittest.mock*
and therefore allows you to use its *patch()* function.

~~~
from app.models import User
    
def test_user_exists_success(mocker):
    mock = mocker.patch('app.models.user.LDAP')
    mock.in_ldap.return_value = {
        'id': 123,
        'name': 'John Doe',
    }
    
    assert mock.in_ldap.called is True
    assert User.exists(id=123) is True
~~~

Note: In this example *mocker.patch* returns an instance of
*unittest.mock.MagicMock*.

---

-> # Advanced: custom fixtures <-


Custom fixtures can be created by applying *@pytest.fixture* decorator
to your own function:

~~~
from application.app import app
    
@pytest.fixture    
def app_client():
    app.test_request_context().push()
    
    return app.test_client()
~~~

The fixture decorator accepts several parameters, notably:

\* *scope*   - modifies the scope of when the fixture is invoked. By default 
            it is before each test but could be instead called once for each
            module or once for the entire session.
            
\* *autouse* - when set to True, the fixture is invoked even when the test 
            function doesn't declare its use.

---

-> # Advanced: custom fixtures - setup/teardown pattern <-


You can use *yield* statement instead of *return* so that the execution
returns to the fixture at the end of the fixture's scope:

~~~
from application.app import app
    
@pytest.fixture    
def app_client():
    app.test_request_context().push()
    
    yield app.test_client()
    
    # Start of the teardown when a test finishes
    ...
~~~

This gives the fixture a chance to execute any necessary clean-up code.

---

-> # Advanced: fixtures from custom packages <-


A custom Python packages can extend pytest with extra fixtures.

* abcd
    - pytest_fixtures.py
    - setup.py
    
## setup.py

~~~
from setuptools import setup
    
setup(
    name='abcd',
    version='1.0.0',
    entry_points={'pytest11': ['abcd = abcd.pytest_fixtures']},
)
~~~

---

-> # What to take to the coding dojo <-


\* *@pytest.fixture* decorator on your function would turn it into
  a custom fixture.

\* *@pytest.fixture(autouse=True)* would cause your fixture to be executed
  even when the test function doesn't declare it as its parameter.
  
\* *yield* in your fixture function would allow you to run additional code
  when a test function exits.
  
\* *@pytest.mark.parametrize('param_name', \['value_a', 'value_b'\])* would make
  your test function to be called multiple times with *param_name* having
  different input value each time.
  
\* *monkeypatch* or *mocker* fixture declared in your test function allows you
  to mock objects, e.g. *mocker.patch('requests.request')*. 
  
