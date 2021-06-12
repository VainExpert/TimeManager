#Kalender  mit UI - Version 0.5
"""
Funktionen:
Kalender fuer Jahr und Rueckgabe des gewaehlten Tages
TODO:
Version 0.9: Kalender an aktuellem Tag beginnen
Version 1.0: Termine eintragen (Holidays)
Version 1.5: Custom-Termine eintragen
Version 2.0: Einbindung in Cmd-Assistant
Version 3.0: Einbindung in A.I.F.E.
"""


# Import Required Library
from tkinter import *
from tkcalendar import Calendar
  
# Create Object
root = Tk()
  
# Set geometry
root.geometry("400x400")
  
# Add Calender
cal = Calendar(root, selectmode = 'day',
               year = 2021, month = 5,
               day = 22)
  
cal.pack(pady = 20)
  
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
  
# Add Button and Label
Button(root, text = "Get Date",
       command = grad_date).pack(pady = 20)
  
date = Label(root, text = "")
date.pack(pady = 20)
  
# Excecute Tkinter
root.mainloop()
