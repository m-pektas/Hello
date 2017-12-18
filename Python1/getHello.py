import json

fileName="HelloDB.txt"
def getHello(country):
    f = open(fileName,"r")
    dictionary = json.loads(f.read())
    try:
        return dictionary[country.upper()]
    except:
        return "I don't know What you say hello in your native language.\n\n\t But"