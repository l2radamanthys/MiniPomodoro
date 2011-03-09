#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygtk
pygtk.require("2.0")
import gtk
import gobject

from extends import run_clock, get_alarm_hour


def create(xml):
    return Form(xml)


class Form:
    def __init__(self, builder=None):
        #ventana
        self.ventana = builder.get_object('frm_pomodoro')
        self.ventana.show_all()

        #icono Bandeja
        self.icono_estado = builder.get_object('IconoEstado')

        #menu popup
        self.menu = builder.get_object("menu")

        #otros widget
        self.lbl_tiempo = builder.get_object('lbl_tiempo')
        self.lbl_estado = builder.get_object('lbl_estado')

        #conectar seniales
        builder.connect_signals(self)

        #otros
        self.pomodoros = 0 #cantidad de pomodoros q ocurrieron
        self.hora_alarma = None

        gobject.timeout_add(500, run_clock, self)

    def on_IconoEstado_activate(self, widget, *argv):
        self.ventana.show_all()


    def on_IconoEstado_popup_menu(self, widget, button, activate_time):
        self.menu.popup(None, None, None, button, activate_time)


    def on_btn_minimizar_clicked(self, widget, *argv):
        self.ventana.hide()


    #menu eventos
    def on_OnOff_activate(self, widget, *argv):
        pass


    def on_Siguiente_activate(self, widget, *argv):
        pass


    def on_Salir_activate(self, widget, *argv):
        gtk.main_quit()

