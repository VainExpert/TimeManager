

from tkinter import *
from tkinter.ttk import *
from math import *
import datetime
import platform
import winsound #windows-specific
from InternationalHolidays import internationalDays
#Deutsche Wochentage
import locale
locale.setlocale(locale.LC_ALL, "de_DE")

"""
TODO:
Feiertage => Performance verbessern,
Tetris-Animation-Clock, Sun-Animation-Clock
"""

#Initialize TKinter Window
window = Tk()
window.title("Clock")
window.geometry('1024x512')

#Help Variable fuer Special Day
year = datetime.datetime.today().strftime("%Y")
feiertage = internationalDays(int(year))
feiertage.baseGermanDays()

#Help Variables for Stopwatch
stopwatch_counter_num = 66600
stopwatch_running = False

#Help Variables for Timer
timer_counter_num = 66600
timer_running = False

#Help Variable for WordClock
words = """
        E S Y I S T L F Ü N F \n
        Z E H N Z W A N Z I G \n
        D R E I V I E R T E L \n
        T N A C H G V O R J M \n
        H A L B X Z W Ö L F P \n
        Z W E I N S I E B E N \n
        K D R E I R H F Ü N F \n
        E L F N E U N V I E R \n
        W A C H T R Z E H N S \n
        B S E C H S F M U H R \n
        E V H K I I I I G Z L \n
        """
minPositions = {'1': ['22.16', '22.17'], '2': ['22.16', '22.19'], '3': ['22.16', '22.21'], '4': ['22.16', '22.23'],
                '5': ['2.22', '2.29', '8.10', '8.17'], '10': ['4.8', '4.15', '8.10', '8.17'],
                '15': ['6.16', '6.29','8.10', '8.17'], '20': ['4.16', '4.29', '8.10', '8.17'],
                '25': ['2.22', '2.29', '8.20', '8.25', '10.8', '10.15'], '30': ['10.8', '10.15'],
                '35': ['2.22', '2.29', '8.10', '8.17', '10.8', '10.15'], '40': ['4.16', '4.29', '8.20', '8.25'],
                '45': ['6.8', '6.29'], '50': ['4.8', '4.15', '8.20', '8.25'], '55': ['2.22', '2.29', '8.20', '8.25']}

hourPositions = {'1': ['12.12', '12.19'], '2': ['12.8', '12.19'], '3': ['14.10', '14.17'], '4': ['16.22', '16.29'],
                '5': ['14.24', '14.29'], '6': ['20.10', '20.19'], '7': ['12.18', '12.29'], '8': ['18.10', '18.17'],
                '9': ['16.14', '16.21'], '10': ['18.20', '18.27'], '11': ['16.8', '16.13'], '12': ['10.18', '10.27']}



#Clock Main Function
def clock():
    
    date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    date, time = date_time.split()
    day, month, year = date.split("-")
    spdate = year + "-" + month + "-" + day
    
    date = ".".join(date.split("-"))
    weekday = datetime.datetime.now().strftime('%A')
    kw = datetime.datetime.today().isocalendar()[1]
    outdate = str(kw) + ": " + weekday + ", " + date
    
    special = SpecialName(spdate)
    
    time_label.config(text= time)
    date_label.config(text= outdate)
    special_label.config(text= special)
    time_label.after(1000, clock)

#Clock Get Special Day - Help Function -> Internationale Feiertag-Klasse
def SpecialName(date):

    feiertage.modifyToday()
    names = feiertage.getDay(date)
    
    if names == [] and country == "Error":
        return "Heute ist kein spezieller Tag. :("

    output = "\t\tHeute ist \n"
    for name in names:
        output += name + " und\n"
        
    output = output.strip(" und\n")
    return output
    

#Wordclock Function
def wordClock():
    
    date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    date, time = date_time.split()
    hours, minutes = time.split(":")

    wordclock.tag_remove('highlight', '2.19', '22.24')
        
    for minute, positions in minPositions.items():
        if int(minutes) - 1 == int(minute):
            highlight(positions, wordclock)
            highlight(minPositions['1'], wordclock)
            break

        elif int(minutes) - 2 == int(minute):
            highlight(positions, wordclock)
            highlight(minPositions['2'], wordclock)
            break

        elif int(minutes) - 3 == int(minute):
            highlight(positions, wordclock)
            highlight(minPositions['3'], wordclock)
            break

        elif int(minutes) - 4 == int(minute):
            highlight(positions, wordclock)
            highlight(minPositions['4'], wordclock)
            break

        elif int(minutes) == int(minute):
            highlight(positions, wordclock)
            break

    if int(hours) > 11 and int(hours) < 24:
        hours = int(hours) -12

    for hour, positions in hourPositions.items():
        if int(hours) == int(hour):
            highlight(positions, wordclock)
            break

    wordclock.after(1000, wordClock)

#Wordclock Help Fucntion
def highlight(positions, wordclock):

    for i in range(0, len(positions), 2):
        wordclock.tag_add('highlight', positions[i], positions[i+1])


#Sun-Time
def sunClock():

##    sun_obj = Celestial(200, 200, 10)
    sun = suncanvas.create_oval(200, 200, 225, 225, fill = "yellow", width = 0)
