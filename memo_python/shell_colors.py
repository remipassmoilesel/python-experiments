'''
Created on 10 mars 2016

@author: remipassmoilesel
'''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# To use code like this, you can do something like

print bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC
      
# Source: http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python