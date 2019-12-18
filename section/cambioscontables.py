# -*- coding: utf-8 -*-
from pageobject.pageobjectcambioscontables import ObjectPageCambiosContables
from drivers.driverrequests import DriverRequests
from section.home import Home
import time
import datetime


class CambiosContables(ObjectPageCambiosContables, DriverRequests, Home):
    def add_new_cambio_contable(self):
        try:
            self.web_driver_wait(self.set_field_fecha_desde())
            self.fill_fields(self.set_field_fecha_desde(), self.getTodayWithFormat())
            self.web_driver_wait(self.set_field_fecha_hasta())
            self.fill_fields(self.set_field_fecha_hasta(), self.getTodayWithFormat())
            self.web_driver_wait(self.set_combo_moneda_1())
            self.value_select(self.set_combo_moneda_1(), 'USD')
            self.web_driver_wait(self.set_combo_moneda_2())
            self.value_select(self.set_combo_moneda_2(), 'VES')
            self.web_driver_wait(self.set_field_cambio())
            self.fill_fields(self.set_field_cambio(), str(self.data_responses()))
            self.web_driver_wait(self.set_agregar_button())
            self.click_button(self.set_agregar_button())
        except Exception, e:
            print(e)
            self.end_session()
            self.fail(e)
        else:
            print "add_new_cambio_contable"

    def add_new_cambio_contable_saturday(self):
        try:
            self.web_driver_wait(self.set_field_fecha_desde())
            self.fill_fields(self.set_field_fecha_desde(), self.date_process_sat())
            self.web_driver_wait(self.set_field_fecha_hasta())
            self.fill_fields(self.set_field_fecha_hasta(), self.date_process_sat())
            self.web_driver_wait(self.set_combo_moneda_1())
            self.value_select(self.set_combo_moneda_1(), 'USD')
            self.web_driver_wait(self.set_combo_moneda_2())
            self.value_select(self.set_combo_moneda_2(), 'VES')
            self.web_driver_wait(self.set_field_cambio())
            self.fill_fields(self.set_field_cambio(), str(self.data_responses()))
            self.web_driver_wait(self.set_agregar_button())
            self.click_button(self.set_agregar_button())
        except Exception, e:
            print(e)
            self.end_session()
            self.fail(e)
        else:
            print "add_new_cambio_contable_saturday"

    def add_new_cambio_contable_sunday(self):
        try:
            self.web_driver_wait(self.set_field_fecha_desde())
            self.fill_fields(self.set_field_fecha_desde(), self.date_process_sun())
            self.web_driver_wait(self.set_field_fecha_hasta())
            self.fill_fields(self.set_field_fecha_hasta(), self.date_process_sun())
            self.web_driver_wait(self.set_combo_moneda_1())
            self.value_select(self.set_combo_moneda_1(), 'USD')
            self.web_driver_wait(self.set_combo_moneda_2())
            self.value_select(self.set_combo_moneda_2(), 'VES')
            self.web_driver_wait(self.set_field_cambio())
            self.fill_fields(self.set_field_cambio(), str(self.data_responses()))
            self.web_driver_wait(self.set_agregar_button())
            self.click_button(self.set_agregar_button())
        except Exception, e:
            print(e)
            self.end_session()
            self.fail(e)
        else:
            print "add_new_cambio_contable_sunday"

    def select_result_cambio_contable(self):
        try:
            self.web_driver_wait(self.set_search_result())
            self.click_link(self.set_search_result())
        except Exception, e:
            print(e)
            self.end_session()
            self.fail(e)
        else:
            print "select_result_cambio_contable"

    def update_cambio_contable(self):
        try:
            self.web_driver_wait(self.set_field_cambio())
            self.clean_fields_keyboard(self.set_field_cambio())
            self.fill_fields(self.set_field_cambio(), str(self.data_responses()))
            self.click_button(self.set_modificar_button())
        except Exception, e:
            print(e)
            self.end_session()
            self.fail(e)
        else:
            print "update_cambio_contable"

    def search_cambio_contable(self):
        try:
            self.web_driver_wait(self.set_search_bar())
            self.fill_fields(self.set_search_bar(), self.getTodayWithFormatYMD() + 'USDVES')
            self.click_button(self.set_search_button())
        except Exception, e:
            print(e)
            self.end_session()
            self.fail(e)
        else:
            print "search_cambio_contable"
            if self.web_driver_wait_bool(self.set_not_result()) is True:
                if self.data_date_process() == 'Viernes':
                    self.add_new_cambio_contable()
                    self.add_new_cambio_contable_saturday()
                    self.add_new_cambio_contable_sunday()
                else:
                    self.add_new_cambio_contable()
            elif self.data_date_process() == 'Viernes':
                self.select_result_cambio_contable()
                self.update_cambio_contable()
                self.add_new_cambio_contable_saturday()
                self.add_new_cambio_contable_sunday()
            else:
                self.select_result_cambio_contable()
                self.update_cambio_contable()

    def date_process_sat(self):
        if self.data_date_process() == 'Viernes':
            fecha = datetime.datetime.now() + datetime.timedelta(days=1)
            sat = str(fecha.strftime('%d/%m/%Y'))
            return sat

    def date_process_sun(self):
        if self.data_date_process() == 'Viernes':
            fecha = datetime.datetime.now() + datetime.timedelta(days=2)
            sun = str(fecha.strftime('%d/%m/%Y'))
            return sun
