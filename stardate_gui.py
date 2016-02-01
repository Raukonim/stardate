# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 12:31:54 2016

@author: a.fajula
"""

from __future__ import division
from pylab import*
from Tkinter import *
# use Tkinter to show a digital clock
import stardate as std

class MyGUI():
    
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = Frame(parent, bg='tan') ###
        self.myContainer1.pack(expand=YES, fill=BOTH)
        
        
       #------ constants for controlling layout ------

        
        buttons_frame_padx = '3m'
        buttons_frame_pady = '2m'
        buttons_frame_ipadx = '3m'
        buttons_frame_ipady = '1m'
        
        background_color='tan'
        
     # top frame
        self.top_frame = Frame(self.myContainer1,
                               height=350,
                               width=600,
                               bg=background_color)
        self.top_frame.pack(
            side=TOP,
            fill=BOTH,
            expand=YES,
            ipadx=buttons_frame_ipadx,
            ipady=buttons_frame_ipady,
            padx=buttons_frame_padx,
            pady=buttons_frame_pady
            )
            
        # mid frame
        self.mid_frame = Frame(self.myContainer1,
                               height=350,
                               width=600,
                               bg=background_color)
        self.mid_frame.pack(
            side=TOP,
            fill=BOTH,
            expand=YES,
            ipadx=buttons_frame_ipadx,
            ipady=buttons_frame_ipady,
            )
        
        #bottom frame        
        self.bottom_frame = Frame(self.myContainer1,
                                  height=50,
                                  width=600,
                                  bg=background_color)
        self.bottom_frame.pack(
            side=BOTTOM,
            fill=X,
            expand=YES
            )

#------------------   TEXT   ------------------------------------
        
        self.standard=Label(self.mid_frame, text='Standard:')
        self.standard.configure(bg=background_color)
        self.standard.grid(row=0, column=0, sticky=W)
        #self.standard.pack(side=TOP, fill=NONE, expand=YES, anchor=W)
        
        self.gagarin=Label(self.mid_frame, text='Gagarin:')
        self.gagarin.configure(bg=background_color)
        self.gagarin.grid(row=1, column=0, sticky=W)
        #self.gagarin.pack(side=TOP, fill=NONE, expand=YES, anchor=W)
        
        self.cochrane=Label(self.mid_frame, text='Cochrane:')
        self.cochrane.configure(bg=background_color)
        self.cochrane.grid(row=2, column=0, sticky=W)
        #self.cochrane.pack(side=TOP, fill=NONE, expand=YES, anchor=W)
        
        self.luna=Label(self.mid_frame, text='Luna:')
        self.luna.configure(bg=background_color)
        self.luna.grid(row=3, column=0, sticky=W)
        #self.luna.pack(side=TOP, fill=NONE, expand=YES, anchor=W)
        
        self.clock_standard=Label(self.mid_frame)
        self.clock_standard.grid(row=0, column=1, sticky=E)
        self.clock_gagarin=Label(self.mid_frame)
        self.clock_gagarin.grid(row=1, column=1, sticky=E)
        self.clock_cochrane=Label(self.mid_frame)
        self.clock_cochrane.grid(row=2, column=1, sticky=E)
        self.clock_luna=Label(self.mid_frame)
        self.clock_luna.grid(row=3, column=1, sticky=E)
        

    def tick(self):
        global time1
        # get the current local time from the PC
        self.time2 = std.stardate().stardate
        self.time3 = std.gagarin().stardate
        self.time4 = std.cochrane().stardate
        self.time5 = std.luna().stardate
        # if time string has changed, update it
        if self.time2 != time1:
            time1 = self.time2
            self.clock_standard.config(text=self.time2,bg=background_color)
            self.clock_gagarin.config(text=self.time3,bg=background_color)
            self.clock_cochrane.config(text=self.time4,bg=background_color)
            self.clock_luna.config(text=self.time5,bg=background_color)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        self.mid_frame.after(1000, mygui.tick())

root = Tk()
mygui=MyGUI(root)
time1 = ''
mygui.tick()
root.mainloop(  )

