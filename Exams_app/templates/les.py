"""import threading
import time
import random

def api(result):
    time.sleep(3)
    result["key"] = random.randint(1, 100)



def experiment():
    threads = []
    sum=0
    for x in range(5):
        k={}
        api(k)
        sum=k["key"]+sum
    print(sum)

def fn():

    threads = []
    for _ in range(5):
        result = {}
        t = threading.Thread(target=api, args=(result,))
        t.start()
        threads.append([t, result])
    thread_number = 1

    a=0
    for thread, result in threads:
        thread.join()
        print("Potok" + str(thread_number) + ' return ' + str(result['key']))
        thread_number = thread_number + 1
        a+=result["key"]
    print(a)"""

"""import unittest
def fun_2(a,b):
    c=[]
    for x in a:
        for y in b:
            if x==y:
                c.append(x)
    return c


class Tests(unittest.TestCase):
    def test_fun_2(self):
        result = fun_2([1,5,9,10],[2,8,9,4])
        self.assertTrue(result == [9])



if __name__ == '__main__':
    unittest.main()"""


"""import unittest
from unittest.mock import Mock

def fn1(a):
    return 2*a

mock_one = Mock(fn1, return_value='mock return value')

print(fn1(2))
print(mock_one(3))"""

"""import unittest
from unittest.mock import Mock

import infa
class Tests(unittest.TestCase):
    def test_buy(self):
        infa.make_information=Mock(
            return_value=False
        )
        self.assertTrue(
            infa.buy(4,5,10) == 'Error'
        )

if __name__ == '__main__':
    unittest.main()"""

"""a=[2,4,5,6]
def fn(b):
    sum=0
    for x in b:
        sum+=x
    b[0]=8

    #print(sum)
fn(a)
print(a)

x=3
def fn_2(y):
    y = 7
fn_2(x)
print(x)"""

"""ls = [4,[7,8],6] #1
_,(x,_),y = ls
print(x)
print(y)


ls = [ (3, [9, 1]), [(23,43), [5, 4]] ] #2
sum=0
for _,(x,_) in ls:
    sum+=x
print(sum)"""

"""import time
from datetime import datetime

def prost(x):
    print("Result"+str(x))
    time.sleep(1)
    k=0
    for i in range(1,x):
        if x % i == 0:
            k += 1
    if k <= 0:
        return x
    else:
        print("Not simple")


def lazy_map(fn,ls):
    for h in ls:
        y = fn(h)
        yield y

start = datetime.now()
generator = lazy_map(prost,range(1000000))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print("Program time " + str((datetime.now()-start).total_seconds())+" sec:")"""

"""import time
from datetime import datetime
def prost(x):
    print("Result:"+str(x))
    k=0
    for i in range(2,x):
        if x % i == 0:
            k += 1
    if k <= 0:
        print("Simple")
    else:
        print("Not simple")
class lazy_map:
    def __init__(self,fn,ls):
        self.fn=fn
        self.idx=0
        self.ls=ls
    def iter__(self):
        return self
    def __next__(self):
        if self.idx>len(self.ls):
            raise StopIteration()
        else:
            val = self.fn(self.ls[self.idx])
            self.idx = self.idx + 1
            return val
start=datetime.now()
iterator=lazy_map(prost,[7,4,5,6,7,13])
next(iterator)
next(iterator)
print("Program time " + str((datetime.now()-start).total_seconds())+" sec")"""


"""from functools import partial #1
def fun(a,b,c):
    sum=0
    for x in a:
        sum+=x
    return sum+b+c


fun_2=partial(fun,[4,2,5])
print(fun_2)
print(fun_2(4,2))"""



