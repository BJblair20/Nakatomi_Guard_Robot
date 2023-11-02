#By: Nathaniel Ryan
#Can you tell that Python is not my primary language


# Import the required module for text 
# to speech conversion
import pyttsx3
from gpiozero import LED
from time import sleep

engine = pyttsx3.init()
led = LED(18)
bool = True
#needs to call upon app instead
soundalarm = True

def ChangeBool(bool):
    if(bool == True):
        bool = False
    else:
        bool = True

def ResumePatrol():
    True

def MarkPersonAsAcceptable():
    True

def StopPatrol():
    True

def ApproachPerson():
    StopPatrol
    #fix with movement

#run until alarm turned off
def Alarm():
    while bool == True:    
        if(soundalarm == True):
            text = "You are Not Permitted here"
            engine.say(text)
            engine.runAndWait()

        led.on()    
        sleep(10)
        led.off()
        sleep(10)
        #pseudocode: check if the app has told it
        #to stop the alarm, then
        ChangeBool(bool)
        
    

#permit class for people who are allowed to be there, 
#inform them of such, then go back to patrolling without bothering them again
def Permit():
    text = "You are Permitted here"
    engine.say(text)
    engine.runAndWait()
    MarkPersonAsAcceptable
    ResumePatrol

    
def RequestThemToHalt():
    text = "Halt"
    engine.say(text)
    engine.runAndWait()
    #wait for update from user
    


#Push request to app user
def QueryUser():
    True
    #if yes
    
    #else



#action class for all behaviours
class ActionList:
    #initialize the class with a dictionary of actions, all set to false
    def __init__(self):

        self.acts = {'QueryUser':'false', 'Alarm':'false', 'RequestThemToHalt':'false', 'Permit':'false'}


    #add actions to action lists, not functional, should just update the relevant dictionary action
    def AddAction(self, act):
        self.acts[act] = 'true'

    #remove actions from action lists, not functional
    def RemoveAction(self, act):
        self.acts[act] = 'false'

    #run to perform actions from action list
    def PerformActions(self):
        #iterate through all acts in the dictionary and run the true ones
        for i in self.acts:
            if(self.acts[i] == True):
                self.acts.keys(i) #I dont actually think this will work but thats a problem for later

        

#Create 5 people, one for each plausible combination of actions
whiteList = ActionList()
blackList = ActionList()
greyList = ActionList()

whiteList.AddAction(Permit)
blackList.AddAction(Alarm)
Alarm
