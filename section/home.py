# -*- coding: utf-8 -*-
from pageobject.pageobjectmainmenu import ObjectPageMainMenu


class Home(ObjectPageMainMenu):

    def inside_menu_tablas_maestras(self):
        try:
            self.web_driver_wait(self.set_link_abm_tablas_maestras())
            self.click_button(self.set_link_abm_tablas_maestras())
            self.assertEqual(u"Tablas Maestras", self.wait_text(self.set_title_tablas_maestras()))
        except Exception, e:
            print(e)
            self.end_session()
            self.fail(e)
        else:
            print "inside_menu_tablas_maestras"

    def end_session(self):
        try:
            self.web_driver_wait(self.set_options_icon())
            self.click_button(self.set_options_icon())
            self.web_driver_wait(self.set_exit_link())
            self.click_link(self.set_exit_link())
        except Exception, e:
            print(e)
            self.end_session()
            self.fail(e)
        else:
            print "end_session"
