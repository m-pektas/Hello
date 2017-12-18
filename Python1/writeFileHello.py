import json

fileName="HelloDB.txt"
def writeFileHello():
    merhaba = {
    "TURKEY"  : "Merhaba :)",
    "ENGLAND" : "Hello",
    "GERMANY" : "Hallo",
    "SPAİN"   : "Hola",
    "FRANCE"  : "Bonjour",
    }

    f = open(fileName,"w")
    f.write(json.dumps(merhaba))
    f.close()

writeFileHello()




