''' This file contains some sample code for functional programming in Python. 
'''

from functools import reduce
import functools, operator, itertools 
from operator import add
import os 
import sys 
from time import *
import math  
    
def is_even(x):
    return (x % 2) == 0


line_list = ['  line 1\n', 'line 2  \n', '' ]

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)
stripped_iter

# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list] 


m = list(map(lambda x: x+1, list(range(1,5))))
print("sample map on one list")
print(m)



objfun = ((lambda x: x+1))
print(list(map(objfun, list(range(1,5)))))


l = list(filter(is_even, range(10)))

print(l)



# let's create an execution utility function
#do_it = lambda f: f() ## for python 2 
do_it = lambda f: list(f)

# let f1, f2, f3 (etc) be functions that perform actions

f1 = map(lambda x: x+1,list(range(1,5)))
#print(list(f1))
f2 = filter(is_even, range(10))
#f3 = 
 
f_sequence = ((map(do_it, [f1,f2])))   # map()-based action sequence

print("The sequence of map and filter function result is: ", list(f_sequence))


 
bigmuls = lambda xs,ys: filter(lambda x,y :x*y > 25,  list(combine(xs,ys)))
combine = lambda xs,ys: map(None, xs*len(ys), dupelms(ys,len(xs)))
dupelms = lambda lst,n: reduce(lambda s,t:s+t, map(lambda l,n=n: [l]*n, lst))
#print(bigmuls((1,2,3,4),(10,15,3,22)))


print([(x,y) for x in (1,2,3,4) for y in (10,15,3,22) if x*y > 25] )

ad = functools.reduce(operator.add, [1,2,3,4], 0)
print(ad)

product = functools.reduce(operator.mul, [1,2,3], 1)
print(product)

ac  = itertools.accumulate([1,2,3,4,5], operator.mul)

for e in ac:  print(e, end=" ")
print()


people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

heights = map(lambda x: x['height'],
              filter(lambda x: 'height' in x, people))

heights = list(heights)

if len(heights) > 0:
    average_height = reduce(add, heights) / len(heights)
    print(average_height)
    
expr = "28+32+++32++39"
print(reduce(add, map(int, filter(bool, expr.split("+")))))


# first class function 

def calculations(a, b):
    def add():
        return a + b

    return a, b, add()

print(calculations(3, 5))


# high ordered funtions 

def speak(topic):
    print("My speach is " + topic) 

def timer(fn):
    def inner(*args, **kwargs):
        t = time()
        fn(*args, **kwargs)
        print("took {time}".format(time=time()-t))

    return inner

speaker = timer(speak)
speaker("FP with Python")

@timer
def speak2(topic):
    print("My speach is " + topic)
    
speak2("FP with Python")


def log(level, message):
    print("[{level}]: {msg}".format(level=level, msg=message))					

from functools import partial
debug = partial(log, "debug")

debug("Start doing something")
debug("Continue with something else")
debug("Finished. Profit?")



### Here is currying 
def fsum(f):
    def apply(a, b):
        return sum(map(f, range(a,b+1)))
    return apply

log_sum = fsum(math.log)
square_sum = fsum(lambda x: x**2)
simple_sum = fsum(int) ## fsum(lambda x: x)

print(simple_sum(1,10))

print(fsum(lambda x: x*2)(1, 10))
print(fsum(functools.partial(operator.mul, 2))(1, 10))

### standard library currying 

from operator import itemgetter
print(itemgetter(3)([1,2,3,4,5])) 

from operator import attrgetter as attr


class Speaker(object):
    def __init__(self, name):
          self.name = "[name] " + name
          
alexey = Speaker("Alexey")
print(attr("name")(alexey))

from operator import methodcaller
methodcaller("__str__")([1,2,3,4,5])


print(methodcaller("keys")(dict(name="Alexey", topic="FP"))) 

values_extractor = methodcaller("values")
print(values_extractor(dict(name="Alexey", topic="FP")))


# good function is small function 

ss = ["UA", "PyCon", "2012"]
#bad
reduce(lambda acc, s: acc + len(s), ss, 0)
# not bad 
reduce(lambda l,r: l+r, map(lambda s: len(s), ss))
# good  
reduce(operator.add, map(len, ss))

#hints : types are callable 
map(str, range(5))

# hints: CLASSES ARE CALLABLE
map(Speaker, ["Alexey", "Andrey", "Vsevolod"]) 

# hint : INSTANCE METHODS ARE CALLABLE 
print(list(map([1,2,3,4,5].count, [1,2,3,10,11])))

#THINK FUNCTIONAL: DATA
#ASSUME THAT WE DON'T HAVE DICT

def dct(*items):
    def pair(key_value):
        key, value = key_value
        return lambda k: value if k == key else None

    def merge(l, r):
        return lambda k: l(k) or r(k)

    return reduce(merge, map(pair, items), pair((None, None)))

me = dct(("name", "Alexey"), ("topic", "FP with Python"))
print(me("name"))
print(me("topic"))
print(me(("ask")))