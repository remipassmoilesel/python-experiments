#!/usr/bin/python2.7
# encoding: utf-8

import datetime
import re
import command
from threading import Thread

class TimedTask(Thread):
    """
    Tache éxécutée sur une echelle temporelle 
    """
    def __init__(self, timeExec=None, listCommands=None, plusTime=None, intervalExec=None):
        self.listCommands = listCommands
        
        if timeExec != None:
            self.setTimeExec(timeExec)
        
        if plusTime != None:
            self.setPlusTimeExec(plusTime)
            
        if intervalExec != None:
            self.setIntervalExec(intervalExec)
            
    def setIntervalExec(self, intervalExec):
        """
        Définir un interval en minutes entre les éxécutions. 
        """
        self.intervalExec = intervalExec

        now = datetime.datetime.now()
        self.timeExec = now + datetime.timedelta(minutes=intervalExec)

    def setTimeExec(self, timeExec):
        """
        Définir l'heure de démarrage de la tâche au format HH:MM
        """
        
        m = re.search('^([0-9]{1,2}):([0-9]{1,2})$', timeExec.strip())
        
        if m == None:
            raise Exception("Illegal format: " + timeExec)
        
        now = datetime.datetime.now()
        self.timeExec = now.replace(hour=int(m.group(1)), minute=int(m.group(2)))

    def setPlusTimeExec(self, plusTime):
        """
        Définir l'heure de démarrage de la tâche au format +MM
        """
        
        m = re.search('^(\+|-)([0-9]+)$', plusTime.strip())
        
        if m == None:
            raise Exception("Illegal format: " + plusTime)

        # la somme en minute a ajouter ou retirer
        diff = int(m.group(2)) if m.group(1) == "+" else -int(m.group(2)) 

        self.timeExec = datetime.datetime.now() + datetime.timedelta(minutes=diff)
            
    def setCommands(self, listCommands):
        self.listCommands = listCommands

    def getTimeExec(self):
        return self.timeExec
    
    def getIntervalExec(self):
        return self.intervalExec

    def refreshIntervalExec(self):
        if self.intervalExec != None:
            self.setIntervalExec(self.intervalExec)
    
    def isItTimeToRun(self):
        timeToRun = self.timeExec < datetime.datetime.now()
        self.refreshIntervalExec()
        return timeToRun
    
    def run(self):
        command.C().executeAll(self.listCommands)
    
    
class TimedTaskManager(Thread):
    """
    Gérer les tâches temporelles et les lancer au moment auportun
    """
    def __init__(self):
        self.taskList = []
    
    def run(self):
        # ....
        print "run"
    
    def createNewTask(self, timeExec):
        """
        Créer une tâche et la référencer dans le gestionnaire
        """
        task = TimedTask(timeExec)
        self.registerTask(task)
        return task
        
    def registerTask(self, task):
        """
        Référencer une tache
        """
        self.taskList.append(task)
        
        
class ProcessMonitoring(TimedTask):
    
    def __init__(self, processId):
        self.processId = processId


if __name__ == "__main__":
    
    tt = TimedTask(plusTime="+10")
    
    print tt.getTimeExec()
    
    tt.setTimeExec("12:10")
    
    print tt.getTimeExec()
    
    print tt.isItTimeToRun()
    
