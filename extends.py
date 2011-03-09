#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import datetime


#stributos para usar con el Markup
TAG_ATRIB_H = 'font_desc="Alien Encounters 44"'
TAG_INI_H = "<span %s>" %TAG_ATRIB_H
TAG_END_H = "</span>"


def get_alarm_hour(mi_form):
    t1 = datetime.timedelta(minutes=25)
    t2 = time.localtime()
    t3 = datetime.timedelta(hours=t2.tm_hour, minutes=t2.tm_min, seconds=t2.tm_sec)
    return t3 + t1


def run_clock(mi_form):
    """
        Actualiza la etiqueta que muestra la hora del reloj
    """
    hora = time.strftime("%H:%M:%S")
    mi_form.lbl_tiempo.set_markup(TAG_INI_H + hora + TAG_END_H)
    return True
