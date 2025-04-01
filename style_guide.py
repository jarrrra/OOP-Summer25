'''
naming convention
'''

#good
MAX_NUMBER = 10
current_number = 1
class Students:
  pass
def calculate_sum():
  pass

#bad
disfbgfh = 1
Currentnumber = 1
class student:
  pass
def Calc():
  pass

'''
indentation & spaces
'''

#good
a = 1
if a > 0:
  print(a)
  if a == 1:
    a = a + 1

def example_func(a, b,
                 c, d):
  pass

class ExampleClass:
  def __init__(self):
    pass


#bad
  a      =     2
if a>0:
print(a)
if a==1:
a = a +1
def example_func(a,b,
  c,d):
            pass
class ExampleClass:
def __init__(self):
    pass


'''
imports
'''

#good
import os
import sys
from subprocess import Popen, PIPE

#bad
import sys, os


'''
function returns
'''

#good
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)

#bad
def foo(x):
    if x >= 0:
        return math.sqrt(x)

def bar(x):
    if x < 0:
        return
    return math.sqrt(x)


'''
catching exceptions
'''

#good
try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)

#bad
try:
    return handle_value(collection[key])
except KeyError:
    return key_not_found(key)
