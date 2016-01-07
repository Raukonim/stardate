# -*- coding: utf-8 -*-
"""
Created on Thu Jan 07 13:47:36 2016

@author: a.fajula
"""

from __future__ import division
from pylab import*
from datetime import datetime, timedelta

interactive(True)
close('all')

class stardate(object):

    def date2stardate(self):
        
        date_difference=self.date-self.start_date
        stardate=date_difference.days/self.stardate_increment
        
        return [date_difference, stardate]
    
    def __init__(self, date2convert=datetime.today()):
        
        year=365.2425
        self.date=date2convert
        self.type='standard'
        self.start_date=datetime.today()-timedelta(days=year)
        self.stardate_increment=year/1000
        #self.date2stardate()
    


class gagarin(stardate):
    
    def __init__(self,date2convert=datetime.today()):
        
        try:
            stardate.__init__(self,date2convert=datetime.today())
        except ValueError:
            pass
        self.type='Gagarin'
        self.start_date=datetime(1961,04,12,06,07,00,000000)
        self.time_diference, self.stardate=self.date2stardate()
        print self.__dict__

class cochrane(stardate):
    
    def __init__(self,date2convert=datetime.today()):
        
        try:
            stardate.__init__(self,date2convert=datetime.today())
        except ValueError:
            pass
        self.type='Cochrane'
        self.start_date=datetime(2063,04,05,11+7,00,00,000000)
        self.time_diference, self.stardate=self.date2stardate()

#class cochrane(object):
#    
#    def __init__(self):
#        
#        try:
#            stardate.__init__(self,date2convert)
#        except ValueError:
#            pass
#        self.type='cochrane'