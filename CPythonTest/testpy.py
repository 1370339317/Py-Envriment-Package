#coding:utf-8
'''
create on 2017-04-20
@author:sandy
'''
def Hello(s):
    print ("Hello World")
    print(s)
    return s

def Imphash(s):
    return pefile.PE(s).get_imphash()

 
class Person(object):
 
    def __init__(self):
        self.name = "mandy"
        self.age = 20
 
    def setInfo(self,name,age):
        print(self,dir(self),name)
        self.name = name
        self.age = age
 
    def getInfo(self):
        print('python: name={}, age={}'.format(self.name, self.age))
        return self.name, self.age
 
    def sayHello(self, name):
        print(self,dir(self),name)
        # self.name = "sssss"
        print ("Hello,", name)
        return name