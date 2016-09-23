'''
Created on Mar 30, 2016

@author: remipassmoilesel
'''
class Iterable:
    def __init__(self, value, *sons):
        self.value = value 
        self.childs = sons
    
    def next(self):
        self.iterIndex += 1
        if self.iterIndex < len(self.childs):
            return self.childs[self.iterIndex]
        else:
            raise StopIteration
        
    def __iter__(self):
        self.iterIndex = -1;
        return self