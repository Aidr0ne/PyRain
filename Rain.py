import sys
import Grabber
import importlib
import random

tips = ["This is a tip =-)", "Made by aidr0ne", "Polar bears are amazing!",
        "Did you know that this was made by one person"]

Version = 0.2  # VERSION AT TIME OF DOWNLOAD
    
if __name__ == "__main__":
    
    if Grabber.Check_For_Key(".config.json"):
        try:
            data = Grabber.Read_File(".config.json")
            data = dict(data)
            args = data["arg"]  # arguments
            scripts = data["scripts"]  # scripts
            version = data["version"]  # version
            Description = data["description"]  # description
            
        except Exception as e:
            print("Config Data corrupted")
            print(f"Error notes: {e}")
            print("Goto: https://github.com/Aidr0ne/PyRain/tree/main To Restore config")
            sys.exit(1)
    else:
        print("Config file not found")
        print("Goto: https://github.com/Aidr0ne/PyRain/tree/main To Restore config")
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

    print(tips[random.randint(0, len(tips))])

    run = False
        
    for i in range(len(args)):
        if arg2 == args[i]:
            run = True
            with open(arg3, "r") as file:
                To = file.read()
                
            module = importlib.import_module(scripts[i])
            run = module.Compression()
            fl = arg2
            run.Main(To, fl)

    if run == False:
        print("Sorry the file coudnt be found please make sure you put in the file path correctly"
              "and make sure it exists")
    
