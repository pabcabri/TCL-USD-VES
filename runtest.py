# -*- coding: utf-8 -*-
import unittest
from tests.testrequest.testmyrequests import TestMyRequests
from tests.testui.testambcambiocontable import TestABMCambioContable


class SuiteTest(object):
    @property
    def suite_test(self):
        test_suite = unittest.TestSuite()
        test_suite.addTest(unittest.makeSuite(TestMyRequests))
        test_suite.addTest(unittest.makeSuite(TestABMCambioContable))
        return test_suite


tests = SuiteTest()
suite = tests.suite_test
unittest.TextTestRunner(verbosity=2).run(suite)

