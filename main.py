#imorting datetime time tkinter
import time # for time
import datetime as dt

import tkinter # for messagebox prompt
from tkinter import messagebox

# it will get the time zone  
# of the specified location 
import pytz
IST = pytz.timezone('Asia/Kolkata')
#finish importing all required modules


#setting all the variables

#========================
#1 now stores current time
now=dt.datetime.now(IST)

#2 worktime stores 25 min(seconds)25*60
worktime=15

#3 endwork stores 25 min(minute)
endwork=dt.timedelta(0,worktime)

#4 workstoptime stores the time at which work should be stopped
work_stop_time=now+endwork

#5 5 min(seconds)5*60
breaktime=10

#6 breakstoptimee stores the time at which break should be stopped
break_stop_time=now+dt.timedelta(0,worktime+breaktime)

#7 these variables store the total no. of pomodoro sessions and breaks encountered
pomo_cnt=1
break_cnt=1
#=========================

# message box stuff
bigbox=tkinter.Tk()
bigbox.withdraw()
messagebox.showinfo("Promodoro has sucessfully started","\nThis promodoro started at "+now.strftime("%H:%M")+"hr\nTimer set for 25 minutes from now \nPRESS OK TO ENABLE POMODORO")
# message box stuff ended

#main while Loop
#===============

while(True):
	now=dt.datetime.now(IST)
	if now<work_stop_time:
		continue
	if now==work_stop_time:
		pomo_cnt+=1
		continue
	if ((now>work_stop_time)and(now<=break_stop_time)):
		messagebox.showinfo("work session finished !!","\nNow you can take a break until "+break_stop_time.strftime("%H:%M")+"\nPRESS OK TO ACKNOWLEDGE BREAK")
	
	else:
		messagebox.showinfo("Heyy","\nBreaks done press ok to go the menu")
		usans=messagebox.askyesno(" Break time over ;( ","\nWould you like to continue with another pomodoro session ??")
		if(usans == True):
			pomo_cnt+=1
			now=dt.datetime.now(IST)
			endwork=dt.timedelta(0,worktime)
			work_stop_time=now+endwork
			break_stop_time=now+dt.timedelta(0,worktime+breaktime)
			messagebox.showinfo("Promodoro has sucessfully started","\nThis promodoro started at "+now.strftime("%H:%M")+"hr\nTimer set for 25 minutes from now")
		else:
			messagebox.showinfo("CONGOOOO!!","\nYou have finished "+ str(pomo_cnt)+" today!!\nbyee!!and keep staying productive")
			break;







