# look at the functional coding for python also 

# PEP8 
# pylint
import time 
#import six 
#import click
import random
from collections import Counter
count = dict(Counter("testString"))
from operator import itemgetter, attrgetter 
###############

# string
s = "testString"
sub = "sub"
sub in s 
s[1: 2] # start: end
s.upper()
s.lower()
s.find(sub) 
s.count(sub)
s.startswith(sub) 
s.endswith(sub)
s.isalnum()
s.isalpha() # all letters in alphabet 
s.isdigit()
s.islower() # at leas one alphabet and is lower 
s.isupper()
s.isspace()
s.split()
s.split("\t") 
s.rstrip() # trailing 
s.lstrip() # leading 
s.strip()

###############
# tuples
t = (10, 1) 
t[0]
###############
# list
l = []
l = ["one"]
"x" in l 
l.append("y") 
l.sort() # in-place
l.sort(key = len, reverse=False)
l.reverse() # in-place 
sorted(l) # return a new list 

##############
# use list as stacks 
stack = [1, 2, 3]
stack.append(4)
stack.pop(stack.index(2))
print(stack)
##############
#  queue 
import queue
q = queue.Queue() # LifoQueue, PriorityQueue 
q.empty()
q.full()
q.put('v')
q.get()
q.qsize
###############
import collections 
''' This module implements specialized container datatypes providing
alternatives to Python's general purpose built-in containers, dict,
list, set, and tuple.

* namedtuple   factory function for creating tuple subclasses with named fields
* deque        list-like container with fast appends and pops on either end
* ChainMap     dict-like class for creating a single view of multiple mappings
* Counter      dict subclass for counting hashable objects
* OrderedDict  dict subclass that remembers the order entries were added
* defaultdict  dict subclass that calls a factory function to supply missing values
* UserDict     wrapper around dictionary objects for easier dict subclassing
* UserList     wrapper around list objects for easier list subclassing
* UserString   wrapper around string objects for easier string subclassing

'''
q = collections.deque() # it serves as a two sided queue, linked list or list
q.append('elm')
q.remove('elm')
q.appendleft('elm')
q[0]
q[-1]
###############
# set 
s = set()
s = set(list([1, 2, 3]))
s = {4, 5}
6 in s 
len(s) 
s.add(6) 
s.remove(4)
s == s 
s.issubset(s)
s.union(s)
s.intersection(s) 
s.difference(s)
###############
# dict, can be used also for storing graphs 
d = {}
d = dict()
d = {'k1': 'v1', 'k2': 'v2', 'k3': 'v2'}
'k' in d 
v = d['k1']
v = d.get('k', 'defaultvalue') 
len(d) 
v = d.pop("k2") # keyError
del d["k3"]
d.keys()
d.values()
d.items()
for k, v in d.items(): 
    print(k, v) 
    
################
import heapq # for min/max heap
# a priority queue also can be used as a heap
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)        # for a maxheap!!


################
#random 
import random as r 
r.random() # [0.0, 1.0)
r.randint(10, 20) 
r.randrange(100, 10000, step = 2) 
#r.sample(population, k) 
r.sample(range(1000), 13) 

################
#extra
sqrs = [x **2 for x in range(10)] 

################
n = int(input())
list_num = [int(i) for i in input().strip().split(' ')]
a, b = input().strip().split(' ')
###############
import time 
import functools, inspect

def timing_it(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        return (t2 - t1), res, func.__name__
    return wrapper
@timing_it
def foo(): 
    return True 
###############
# files 
with open("python_cheat_sheet.py", "r") as f: 
    s = f.read()
    s = f.readline()
    s = f.readlines()
    
f.close()
f.write(s)
f.writelines(lines) # a list of str         

