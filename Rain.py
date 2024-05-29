import sys
import struct
import zlib
import Grabber
import importlib

Version = 0.2 #VERSION AT TIME OF DOWNLOAD
    
if __name__ == "__main__":
    
    if Grabber.Check_For_Key(".config.json"):
        try:
            data = Grabber.Read_File(".config.json")
            data = dict(data)
            args = data["arg"] # arguments
            scripts = data["scripts"] # scripts
            version = data["version"] # version
            Description = data["description"] # description
            
        except Exception as e:
            print("Config Data corupted")
            print(f"Error notes: {e}")
            print("Goto: https://github.com/Aidr0ne/PyRain/tree/main To Restore config")
            sys.exit(1)
    else:
        print("Config file not found")
        print("Goto: https://github.com/Aidr0ne/PyRain/tree/main To Restore config")
        sys.exit(1)
        
    if len(args) != len(scripts) and len(args) != len(Description):
        print("Config File possibly outdated or modified")
        print("Goto: https://github.com/Aidr0ne/PyRain/tree/main To Restore config")
        sys.exit(1)
    
    if len(sys.argv) != 3:
        for i in range(len(args)):
            print(f"Usage: Rain.py {args[i]} <filename> {Description[i]}")
        print("Help: Rain.py -h")
        sys.exit(1)
        
    print(f"Rain a python compression tool V{version}")
        
    for i in range(len(args)):
        if sys.argv[1] == args[i]:
            with open(sys.argv[2], "r") as file:
                To = file.read()
                
            module = importlib.import_module(scripts[i])
            run = module.Compression()
            fl = sys.argv[2]
            run.Main(To, fl)
        
    
