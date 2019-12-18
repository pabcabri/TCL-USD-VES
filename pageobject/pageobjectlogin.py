# -*- coding: utf-8 -*-
from drivers.driverui import DriverUI


class ObjectPageLogin(DriverUI):

    # LOGIN
    def set_field_username(self):
        xpath = "//input[@name='usuario']"
        return xpath

    def set_field_password(self):
        xpath = "//input[@name='password']"
        return xpath

    def set_combo_language(self):
        xpath = "//select[@id='language']"
        return xpath

    def set_button_signin(self):
        xpath = "//input[@id='Entrar']"
        return xpath

    def set_message_alert_wrong_login(self):
        xpath = "//h2"
        return xpath

    def set_logout_memos(self):
        xpath = "//*[@id='menu_user']/li[2]/a"
        return xpath