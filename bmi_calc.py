# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:38:09 2021

@author: 6-17
"""

### Create a BMI Calculation Application

from pywebio.input import *
from pywebio.output import *

def bmicalculator():
    height=input("Please enter the height in cm", type=FLOAT)
    weight=input("Please enter the weight in kg",type=FLOAT)
    
    bmi = weight/(height/100)**2
    
    bmi_output=[(16, 'Severely underweight'), (18.5, 'Underweight'), 
                (25, 'Normal'), (30, 'Overweight'), (35, 'Moderately obese'),
                (float('inf'), 'Severely obese')]
    
    
    for tup1, tup2 in bmi_output:
        if bmi <= tup1:
            put_text("Your BMI is :%.1f and the person is :%s" %(bmi,tup2))
            break


if __name__ == '__main__':
    bmicalculator()