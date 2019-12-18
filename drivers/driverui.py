# -*- coding: utf-8 -*-
import webdriver_manager
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.service import WebDriverException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import unittest
import datetime
import time
import os


class DriverUI(unittest.TestCase):

    def setUp(self):
        global capabilities
        brw = 'CHROME'
        try:
            if self.select_environment() == 'LOCAL':
                try:
                    if brw == 'CHROME':
                        self.driver = webdriver.Chrome(ChromeDriverManager().install())
                    elif brw == 'FIREFOX':
                        self.driver = webdriver.Firefox(GeckoDriverManager().install())
                    self.driver.implicitly_wait(5)
                    self.driver.maximize_window()
                except WebDriverException as wde:
                    print "WebDriver doesn't exist"
                    self.fail(wde)
                else:
                    return self.driver
            elif self.select_environment() == 'REMOTE':
                if brw == 'CHROME':
                    capabilities = DesiredCapabilities.CHROME
                elif brw == 'FIREFOX':
                    capabilities = DesiredCapabilities.FIREFOX
                selenium_grid_url = 'http://10.1.27.253:4444/wd/hub'
                try:
                    self.driver = webdriver.Remote(command_executor=selenium_grid_url,
                                                   desired_capabilities=capabilities)
                    self.driver.implicitly_wait(5)
                    self.driver.maximize_window()
                except WebDriverException as wde:
                    print "WebDriver doesn't exist"
                    self.fail(wde)
                else:
                    return self.driver
        except Exception, e:
            print "Environment not detected"
            self.fail(e)

    def getUrl(self, url):
        self.driver.get(url)

    def getCookie(self, ck):
        cookies_list = self.driver.get_cookies()
        cookies_dict = {}
        for cookie in cookies_list:
            cookies_dict[cookie['name']] = cookie['value']
        session_id = cookies_dict.get(ck)
        return session_id

    def tearDown(self):
        self.driver.quit()

    def delay(self, sec):
        time.sleep(sec)

    def getToday(self):
        return datetime.datetime.now()

    def getTodayWithFormat(self):
        return str(time.strftime('%d/%m/%Y'))

    def getTodayWithFormatYMD(self):
        return str(time.strftime('%Y-%m-%d'))

    def clean_fields(self, elem):
        self.driver.find_element(By.XPATH(elem)).clear()

    def clean_fields_keyboard(self, elem):
        self.driver.find_element_by_xpath(elem).send_keys(Keys.CONTROL + "a")
        self.driver.find_element_by_xpath(elem).send_keys(Keys.BACKSPACE)

    def fill_fields(self, elem, value):
        self.driver.find_element_by_xpath(elem).send_keys(value)

    def fill_fields_date_db(self, elem, date):
        self.driver.find_element_by_xpath(elem).send_keys(date)

    def fill_fields_date(self, elem, day, month, year):
        self.driver.find_element_by_xpath(elem).send_keys(day)
        self.driver.find_element_by_xpath(elem).send_keys(month)
        self.driver.find_element_by_xpath(elem).send_keys(year)

    def click_button(self, elem):
        self.driver.find_element_by_xpath(elem).click()

    def web_driver_wait(self, elem):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, elem)))

    def web_driver_wait_bool(self, elem):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, elem)))
            return True
        except TimeoutException:
            return False

    def web_driver_wait_to_text(self, elem, message):
        WebDriverWait(self.driver, 120).until(EC.text_to_be_present_in_element((By.XPATH, elem), message))

    def wait_text(self, elem):
        return self.driver.find_element_by_xpath(elem).text

    def wait_text_by_css(self, elem):
        return self.driver.find_element_by_css_selector(elem).text

    def get_elements(self, elem):
        return self.driver.find_elements_by_xpath(elem)

    def get_element(self, elem):
        return self.driver.find_element_by_xpath(elem)

    def save_screenshot_test_pass(self, name):
        # self.driver.get_screenshot_as_file('../screenshots/pass/' + name + '_' + str(self.getToday()) + '.png')
        self.driver.get_screenshot_as_file(self.screenshot_pass_path() + "/"
                                           + name + '_' + str(self.getToday()) + '.png')

    def save_screenshot_test_fail(self, name):
        # self.driver.get_screenshot_as_file('../screenshots/fail/' + name + '_' + str(self.getToday()) + '.png')
        self.driver.get_screenshot_as_file(self.screenshot_fail_path() + "/"
                                           + name + '_' + str(self.getToday()) + '.png')

    def click_link(self, elem):
        self.driver.find_element_by_xpath(elem).click()

    def value_select(self, elem, value):
        Select(self.driver.find_element_by_xpath(elem)).select_by_value(value)

    def read_search_field(self, elem):
        return self.driver.find_element_by_xpath(elem).get_attribute("value")

    def read_value_in_field(self, elem):
        return self.driver.find_element_by_xpath(elem).get_attribute("value")

    def select_checkbox(self, elem):
        self.driver.find_element_by_xpath(elem).click()

    def select_file(self, elem, path):
        self.driver.find_element_by_xpath(elem).send_keys(path)

    def files_path(self):
        filepath = str(os.path.realpath('../audit/files'))
        return filepath

    def screenshot_pass_path(self):
        filepath = str(os.path.realpath('../screenshots/pass/'))
        return filepath

    def screenshot_fail_path(self):
        filepath = str(os.path.realpath('../screenshots/fail/'))
        return filepath

    def element_displayed(self, elem):
        return self.driver.find_element_by_xpath(elem).is_displayed()

    def element_enabled(self, elem):
        return self.driver.find_element_by_xpath(elem).is_enabled()

    def element_selected(self, elem):
        return self.driver.find_element_by_xpath(elem).is_selected()

    def change_windows(self, elem):
        return self.driver.switch_to.window(elem)

    def window_before(self):
        return self.driver.window_handles[0]

    def window_after(self):
        return self.driver.window_handles[1]

    def keyboard_tab(self, elem):
        self.driver.find_element_by_xpath(elem).send_keys(Keys.TAB)

    def select_environment(self):
        path_ratd_remote = '/var/lib/jenkins/workspace/'
        if os.path.exists(path_ratd_remote) is True:
            e = 'REMOTE'
            return e
        else:
            e = 'LOCAL'
            return e


if __name__ == "__main__":
    unittest.main()
