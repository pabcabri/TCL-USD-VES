# -*- coding: utf-8 -*-
from pageobject.pageobjecttablasmaestras import ObjectPageTablasMaestras
from section.home import Home


class TablasMaestras(ObjectPageTablasMaestras, Home):

    def inside_menu_cambios_contables(self):
        try:
            self.web_driver_wait(self.set_link_abm_cambios_contables())
            self.click_button(self.set_link_abm_cambios_contables())
        except Exception, e:
            print(e)
            self.end_session()
            self.fail(e)
        else:
            print "inside_menu_cambios_contables"
