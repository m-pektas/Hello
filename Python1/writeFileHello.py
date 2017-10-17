import json

def writeFileHello():
    merhaba = {
    "TURKEY"  : "Merhaba :)",
    "ENGLAND" : "Hello",
    "GERMANY" : "Hallo",
    "SPAİN"   : "Hola",
    "FRANCE"  : "Bonjour",
    }

    f = open("HelloDB.txt","w")
    f.write(json.dumps(merhaba))
    f.close()

writeFileHello()




