"""
a=-5.64
>>> abs(a)
5.64

(5).__add__(7)
12

>>> num=10
>>> num + 5
15
>>> num.__add__(5)
15
"""
#new init
class Aditya:
    def __new__(obj):
        print("calling __new__ magic method ")
        res=object.__new__(obj)
        return res
    def __init__(self):
        print("__int__ method is called")
        self.name='Harsha'
clg=Aditya()
