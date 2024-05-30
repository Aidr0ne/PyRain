import zlib
import sys
import Grabber

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
            
    def Determine_if_even(self, ls: list) -> int:  # Returns 2 int's divs and amm
        divs = 1
        amm = float(len(ls))
        if (amm % 2) != 0:  # Checking id ls has an even number of items
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
    
    def Compress(self, To_encypt: str, prep: dict, divs: int) -> list:
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
            
    
    def Main(self, To: str, file: str) -> None:
        
        ls = self.Find_New_Words(To)
        divs, amm = self.Determine_if_even(ls)
        divs = self.Determine_Length(divs, amm)
        prep = self.Determine_binary_keys(ls, divs)
        encrypted = self.Compress(To, prep, divs)
        Grabber.Write_key(file, prep)
        self.Write_binary(file, encrypted)