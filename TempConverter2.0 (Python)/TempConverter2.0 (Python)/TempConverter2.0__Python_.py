import sys

def main():
    menu()

def menu():
    print("What Converter do you want?")
    print()

    Userchoice = input("""
                             A: Celsuis To Farenheight 
                             B: Farenheight To Celsuis
                             C: Celsuis To Kelvin
                             D: Farenheight to Kelvin
                             E: Kelvin to Farenheight
                             F: Kelvin to celsuis
                             G: Exit the program
                             
                             Please choose an option: """)

    if Userchoice == "A" or Userchoice == "a":
        Celsu()
    elif Userchoice == "B" or Userchoice == "b":
        Farenh()
    elif Userchoice == "C" or Userchoice == "c":
        CeltoKel()
    elif Userchoice == "D" or Userchoice == "d":
        faToKel()
    elif Userchoice == "E" or Userchoice == "e":
        keltofar()
    elif Userchoice == "F" or Userchoice == "f":
        Keltocel()
    elif Userchoice == "G" or Userchoice == "g":
        sys.exit

    else:
        print()
        print("You must select an option")
        print("Please try again")
        print()
        menu()











def Celsu():
    print("Temperature Converter")
    print("Enter celsuis:")
    
    celsuisString = input()
    celsuis = float(celsuisString)
    faren = float(celsuis * 1.8 + 32)
    farenString = str(faren)
    print("Farenheigh: " + farenString + "°F")

    print()
    menu()

def Farenh():
    print("Temperature Converter")
    print("Enter Farenheigh:")

    farenString = input()
    faren = float(farenString)
    cels = float(faren - 32 * 5 / 9)
    celsString = str(cels)
    print("Celsuis: " + celsString + "°C")

    print()
    menu()

def CeltoKel():
    print("Temperature Converter")
    print("Enter celsuis:")

    celsuisString = input()
    celsuis = float(celsuisString)
    kel = float(celsuis + 273.15)
    kelString = str(kel)
    print("Kelvin: " + kelString + "K")

    print()
    menu()
    
def faToKel():
    print("Temperature Converter")
    print("Enter Farenheight:")

    farenString = input()
    faren = float(farenString)
    kelv = float(faren + 459.67 / 1.8)
    kelvString = str(kelv)
    print("Kelvin: " + kelvString + "K")

    print()
    menu()

def keltofar():
    print("Temperature Converter")
    print("Enter Kelvin:")

    KelvString = input()
    kelv = float(KelvString)
    farh = float(kelv - 273.15 * 1.8000 + 32.00)
    farhString = str(farh)
    print("Farenheight: " + farh + "°F")

    print()
    menu()

def Keltocel():
    print("Temperature Converter")
    print("Enter Kelvin:")

    kelvString = input()
    kelv = float(kelvString)
    cel = float(kelv - 273.15)
    celString = str(cel)
    print("celsuis: " + celString + "°C")

    print()
    menu()


main()



    





















