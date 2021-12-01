import json
import os
import sys
import codecs



ScriptName = "SQLUserLogging"
Website = ""
Description = "This listens to all messages sent into chat and drops them into a file."
Creator = "Davasorus"
Version = "1.0.0"


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
    
    
    ##Sub = Parent.HasPermission(data.User,"Subscriber"," ")

    Parsed = data.RawData.split(';')

    ##send_message(str(Parsed))
    ##send_message('raw parse ' + str(Parsed[1][-1:]))
    ##send_message('raw parse ' + str(Parsed[1][-2:]))
    ##send_message('raw parse ' + str(Parsed[1][-3:]))
    ##send_message('raw parse ' + str(Parsed[1][-4:]))
    ##send_message('raw parse ' + str(Parsed[1][-5:]))
    ##send_message('raw parse ' + str(Parsed[1][-6:]))
    ##send_message(str(Parsed[1]))
    
    if 'mod=1' in Parsed: 
        mod = 'True'
    else: 
        mod = "False"

    if 'Subscriber=1' in Parsed: 
        sub = 'True'
        subtime = Parsed[0][-2:]
    else:
        sub = 'False'
        subtime = 0

    if 'founder/' in Parsed[0]:
        sub = 'True'
        subtime = Parsed[0][-2:]
        founder = 'True'
    else:
        sub = 'False'
        subtime = 0
        founder = 'False'


    if 'vip/1' in Parsed[1]:
        vip = 'True'
    else:
        vip = 'False'

    if 'bits/' in Parsed[1]:
        bits = 'True'
        if Parsed[1][-1:].isnumeric():
            bitnumber = Parsed[1][-1:]
        elif Parsed[1][-2:].isnumeric():
            bitnumber = Parsed[1][-2:]
        elif Parsed[1][-3:].isnumeric():
            bitnumber = Parsed[1][-3:]
        elif Parsed[1][-4:].isnumeric():
            bitnumber = Parsed[1][-4:]
        elif Parsed[1][-5:].isnumeric():
            bitnumber = Parsed[1][-5:]
        elif Parsed[1][-6:].isnumeric():
            bitnumber = Parsed[1][-6:]
            
    else:             
        bits = 'False'
        bitnumber = 0

    log("Entering Execute")

    Name = data.UserName

    Message = data.Message +'\n'
    Name = Name + '\n'
    Sub = sub + '\n'
    Mod = mod + '\n'
    Subtime = str(subtime) + '\n'
    vipStatus = vip + '\n'
    bit = bits + '\n'
    bitnumbers = str(bitnumber) + '\n'


    
    FName = str(number()) + ".txt"
    
    f = open(Location + FName , "w")
    f.write("UM: " + Message)
    f.write("UN: " + Name)
    f.write("IM: " + Mod)
    f.write("IS: " + Sub)
    f.write("SL: " + Subtime)
    f.write("VP: " + vipStatus)
    f.write("Bt: " + bit)
    f.write("BN: " + bitnumbers)
    f.write('fN: ' + founder)
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


def search_elements(searcher, searchie):
    retrieved_elements = list(filter(lambda x: searcher in x, searchie))
    return



