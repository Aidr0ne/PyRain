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
            data = Grabber.Read_File(name)
            prep = dict(Grabber.Read_File(Grabber.add_json(name)))
            return prep, data

    def decompress_basic(self, data):
        de_data = zlib.decompress(data)
