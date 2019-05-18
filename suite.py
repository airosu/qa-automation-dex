from unittest import TestLoader, TestSuite
from tests._DEMO_FILE_TEST import Test1, Test2


""" Load tests from TestCase using TestLoader """
tc_demo_test_1 = TestLoader().loadTestsFromTestCase(Test1)
tc_demo_test_2 = TestLoader().loadTestsFromTestCase(Test2)



""" Group the tests in suites using TestSuite """
def small_suite_list():
    return TestSuite([tc_demo_test_1])


def full_suite_list():
    suite = TestSuite([
        tc_demo_test_1,
        tc_demo_test_2
    ])
    return suite


