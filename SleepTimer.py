
import os
import tkinter as tk

parent = tk.Tk()
parent.geometry("290x220+40+40")

def shutdown():
    seconds = int(mins.get()) * 60
    os.system("shutdown -s -t {}".format(seconds))


def cancel():
    os.system("shutdown -a")
    return


tk.Label(parent, text="Shutdown Sleep Timer", font=('Calibri 20')).place(x = 20, y = 20)
tk.Label(parent, text="In wie vielen Minuten herunterfahren?", font=('Calibri 10')).place(x = 30, y = 60)

mins = tk.Entry(parent, width=35)
mins.place(x = 30, y = 100)

go_shutdown = tk.Button(parent, 
                   text="Herunterfahren starten", 
                   command=shutdown
                   )
go_shutdown.place(x = 20, y = 150)

cancel_shutdown = tk.Button(parent, 
                   text="Abbrechen", 
                   command=cancel
                   )
cancel_shutdown.place(x = 180, y = 150)

quit_button = tk.Button(parent, 
                   text="Ende", 
                   command=quit
                   )
quit_button.place(x = 130, y = 190)

parent.mainloop()