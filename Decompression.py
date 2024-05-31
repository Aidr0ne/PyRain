import Grabber
import zlib
class Decompression:
    def __init__(self):
        pass

    def identify_files(self, name: str) -> dict:
        if not Grabber.Check_For_Key(name):
            print("Error files needed for decompression have not been Found")
            print(f"Target File Found?: {Grabber.Check_For_Key(name)}")
            print(f"Target Data File Found?: {Grabber.Check_For_Key(Grabber.add_json(name))}")
        else:
            data = Grabber.read_binary(name)
            prep = Grabber.Read_File(Grabber.add_json(name))
            prep = dict(prep)
            return prep, data

    def decompress_basic(self, data):
        de_data = zlib.decompress(data)
        return de_data

    def decompress_custom(self, binary_data: str, prep: dict):
        divs = prep["divs"]
        wrd = ""
        for l in range(int(len(binary_data) / divs)):
            cn = ""
            for i in range(divs):
                cn + str(binary_data[i])

            print(cn)


    def Main(self, o: str, file: str):  # DO NOT TOUCH o
        prep, data = self.identify_files(file)
        dis = self.decompress_custom(data, prep)
        print(dis)  # TODO: FIX DECOMPRESSION SOFTWARE
