#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import datetime


#stributos para usar con el Markup
TAG_ATRIB = 'font_desc="Alien Encounters 33"'
TAG_INI = "<span %s>" %TAG_ATRIB
TAG_END = "</span>"

#estados
POMODORO = 0
DESCANSO = 1


def get_alarm_hour(mi_form, min=25):
    """
        devuelve tiempo restante del pomodoro
    """
    if mi_form.t_btn_OnOff.get_active():
        t1 = datetime.timedelta(minutes=min)
        t2 = time.localtime()
        t3 = datetime.timedelta(hours=t2.tm_hour, minutes=t2.tm_min, seconds=t2.tm_sec)
        return t3 + t1
    else:
        return datetime.timedelta()


def show_dialog(msj=''):
    """
        Generarara un MensajeDialog que Dice Alarma
    """
    mi_dialog = gtk.MessageDialog(buttons=gtk.BUTTONS_OK)
    mi_dialog.set_markup(TAG_INI + msj + TAG_END)
    mi_dialog.run()
    mi_dialog.hide()


def run_clock(mi_form):
    """
        Actualiza la etiqueta que muestra la hora del reloj
    """
    hora = time.strftime("%H:%M:%S")
    mi_form.lbl_tiempo.set_markup(TAG_INI + hora + TAG_END)

    if mi_form.t_btn_OnOff.get_active():
        t1 = time.localtime()
        t2 = datetime.timedelta(hours=t1.tm_hour, minutes=t1.tm_min, seconds=t1.tm_sec)
        crono = mi_form.hora_alarma - t2
        h = str(crono.seconds / 3600).zfill(2)
        m = str((crono.seconds % 3600) / 60).zfill(2)
        s = str(crono.seconds % 60).zfill(2)
        mi_form.lbl_crono.set_markup(TAG_INI + "%s:%s:%s" %(h,m,s) + TAG_END)

        if mi_form.estado == DESCANSO:
                if mi_form.pomodoros != 0 and mi_form.pomodoros % 4 == 0:
                    mi_form.lbl_estado.set_markup(TAG_INI + "DESCANSAR" + TAG_END)
                else:
                    mi_form.lbl_estado.set_markup(TAG_INI + "INTERVALO" + TAG_END)

        elif mi_form.estado == POMODORO:
            mi_form.lbl_estado.set_markup(TAG_INI + "TRABAJAR" + TAG_END)

    else:
        mi_form.lbl_estado.set_markup(TAG_INI + "DETENIDO" + TAG_END)
    return True


def ctlr_alarma(mi_form):
    if mi_form.t_btn_OnOff.get_active():
        t1 = time.localtime()
        t2 = datetime.timedelta(hours=t1.tm_hour, minutes=t1.tm_min, seconds=t1.tm_sec)
        crono = mi_form.hora_alarma - t2
        if crono.seconds == 0:
            if mi_form.estado == POMODORO:
                if self.pomodoros != 0 and self.pomodoros % 4 == 0:
                    show_dialog("TOMAR UN DESCANSO")
                    self.hora_alarma = get_alarm_hour(mi_form, 30)

                else:
                    show_dialog("HACER UN INTERVALO")
                    self.hora_alarma = get_alarm_hour(mi_form, 5)

            elif mi_form.estado == DESCANSO:
                show_dialog("VOLVER A TRABAJAR")
                mi_form.hora_alarma = get_alarm_hour(mi_form, 25)
                mi_form.pomodoros += 1

            mi_form.estado = not(mi_form.estado)

    return True