##
##    middlex = 250
##    middley = 400
##
##    path_iter = circular_path(middlex, middley, 0.18, 10)
##    next(path_iter)  # prime generator
##    update_position(suncanvas, id , sun_obj, path_iter)
##    
    suncanvas.after(1000, sunClock)
    suncanvas.pack()

##class Sun(object):
##
##    COS_0, COS_180 = cos(0), cos(180)
##    SIN_90, SIN_270 = sin(90), sin(270)
##
##    def __init__(self, x, y, radius):
##        self.x, self.y = x, y
##        self.radius = radius
##
##    def bounds(self):
##        """Coords of Rectangle around object"""
##        return (self.x + self.radius*self.COS_0,   self.y + self.radius*self.SIN_270,
##                self.x + self.radius*self.COS_180, self.y + self.radius*self.SIN_90)
##
##def circular_path(x, y, radius, delta_ang, start_ang=0):
##    """ Endlessly generate coords of a circular path every delta angle degrees. """
##    ang = start_ang % 360
##    while True:
##        yield x + radius*cos(ang), y + radius*sin(ang)
##        ang = (ang+delta_ang) % 360
##
##def update_position(suncanvas, id, celestial_obj, path_iter):
##    celestial_obj.x, celestial_obj.y = next(path_iter)  # iterate path and set new position
##    # update the position of the corresponding canvas obj
##    x0, y0, x1, y1 = canvas.coords(id)  # coordinates of canvas oval object
##    oldx, oldy = (x0+x1) // 2, (y0+y1) // 2  # current center point
##    dx, dy = celestial_obj.x - oldx, celestial_obj.y - oldy  # amount of movement
##    suncanvas.move(id, dx, dy)  # move canvas oval object that much
##    # repeat after delay
##    suncanvas.after(DELAY, update_position, suncanvas, id, celestial_obj, path_iter)

#Alarm Function
def alarm():
    
    main_time = datetime.datetime.now().strftime("%H:%M %p")
    alarm_time = get_alarm_time_entry.get()
    alarm_time1,alarm_time2 = alarm_time.split(' ')
    alarm_hour, alarm_minutes = alarm_time1.split(':')
    main_time1,main_time2 = main_time.split(' ')
    main_hour1, main_minutes = main_time1.split(':')
    main_hour = main_hour1

    if int(alarm_hour) == int(main_hour) and int(alarm_minutes) == int(main_minutes) and main_time2 == alarm_time2:
        for i in range(3):
                alarm_status_label.config(text='Zeit vorbei!')
                if platform.system() == 'Windows':
                        winsound.Beep(5000,1000)
                                
        get_alarm_time_entry.config(state='enabled')
        set_alarm_button.config(state='enabled')
        get_alarm_time_entry.delete(0,END)
        alarm_status_label.config(text = '')

    else:
        alarm_status_label.config(text='Alarm gestartet!')
        get_alarm_time_entry.config(state='disabled')
        set_alarm_button.config(state='disabled')

    alarm_status_label.after(1000, alarm)

#Stopwatch Counter - Help Function
def stopwatch_counter(label):
    
    def count():
        if stopwatch_running:
                global stopwatch_counter_num
                if stopwatch_counter_num==66600:
                        display="Starting..."
                else:
                        tt = datetime.datetime.fromtimestamp(stopwatch_counter_num) 
                        string = tt.strftime("%H:%M:%S") 
                        display=string 

                label.config(text=display)
                label.after(1000, count)
                stopwatch_counter_num += 1
    count()

#Stopwatch Main Function
def stopwatch(work):
    
    if work == 'start':
        global stopwatch_running
        stopwatch_running=True
        stopwatch_start.config(state='disabled')
        stopwatch_stop.config(state='enabled')
        stopwatch_reset.config(state='enabled')
        stopwatch_counter(stopwatch_label)
                 
    elif work == 'stop':
        stopwatch_running=False
        stopwatch_start.config(state='enabled')
        stopwatch_stop.config(state='disabled')
        stopwatch_reset.config(state='enabled')
                 
    elif work == 'reset':
        global stopwatch_counter_num
        stopwatch_running=False
        stopwatch_counter_num=66600
        stopwatch_label.config(text='Stopwatch')
        stopwatch_start.config(state='enabled')
        stopwatch_stop.config(state='disabled')
        stopwatch_reset.config(state='disabled')

#Timer Counter - Help Function
def timer_counter(label):
    def count():
        global timer_running
        if timer_running:
            global timer_counter_num
            if timer_counter_num == 66600:
                for i in range(3):    
                    display="Zeit vorbei"
                    if platform.system() == 'Windows':
                            winsound.Beep(5000,1000)
                                    
                timer_running=False
                timer('reset')

            else:
                tt = datetime.datetime.fromtimestamp(timer_counter_num) 
                string = tt.strftime("%H:%M:%S") 
                display=string
                timer_counter_num -= 1
                
            label.config(text=display)
            label.after(1000, count)
        count()

