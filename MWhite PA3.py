# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 13:07:11 2024
@author: MGWhite
"""

import numpy as np

coeffs1 = [2,3,0,1]  
polynomial = np.poly1d(coeffs1)
print(polynomial)
print('At x = 2:', end = ' ')
print(np.polyval(polynomial,2))

coeffs2 = [1,0,1]
derpoly = np.poly1d(coeffs2)
derivative = np.polyder(derpoly)
print(f'Derivative: {derivative}')
print('At x = 1:', end = ' ')
print(np.polyval(derivative, 1))

def Newton(coefficients, x1, previousX = 0, n = 1):
    if n!= 1 and abs(x1 - previousX) <= 0.001:
        print(f'x_{n} = {x1}')
        return x1
    else:
        print(f'x_{n} = {x1}')
        poly = np.poly1d(coefficients)
        derivative = np.polyder(poly)
        
        poly_at_x1 = np.polyval(poly, x1)
        derivative_at_x1 = np.polyval(derivative, x1)
        
        x2 = x1 - (poly_at_x1 / derivative_at_x1)
        n += 1
        return Newton(coefficients, x2, x1, n)
    
def main():
    example = np.poly1d([1,3,2])
    coefficients = []
    coeffs = input(f'Enter the coefficients for your polynomial separated by commas, for example, the input: 1,3,2 will return the polynomial \n {example} : ')
    coeffs = coeffs.split(',')
    
    for coeff in coeffs:
        coeffInt = float(coeff)
        coefficients.append(coeffInt)
    print(coefficients)
    
    x1 = float(input('Enter your initial guess for the root of your polynomial: '))
    root = Newton(coefficients, x1)
    print(f'The calculated root of your polynomial is: {root: .3f}')
    polynomial = np.poly1d(coefficients)
    roots = np.roots(polynomial)
    print(f'The true root(s) of your polynomial is/are: {roots}')

main()