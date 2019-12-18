# -*- coding: utf-8 -*-
from drivers.driverui import DriverUI


class ObjectPageCambiosContables(DriverUI):

    # CAMBIOS CONTABLES

    def set_title_abm_cambios_contables(self):
        xpath = "//h1[@class='title']"
        return xpath

    def set_error_message(self):
        xpath = "//h2[@class='error']"
        return xpath

    # BUSCADOR

    def set_search_bar(self):
        xpath = "//input[@id='search_text']"
        return xpath

    def set_search_button(self):
        xpath = "//input[@id='Buscar']"
        return xpath

    def set_search_result(self):
        xpath = "//a[contains(text(),'" + self.getTodayWithFormatYMD() + "')]"
        return xpath

    def set_not_result(self):
        xpath = "//b[contains(text(),'No hay registros disponibles')]"
        return xpath

    # FORMULARIO DE ALTA

    def set_field_fecha_desde(self):
        xpath = "//input[@id='fecha_desde']"
        return xpath

    def set_field_fecha_hasta(self):
        xpath = "//input[@id='fecha_hasta']"
        return xpath

    def set_combo_moneda_1(self):
        xpath = "//select[@id='moneda1']"
        return xpath

    def set_combo_moneda_2(self):
        xpath = "//select[@id='moneda2']"
        return xpath

    def set_field_cambio(self):
        xpath = "//input[@id='cambio']"
        return xpath

    def set_agregar_button(self):
        xpath = "//input[@id='Agregar']"
        return xpath

    def set_cancelar_button(self):
        xpath = "//input[@value='Cancelar']"
        return xpath

    # FORMULARIO DE MODIFICACION Y ELIMINACION

    def set_modificar_button(self):
        xpath = "//input[@id='Modificar']"
        return xpath

    def set_eliminar_button(self):
        xpath = "//input[@value='Eliminar']"
        return xpath
