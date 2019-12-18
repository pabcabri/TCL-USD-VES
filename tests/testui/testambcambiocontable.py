# -*- coding: utf-8 -*-
from section.login import Login
from section.tablasmaestras import TablasMaestras
from section.cambioscontables import CambiosContables


class TestABMCambioContable(Login, TablasMaestras, CambiosContables):
    def test_00_flows_abm_cambio_contable(self):
        self.signing_in()
        self.inside_menu_tablas_maestras()
        self.inside_menu_cambios_contables()
        self.search_cambio_contable()
        self.end_session()

    def test_01_flows_abm_cambio_contable_laser(self):
        self.signing_in_laser_produccion()
        self.inside_menu_tablas_maestras()
        self.inside_menu_cambios_contables()
        self.search_cambio_contable()
        self.end_session()

    def test_02_flows_abm_cambio_contable_estelar(self):
        self.signing_in_estelar_produccion()
        self.inside_menu_tablas_maestras()
        self.inside_menu_cambios_contables()
        self.search_cambio_contable()
        self.end_session()

    def test_03_flows_abm_cambio_contable_aruba(self):
        self.signing_in_aruba_produccion()
        self.inside_menu_tablas_maestras()
        self.inside_menu_cambios_contables()
        self.search_cambio_contable()
        self.end_session()

    def test_04_flows_abm_cambio_contable_airpanama(self):
        self.signing_in_airpanama_produccion()
        self.inside_menu_tablas_maestras()
        self.inside_menu_cambios_contables()
        self.search_cambio_contable()
        self.end_session()