#Timer Main Function
def timer(work):
    
    if work == 'start':
        global timer_running, timer_counter_num
        timer_running=True

        if timer_counter_num == 66600:
            timer_time_str = timer_get_entry.get()
            hours,minutes,seconds=timer_time_str.split(':')
            minutes = int(minutes)  + (int(hours) * 60)
            seconds = int(seconds) + (minutes * 60)
            timer_counter_num = timer_counter_num + seconds  

        timer_counter(timer_label)
        timer_start.config(state='disabled')
        timer_stop.config(state='enabled')
        timer_reset.config(state='enabled')
        timer_get_entry.delete(0,END)

    elif work == 'stop':
        timer_running=False
        timer_start.config(state='enabled')
        timer_stop.config(state='disabled')
        timer_reset.config(state='enabled')

    elif work == 'reset':
        timer_running=False
        timer_counter_num=66600
        timer_start.config(state='enabled')
        timer_stop.config(state='disabled')
        timer_reset.config(state='disabled')
        timer_get_entry.config(state='enabled')
        timer_label.config(text = 'Timer')

#Tab Control
tabs_control = Notebook(window)
clock_tab = Frame(tabs_control)
wordclock_tab = Frame(tabs_control)
sunclock_tab = Frame(tabs_control)
alarm_tab = Frame(tabs_control)
stopwatch_tab = Frame(tabs_control)
timer_tab = Frame(tabs_control)
tabs_control.add(clock_tab, text="Clock")
tabs_control.add(wordclock_tab, text="WordClock")
tabs_control.add(sunclock_tab, text="SunClock")
tabs_control.add(alarm_tab, text="Alarm")
tabs_control.add(stopwatch_tab, text='Stopwatch')
tabs_control.add(timer_tab, text='Timer')
tabs_control.pack(expand = 1, fill ="both")

#Tkinter Labels for Clock
time_label = Label(clock_tab, font = 'calibri 45 bold', foreground = 'black')
time_label.pack(anchor='center')
date_label = Label(clock_tab, font = 'calibri 30 bold', foreground = 'black')
date_label.pack(anchor='s')
special_label = Label(clock_tab, font = 'calibri 20 bold', foreground = 'black')
special_label.pack(anchor='s')

#Tkinter Text for Word Clock
wordclock = Text(wordclock_tab, font = 'Courier 15 bold')
wordclock.insert('1.0', words)
wordclock.tag_configure('highlight', foreground='red', relief= 'raised')
wordclock.tag_add('highlight', '2.8', '2.11')
wordclock.tag_add('highlight', '2.14', '2.19')
wordclock.pack(anchor='n')

#Tkinter Canvas for Sun Clock
suncanvas = Canvas(sunclock_tab, bg='black', width=800, height=600)
suncanvas.pack(anchor='center')

#Tkinter Labels for Alarm
get_alarm_time_entry = Entry(alarm_tab, font = 'calibri 15 bold')
get_alarm_time_entry.pack(anchor='center')
alarm_instructions_label = Label(alarm_tab, font = 'calibri 10 bold', text = "Enter Alarm Time. Eg -> 01:30 PM, 01 -> Hour, 30 -> Minutes")
alarm_instructions_label.pack(anchor='s')
set_alarm_button = Button(alarm_tab, text = "Set Alarm", command=alarm)
set_alarm_button.pack(anchor='s')
alarm_status_label = Label(alarm_tab, font = 'calibri 15 bold')
alarm_status_label.pack(anchor='s')

#Tkinter Labels for Stopwatch
stopwatch_label = Label(stopwatch_tab, font='calibri 40 bold', text='Stopwatch')
stopwatch_label.pack(anchor='center')
stopwatch_start = Button(stopwatch_tab, text='Start', command=lambda:stopwatch('start'))
stopwatch_start.pack(anchor='center')
stopwatch_stop = Button(stopwatch_tab, text='Stop', state='disabled',command=lambda:stopwatch('stop'))
stopwatch_stop.pack(anchor='center')
stopwatch_reset = Button(stopwatch_tab, text='Reset', state='disabled', command=lambda:stopwatch('reset'))
stopwatch_reset.pack(anchor='center')

#Tkinter Labels for Timer
timer_get_entry = Entry(timer_tab, font='calibiri 15 bold')
timer_get_entry.pack(anchor='center')
timer_instructions_label = Label(timer_tab, font = 'calibri 10 bold', text = "Enter Timer Time. Eg -> 01:30:30, 01 -> Hour, 30 -> Minutes, 30 -> Seconds")
timer_instructions_label.pack(anchor='s')
timer_label = Label(timer_tab, font='calibri 40 bold', text='Timer')
timer_label.pack(anchor='center')
timer_start = Button(timer_tab, text='Start', command=lambda:timer('start'))
timer_start.pack(anchor='center')
timer_stop = Button(timer_tab, text='Stop', state='disabled',command=lambda:timer('stop'))
timer_stop.pack(anchor='center')
timer_reset = Button(timer_tab, text='Reset', state='disabled', command=lambda:timer('reset'))
timer_reset.pack(anchor='center')

#Start Everything
if __name__ == '__main__':
    clock()
    wordClock()
    sunClock()
    window.mainloop()
