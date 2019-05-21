
# coding: utf-8

# # Table of Contents
#  <p>

# In[14]:

import datetime

class ParkingLot(object):
    """
        20151007 parking lot OOP practice
    """

    def __init__(self, name, capacity = 1):
        ''' return a ParkingLot object with name "name" '''

        self.name = name
        self.capacity = capacity
        self.earnings = 0
        # QUESTION: how to correctly set the hourly rate?
        self.rate = 1
    
        self.carsAndEnterTime = {}

    def SetCapacity(self, newCap):
        ''' change the capacity from the default 1 '''
        if newCap < 1:
            # QUESTION: correct way of throwing exception?
            raise RunTimeError("Error: parking lot size cannot be less than 1")

        self.capacity = newCap

    def GetCapacity(self):
        ''' return parking lot capacity '''
        return self.capacity

    def GetEarnings(self):
        ''' return how much much parking has made '''
        return self.earnings

    def VehicleEnters(self, vehicle):
        ''' vehicle enters parking lot'''
    
    # put car and its enter time in a dictionary
        self.carsAndEnterTime[vehicle] = datetime.datetime.now()   

        if self.capacity == 0:
            raise RuntimeError("Error: Parking lot full!")

        self.capacity -= 1

    def VehicleLeaves(self, vehicle):
        ''' vehicle leaves parking lot. when it leaves, charges money '''
    
        secondsDiff = datetime.datetime.now() - self.carsAndEnterTime[vehicle]
        self.earnings += self.rate*secondsDiff.seconds
        # after earned money, delete vehicle from dictionary
        del self.carsAndEnterTime[vehicle]

        self.capacity += 1

    def SetSecondlyRate(self, rate=0):
        ''' how much to charge per second '''
        self.rate = rate
  
    def __str__(self):
        ''' prints basic information of parking lot '''
        return "Parking lot: " + self.name + "\nSpots open: " + str(self.capacity) + "\nHourly rate: " + str(self.rate) + "\n" + str(self.carsAndEnterTime) + "\nEarnings: $" + str(self.earnings)


# In[15]:

import unittest
#from ParkingLot import *

class Test_Parkinglot(unittest.TestCase):
    emptyParkingLot = ParkingLot("empty", 0)
    p1 = ParkingLot("p1", 0)

    def test_GetCapacity(self):
        self.assertEqual(emptyParkingLot.GetCapacity(), 0)

    def test_SetCapacity(self):
        self.p1.SetCapacity(100)  
        self.assertTrue(p1.capacity, 100)

if __name__ == '__main__':
    unittest.main()


# In[11]:

help(unittest)


# In[ ]:



