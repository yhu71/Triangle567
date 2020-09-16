# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def test001_InvalidInput(self):
        self.assertEqual(classifyTriangle("s", 1, 1), 'InvalidInput', 'Invalid input validation failed')

    def test002_InvalidInput(self):
        self.assertEqual(classifyTriangle(0, 3, 4), 'InvalidInput', 'Invalid input validation failed')

    def test003_InvalidInput(self):
        self.assertEqual(classifyTriangle(0, -3, -4), 'InvalidInput', 'Invalid input validation failed')

    def test004_NotTriangle(self):
        self.assertEqual(classifyTriangle(4, 6, 1), 'NotTriangle', 'Not triangle validation failed')

    def test005_NotTriangle(self):
        self.assertEqual(classifyTriangle(4, 6, 10), 'NotTriangle', 'Not triangle validation failed')

    def test006_EquilateralTriangle(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','Equilateral triangle validation failed')

    def test007_EquilateralTriangle(self):
        self.assertEqual(classifyTriangle(1.2,1.2,1.2),'Equilateral','Equilateral triangle validation failed')

    def test008_RightTriangle(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','Right triangle validation failed')

    def test009_RightTriangle(self):
        self.assertEqual(classifyTriangle(2,4,4.4721),'Right','Right triangle validation failed')

    def test010_IsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(3.3, 3.3, 5.9),'Isosceles','Isosceles triangle validation failed')

    def test011_RightAndIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(2.82842712475, 2.82842712475, 4),'Isosceles and Right',
                         'Isosceles and Right triangle validation failed')

    def test012_ScaleneTriangle(self):
        self.assertEqual(classifyTriangle(1.18, 2.01, 3.1),'Scalene',
                         'Scalene triangle validation failed')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

