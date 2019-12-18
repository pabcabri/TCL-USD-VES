# -*- coding: utf-8 -*-
from pageobject.pageobjectlogin import ObjectPageLogin
from pageobject.pageobjectmainmenu import ObjectPageMainMenu


class Login(ObjectPageLogin, ObjectPageMainMenu):

    def login(self, url, user, pwd):
        self.getUrl(url)
        self.fill_fields(self.set_field_username(), user)
        self.fill_fields(self.set_field_password(), pwd)
        self.click_button(self.set_button_signin())

    def signing_in(self):
        try:
            self.login("https://kiuadmin.kiusys.com/kiuadmin-ratd-qa/", "pcabria", "R@b@T0")
        except Exception, e:
            print "Login incorrecto"
            self.fail(e)
        else:
            print "Login correcto"

    def signing_in_laser_produccion(self):
        try:
            self.login("https://admin.kiusys.net/laser/index.php", "jnk", "Toto123*")
        except Exception, e:
            print "Login incorrecto"
            self.fail(e)
        else:
            print "Login correcto"

    def signing_in_estelar_produccion(self):
        try:
            self.login("https://admin.kiusys.net/estelar/index.php", "jnk", "Toto123*")
        except Exception, e:
            print "Login incorrecto"
            self.fail(e)
        else:
            print "Login correcto"

    def signing_in_aruba_produccion(self):
        try:
            self.login("https://admin.kiusys.net/aruba/index.php", "jnk", "Toto123*")
        except Exception, e:
            print "Login incorrecto"
            self.fail(e)
        else:
            print "Login correcto"

    def signing_in_airpanama_produccion(self):
        try:
            self.login("https://admin.kiusys.net/airpanama/index.php", "jnk", "Toto123*")
        except Exception, e:
            print "Login incorrecto"
            self.fail(e)
        else:
            print "Login correcto"
