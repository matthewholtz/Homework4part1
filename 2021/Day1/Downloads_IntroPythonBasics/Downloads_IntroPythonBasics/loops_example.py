#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:02:20 2020

@author: mark
"""

# Initialize counters
num_vowels = 0
num_nonvowels = 0
num_chars = 0

target_string = 'Some interesting words'

for letter in target_string:
    num_chars += 1

    if letter in 'aeiou':
        num_vowels += 1
    else:
        num_nonvowels += 1

# This is the newer way of doing formatted printing. The {} are placeholders and can
# contain format strings.
print('There are {} total characters - {} vowels and {} non-vowels.'.format(
        num_chars, num_vowels, num_nonvowels))