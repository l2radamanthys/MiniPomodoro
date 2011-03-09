#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygtk
pygtk.require('2.0')
import gtk

import frm_pomodoro

class MiApp:
    def __init__(self, xml_file=''):
        self.builder = gtk.Builder()
        self.builder.add_from_file(xml_file)

        #creo la ventana
        frm_pomodoro.create(self.builder)

    def main(self):
        #pasar el control principal a GTK
        gtk.main()


    def destroy(self):
        #detener la ejecucion de la aplicacion
        gtk.main_quit()


if __name__ == '__main__':
    app = MiApp("data/interfaz.xml")
    app.main()
