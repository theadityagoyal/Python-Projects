#abstract class works like an interface
from abc import *
class Myclass(ABC):
    def connect(self):
        pass
    def disconnect(self):
        pass

class Oracle(Myclass):
    def connect(self):
        print('connecting to oracle database...')
    def disconnect(self):
        print('disconnected from oracle...')

class Sybase(Myclass):
    def connect(self):
        print('connecting to sybase database...')
    def disconnect(self):
        print('disconnected from sybase')

class Database:
    str=input('Enter database name:')

    classname1= globals()[str]
    
    x=classname1()
    
    x.connect()
    x.disconnect()
    
