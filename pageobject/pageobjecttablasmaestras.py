# -*- coding: utf-8 -*-
from drivers.driverui import DriverUI


class ObjectPageTablasMaestras(DriverUI):

    # CAMBIOS

    def set_link_abm_cambios_contables(self):
        xpath = "//a[contains(text(),'· Cambios Contables')]"
        return xpath
