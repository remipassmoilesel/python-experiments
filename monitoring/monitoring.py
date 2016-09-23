#!/usr/bin/python2.7
# encoding: utf-8

from timedtasks import TimedTask
from timedtasks import TimedTaskManager

if __name__ == "__main__":
    
    # redémarrer le serveur une fois par jour ?
    # surveiller un processus: SSH ? Apache ? ...
    
    tt = TimedTask(plusTime="+10")
    
    print tt.getTimeExec()
    
    tt.setTimeExec("12:10")
    
    print tt.getTimeExec()
    
    print tt.isItTimeToRun()