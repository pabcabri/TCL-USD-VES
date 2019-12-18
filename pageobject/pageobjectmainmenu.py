# -*- coding: utf-8 -*-
from drivers.driverui import DriverUI


class ObjectPageMainMenu(DriverUI):

    # USER

    def set_user_name_1(self):
        xpath = "// span[contains(text(), 'Pablo Cabria')]"
        return xpath

    def set_user_name_2(self):
        xpath = "//span[contains(text(),'Usuario Carga Cambios')]"
        return xpath

    # ADMINISTRACION

    def set_link_abm_tablas_maestras(self):
        xpath = "//a[contains(text(),'Altas, Bajas y Modificaciones de las Tablas Maestr')]"
        return xpath

    # TITLE

    def set_title_tablas_maestras(self):
        xpath = "//h1[@class='title']"
        return xpath

    # LOGIN OUT

    def set_options_icon(self):
        xpath = "//a[@title='Opciones']//img[@height='16']"
        return xpath

    def set_exit_link(self):
        xpath = "//a[@href='index.php?a=exit']"
        return xpath
