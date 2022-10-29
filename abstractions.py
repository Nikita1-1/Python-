
from abc import ABC, abstractmethod

class Wine(ABC):#parent class that takes argumetns from library
    def kind(self, sort):#creating method and passing selfs 
        print('You choose', sort, 'wine')
        @abstractmethod
        def producer(self, sort):#this methiod will be created in WineProducer class
            pass

class WineProducer(Wine):
    def producer(self, sort):
        print('You choose red wine, grape {}'.format(sort))

w = WineProducer()
w.kind('Sangiovese')
w.producer('Sangiovese')
