from datetime import datetime
import os
import shutil


class SaveToSD():

    def save(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        src_path = dir_path + "/../temps/STLFILE.stl"  # Naam van STL bestand
        # Als het goed is komt hier de SD kaart te staan
        dst_path = "/media/pi/9016-4EF8/"
        # Waarschijnlijk maar 1 resultaat, moeten we testen
        dst_path = dst_path + datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + ".stl"
        shutil.copy(src_path, dst_path)
