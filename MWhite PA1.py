# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:57:36 2024

@author: MGWhite
"""
import random
from tabulate import tabulate
import time

percent_data = [
    ["1D"],
    ["2D"],
    ["3D"],
]
time_data = [["3D"]]

def choose_axis():
    axis = random.choice(['x','y','z'])
    return axis

def choose_movement():
    move = random.choice([-1,1])
    return move

def experiment_in_1d(n):
    x = 0
    for i in range(n):
        x += choose_movement()
        if x == 0:
            return True
    return False

def experiment_in_2d(n):
    x = 0
    y = 0
    for i in range(n):
        if choose_axis() == 'x':
            x += choose_movement()
        else:
            y += choose_movement()
        if x == y == 0:
            return True
    return False

def experiment_in_3d(n):
    x = 0
    y = 0
    z = 0
    for i in range(n):
        if choose_axis() == 'x':
            x += choose_movement()
        elif choose_axis() == 'y':
            y += choose_movement()
        else:
            z += choose_movement()
        if x == y == z == 0:
            return True
    return False
        
def main():
    for dimension in range(3):
        for i in range(6):
            steps = 2 * 10**(i+1)
            counter = 0
            
            if dimension == 2:
                start = time.time()
                
            for j in range(100):
                if dimension == 0:
                    origin_hit = experiment_in_1d(steps)
                elif dimension == 1:
                    origin_hit = experiment_in_2d(steps)
                else:
                    origin_hit = experiment_in_3d(steps)
                
                if origin_hit == True:
                    counter += 1
                    
            if dimension == 2:
                finish = time.time()
                total_time = finish - start
                time_data[0].append(total_time)
                
            percent_data[dimension].append(counter)
        
        
        
    # Table headers
    headers = ["Dimension", "20", "200", "2000", "20000", "200000", "2000000"]

    # Use the tabulate function to format the data into a table
    percent_table = tabulate(percent_data, headers, tablefmt="grid")
    time_table = tabulate(time_data, headers, tablefmt="grid")

    # Print the formatted table
    print(percent_table)
    print(time_table)
    
    
    
main()
