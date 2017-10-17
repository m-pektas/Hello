import getHello
import os                   # os added for cls comment


while True :
    country = input("What is your country ? \n\n\t: ")
    print("\n\n\t",getHello.getHello(country),", Welcome my Hello Project :)")
    exit = input("\n\n if do you want exit enter 1, please..")
    if(exit == '1'):
        break
    os.system("cls")
