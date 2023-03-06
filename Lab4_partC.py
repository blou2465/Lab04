# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:49:38 2023

@author: anwar
"""

def ConvertToMilitaryTime(time):
    
    #Checks if it is 12:00 AM
    if time[-2:] == "AM" and time[:2] == "12":
        Mil_time = "00" + time[2:-2]
        return Mil_time
    
    #Checks if it is 12 PM or anything past 12:59 AM
    elif (time[-2:] == "PM" and time[:2] == "12") or (time[-2:] == "AM"):
        Mil_time = time[:-2]
        return Mil_time
    
    #Will add 12 to the times from 1:00 PM to 11:59 PM
    else:
        Mil_time = str(int(time[:2]) + 12) + time[2:-2]
        return Mil_time
    
    

print("Enter a time to be converted to military time, e.g. 01:00 PM")
Time = input("Time to be converted to military time : ")

ConvertedTime = ConvertToMilitaryTime(Time)

print("Converted military time: ", ConvertedTime)