import sys
import struct
import zlib
import Grabber

Version = 0.1 #VERSION AT TIME OF DOWNLOAD


class Compression:
    def __init__(self):
        pass
    
    def Find_New_Words(self, words: str) -> list:
        ls = []
        for letter in words:
            found = False
            found = self.Check_if_exists(ls, letter)
            if found == False:
                ls.append(letter)
        return ls
                
    def Check_if_exists(self, ls: list, letter: str) -> bool:
        for lot in ls:
            if lot == letter:
                return True
            else:
                pass
        return False
            
    def Determine_if_even(self, ls: list) -> int:   #Returns 2 int's divs and amm
        divs = 1
        amm = float(len(ls))
        if (amm % 2) != 0:   #Checking id ls has a even number of items
            divs += 1
            amm -= 1
        return divs, amm
    
    def Determine_Length(self, divs: int, amm: int) -> int:
        while True:
            if amm / 2 >= 1:
                divs += 1
                amm = amm / 2
            else:
                break
        return divs
    
    def Determine_binary_keys(self, ls: list, divs: int) -> dict:
        prep = {}
        counter = 0

        for item in ls:
            counter += 1
            bine = self.Binary_generator(counter)
            bine = self.Remove_Extra_0s(bine, divs)
            bine = int(bine)
            prep[item] = bine
        
        return prep
            
            
    def Binary_generator(self, count: int) -> str:
        table = [128, 64, 32, 16, 8, 4, 2, 1]
        bine = ""
        for i in range(8):
            if count - table[i] >= 0:
                bine += "1"
                count -= table[i]
            else:
                bine += "0"
        return bine
        
    
    def Remove_Extra_0s(self, bine: str, divs:int) -> str:
        for i in range(8 - divs):
            bine = bine[1:]
        return bine
    
    def Compress(self, To_encypt: str, prep: dict) -> list:
        Encrypted = []
        space = ""
        for i in range(divs):
            space = space + "0"
        
        space = int(space)

        for item in To_encypt:
            Encrypted.append(prep[item])
            if item == " ":
                Encrypted.append(space)
        
        return Encrypted
    
    def Write_binary(self, output_file: str, binary_data_list: list) -> None:
        
        # Convert each number to an 8-bit binary string
        binary_strings = [format(num, '08b') for num in binary_data_list]

        # Join all binary strings into a single binary string
        binary_data = ''.join(binary_strings)
        binary_data = int(binary_data, 2).to_bytes((len(binary_data) + 7) // 8, byteorder='big')
        compressed_data = zlib.compress(binary_data)
        print("Original size:", len(binary_data))
        print("Compressed size:", len(compressed_data))

        with open(output_file, "wb") as f:
            f.write(compressed_data)
    
    
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
        
            en = Compression()
            ls = en.Find_New_Words(To)
            divs, amm = en.Determine_if_even(ls)
            divs = en.Determine_Length(divs, amm)
            prep = en.Determine_binary_keys(ls, divs)
            encrypted = en.Compress(To, prep)
            en.Write_binary(sys.argv[2], encrypted)
        
        
    