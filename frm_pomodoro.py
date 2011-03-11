#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygtk
pygtk.require("2.0")
import gtk
import gobject

from extends import *

#estados
POMODORO = 0
DESCANSO = 1

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
        self.lbl_crono = builder.get_object('lbl_crono')
        self.lbl_estado = builder.get_object('lbl_estado')
        self.t_btn_OnOff = builder.get_object('t_btn_OnOff')

        #conectar seniales
        builder.connect_signals(self)

        #otros
        self.pomodoros = 0 #cantidad de pomodoros q ocurrieron
        self.estado = POMODORO
        self.hora_alarma = get_alarm_hour(self)

        gobject.timeout_add(500, run_clock, self)
        gobject.timeout_add(500, ctlr_alarma, self)

    def on_IconoEstado_activate(self, widget, *argv):
        self.ventana.show_all()


    def on_IconoEstado_popup_menu(self, widget, button, activate_time):
        self.menu.popup(None, None, None, button, activate_time)


    def on_t_btn_OnOff_toggled(self, widget, *argv):
        self.hora_alarma = get_alarm_hour(self)


    def on_btn_siguiente_clicked(self, widget, *argv):
        pass


    def on_btn_minimizar_clicked(self, widget, *argv):
        self.ventana.hide()


    #menu eventos
    def on_OnOff_activate(self, widget, *argv):
        estado = self.t_btn_OnOff.get_active()
        self.t_btn_OnOff.set_active(not(estado))
        self.hora_alarma = get_alarm_hour(self)


    def on_Siguiente_activate(self, widget, *argv):
        pass


    def on_Salir_activate(self, widget, *argv):
        gtk.main_quit()

