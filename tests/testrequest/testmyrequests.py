# -*- coding: utf-8 -*-
from drivers.driverrequests import DriverRequests
import unittest


class TestMyRequests(DriverRequests):

    @unittest.SkipTest
    def test_00_status_response(self):
        try:
            self.assertEquals(self.status_request_QA(), 200)
        except (AssertionError, BaseException, Exception), e:
            print str(self.status_request_QA())
            print "\nNo es un 200"
            self.fail(e)
        else:
            print "\nEl valor es " + str(self.status_request_QA())

    @unittest.SkipTest
    def test_01_response_json(self):
        try:
            self.assertTrue(self.json_request_QA())
        except (AssertionError, BaseException, Exception), e:
            print "\nNo hay JSON"
            self.fail(e)
        else:
            print "\nJSON: \n" + str(self.json_request_QA())

    @unittest.SkipTest
    def test_04_data_responses(self):
        try:
            print self.element_request_QA('USD', 'dolartoday')
            self.assertEqual(str(self.element_request_QA('USD', 'dolartoday')), '730.29')
        except (AssertionError, BaseException, Exception), e:
            print "\nNO ES IGUAL"
            self.fail(e)
        else:
            print "\nES IGUAL"
