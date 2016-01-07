# -*- coding: utf-8 -*-
"""
Created on Thu Jan 07 13:47:36 2016

@author: a.fajula
"""

from __future__ import division
from pylab import*
from datetime import datetime

interactive(True)
close('all')

class stardate(object):
    
    def __init__(self, date2convert=datetime.today()):
        
        self.date=date2convert
        self.type='standard'

class gagarin(object):
    
    def __init__(self):
        
        try:
            stardate.__init__(self,date2convert)
        except ValueError:
            pass
        self.type='gagarin'


class cochrane(object):
    
    def __init__(self):
        
        try:
            stardate.__init__(self,date2convert)
        except ValueError:
            pass
        self.type='cochrane'

class cochrane(object):
    
    def __init__(self):
        
        try:
            stardate.__init__(self,date2convert)
        except ValueError:
            pass
        self.type='cochrane'