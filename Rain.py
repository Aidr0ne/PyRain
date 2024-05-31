import sys
import Grabber
import importlib
import random
import pygame

tips = ["This is a tip =-)", "Made by aidr0ne", "Polar bears are amazing!",
        "Did you know that this was made by one person"]

Version = 0.22  # VERSION AT TIME OF DOWNLOAD
    
if __name__ == "__main__":
    
    if Grabber.Check_For_Key(".config.json"):
        try:
            data = Grabber.Read_File(".config.json")
            data = dict(data)
            args = data["arg"]  # arguments
            scripts = data["scripts"]  # scripts
            version = data["version"]  # version
            Description = data["description"]  # description
            Execute = data["execute"]
            
        except Exception as e:
            print("Config Data corrupted")
            print(f"Error notes: {e}")
            print("Goto: https://github.com/Aidr0ne/PyRain/tree/main To Restore config")
            sys.exit(1)
    else:
        print("Config file not found")
        print("Go to: https://github.com/Aidr0ne/PyRain/tree/main To Restore config")
        sys.exit(1)

    arg1 = ""
    arg2 = ""
    arg3 = ""

    dev = False
    if len(sys.argv) == 1:
        print("Entering Dev Mode")
        arg2 = input("Please enter mode: ")
        arg3 = input("Please enter filename to test on: ")
        dev = True
    else:
        arg2 = sys.argv[1]
        arg3 = sys.argv[2]
        
    if len(args) != len(scripts) and len(args) != len(Description):
        print("Config File possibly outdated or modified")
        print("Goto: https://github.com/Aidr0ne/PyRain/tree/main To Restore config")
        sys.exit(1)
    
    if (len(sys.argv) != 3 or sys.argv[1] == "-h") and dev is False:
        for i in range(len(args)):
            print(f"Usage: Rain.py {args[i]} <filename> {Description[i]}")
        print("Help: Rain.py -h")
        sys.exit(1)
        
    print(f"Rain a python compression tool V{version}")

    print(tips[random.randint(0, len(tips)-1)])

    Run = False
        
    for i in range(len(args)):
        if arg2 == args[i]:
            Run = True
            try:
                with open(arg3, "r") as file:
                    To = file.read()
            except Exception as e:
                To = ""
                possibles = [""]
                a1 = False
                for item in possibles:
                    if arg2 == item:
                        a1 = True
                    else:
                        a1 = False

                print(f"A Fatal error has occurred while trying to load {arg3}\n"
                      f"Error: {e}\n"
                      f"Is it possible to continue?: {a1}")
                if a1:
                    ask = input(f"It is possible to continue Do you want to?\n "
                                "(WARNING MAY CAUSE CRASH OR DESTROY YOUR DATA), Please enter yes or no: ")
                    if ask.lower() == "yes":
                        pass
                    else:
                        sys.exit(1)
                else:
                    sys.exit(1)

            module = importlib.import_module(scripts[i])
            cls = getattr(module, Execute[i])
            instance = cls()

            instance.Main(To, arg3)

    if not Run:
        print("Sorry the file couldn't be found please make sure you put in the file path correctly"
              " and make sure it exists")
    
