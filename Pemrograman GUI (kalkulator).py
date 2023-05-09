#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from math import pow, sqrt

window = Tk()
window.title("Kalkulator GUI dengan Python")
window.geometry('400x300')

lbl = Label(window, text="Masukan Nilai Pertama : ", anchor="e", width=20)
lbl.grid(column=0, row=0)

lbl2 = Label(window, text="Masukan Nilai Kedua : ", anchor="e", width=20)
lbl2.grid(column=0, row=1)

lbl3 = Label(window, text="Hasil : ", anchor="e", width=20)
lbl3.grid(column=0, row=2)

nilai1 = Entry(window, width=20)
nilai1.grid(column=1, row=0)

nilai2 = Entry(window, width=20)
nilai2.grid(column=1, row=1)

hasil = Label(window, text="0", anchor="w", width=20)
hasil.grid(column=1, row=2)

def tambah():
    hasil.configure(text=(float(nilai1.get())+float(nilai2.get())))

def kurang():
    hasil.configure(text=(float(nilai1.get())-float(nilai2.get())))

def kali():
    hasil.configure(text=(float(nilai1.get())*float(nilai2.get())))

def bagi():
    hasil.configure(text=(float(nilai1.get())/float(nilai2.get())))

def pangkat():
    hasil.configure(text=(pow(float(nilai1.get()), float(nilai2.get()))))

def akar():
    hasil.configure(text=(pow(float(nilai1.get()), 1/float(nilai2.get()))))

def modulus():
    hasil.configure(text=(float(nilai1.get())%float(nilai2.get())))

btnTambah = Button(window, text="Tambah", command=tambah)
btnTambah.grid(column=0, row=3)

btnKurang = Button(window, text="Kurang", command=kurang)
btnKurang.grid(column=1, row=3)

btnKali = Button(window, text="Kali", command=kali)
btnKali.grid(column=2, row=3)

btnBagi = Button(window, text="Bagi", command=bagi)
btnBagi.grid(column=3, row=3)

btnPangkat = Button(window, text="Pangkat", command=pangkat)
btnPangkat.grid(column=0, row=4)

btnAkar = Button(window, text="Akar", command=akar)
btnAkar.grid(column=1, row=4)

btnModulus = Button(window, text="Modulus", command=modulus)
btnModulus.grid(column=2, row=4)

window.mainloop()


# In[ ]:




