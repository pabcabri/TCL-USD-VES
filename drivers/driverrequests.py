import errno
import unittest
import requests
import json
import os


class DriverRequests(unittest.TestCase):
    def connect_to_response(self):
        url = "https://s3.amazonaws.com/dolartoday/data.json"
        r = requests.get(url)
        return r

    def status_request_QA(self):
        return self.connect_to_response().status_code

    def json_request_QA(self):
        return self.connect_to_response().json()

    def text_request_QA(self):
        return self.connect_to_response().text

    def OK_request_QA(self):
        return self.connect_to_response().ok

    def element_request_QA(self, attr, attr1):
        dtjson = json.loads(self.text_request_QA())
        attribute = dtjson[attr][attr1]
        return attribute

    def access_dir(self, folder):
        #path = os.chdir('/home/pcabria/PycharmProjects/RATD/' + folder)
        path = os.chdir('/var/lib/jenkins/workspace/Smoke-RATD/' + folder)
        return path

    def access_file(self, files):
        try:
            self.access_dir('files')
            fp = open(files)
        except IOError as e:
            if e.errno == errno.EACCES:
                return "\n No se encontro el archivo"
            raise
        else:
            with fp:
                return fp.read()

    def data_responses(self):
        try:
            dr = self.element_request_QA('USD', 'dolartoday')
        except (AssertionError, BaseException, Exception), e:
            print e
            self.fail(e)
        else:
            return dr

    def data_date_process(self):
        try:
            dp = self.element_request_QA('_timestamp', 'dia')
        except (AssertionError, BaseException, Exception), e:
            print e
            self.fail(e)
        else:
            return dp


if __name__ == "__main__":
    unittest.main()
