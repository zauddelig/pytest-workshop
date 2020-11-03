"""
Pytest does not need classes, but it may be still easier for the developer
to incapsulate a number of tests for the same feature in the same class.

This may help maintain a clean code.

"""


class TestBasic:
    """
    As you may know the classic Unittest framework relay on tests,
    in pytest they are still used but not so much.

    To work:
        The class needs to be prefixed with Test

        The test functions must be prefixed with test_

    """
    success = True

    def this_will_not_run(self):
        """
        This function will not run, because is not using test_
        :return:
        """
        assert self.success, "ops!"

    def test_this_will_run(self):
        """
        Once fixed the class name to TestBasic you will see a failure, fix it!
        :return:
        """
        assert self.success, 'Running!'


class TestStateInTests:
    """
    Previously we used the class parameter self.success to do a test,
    what happens if we change it?

    The first test will change the value of self.message but the second test
    will fail.
    """
    message = 'Hello World!'

    def test_first(self):
        message = self.message
        self.message = 'Goodbye'
        assert message == 'Hello World!'

    def test_second(self):
        assert self.message == 'Hello World!', 'The state was not changed!'


# ========
# EXERCISE
# ========

# convert state change to a test and fix it using teardown or setup methods


class TestStateChanges:
    """
    Sometimes side effects happen, and this may lead
    to little, hard to spot bugs in your tests.

    You can fix this using one of those functions, this will effectively
     replicate x-unit style testing:

    def setup_method(self):
        '''
        This code will run __before__ the test.
        '''
        pass

    def teardown_method(self):
        '''
        This code will run __after__ the test.
        '''
        pass

    """
    array = []  # array will maintain its state between runs.

    def test_first(self):
        self.array.append('first test')
        assert len(self.array) == 1

    def test_second(self):
        self.array.append('second test')
        assert len(self.array) == 2, f'A side effect happened!'