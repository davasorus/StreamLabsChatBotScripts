import json
import os
import sys
import codecs

ScriptName = "SQLUserLogging"
Website = "https://en.wikipedia.org/wiki/The_X-Files"
Description = "This listens to all messages sent into chat and drops them into a file."
Creator = "Davasorus"
Version = "2.0.0"


settings = {}
num = 0
command = "!test"

Location = "E:\\Recordings\\TwitchChatIngest\\"

def Init():
    global settings
    work_dir = os.path.dirname(__file__)
    

    try:
        with codecs.open(os.path.join(work_dir, "settings.json"), encoding='utf-8-sig') as json_file:
            settings = json.load(json_file, encoding='utf-8-sig')
    except Exception, e:
        log(str(e))
    
    return

def Execute(data):
    if (not (data.GetParam(0) != command and data.GetParam(0).strip())):
        return
    
    

    log("Entering Execute")

    
    Name = data.UserName
    Message1 = data.Message +'\n'
    Message2 = Name + '\n'
    
    FName = str(number()) + ".txt"
    
    f = open(Location + FName , "w")
    f.write(Message1)
    f.write(Message2)
    f.close()
      
    log("Leaving Execute")
    return

def Tick():
    return

def send_message(message):
    log("Entering Message")

    Parent.SendStreamMessage(message)

    log("Leaving Message")
    return

def log(message):
    Parent.Log(command,message)

    return

def number():
    global num
    num +=1
    return num