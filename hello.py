#!/usr/bin/env python3
# -*- coding: latin-1 -*-
# Desenvolvimento Aberto
# hello.py
 
'''
Created on 21/09/2014
 
@author: Desenvolvimento Aberto
'''
# importa modulo
from Tkinter import Frame
from Tkinter import Tk
from Tkinter import Label
 
# Cria classe hello
class hello(Frame):
 
    # Construtor da classe
    def __init__(self, formulario=None):
        Frame.__init__(self, formulario)
        # Cria texto
        texto = "PyDev - Python IDE for Eclipse - Linux" + \
                "\n\n\n\nDesenvolvimento Aberto\n\nHello World\n\nTkinter!!!!"              
 
        # Cria um novo label
        rotulo = Label(self, text = texto)
 
        # Retira espaço desocupado na janela
        rotulo.pack(padx=70, pady=30)
        self.pack()
 
# Cria aplicação
root = Tk(className="..::Desenvolvimento Aberto::.. - Linux")
app = hello(formulario=root)
app.mainloop()