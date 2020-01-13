from datetime import datetime
import os
import shutil

class SaveToSD():

    def save(self):
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
    
        src_path = dir_path + "/../temps/STLFILE.stl" # Naam van STL bestand
        dst_path = dir_path + "/media/pi" # Als het goed is komt hier de SD kaart te staan
        print(str(dst_path))
        # https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory?rq=1
        directories = []
        for (os.dirpath, os.dirnames, os.filenames) in os.walk(dir_path):
            directories.extend(os.filenames)   # Voegt namen toe aan de array
            break
	    dst_path = dst_path + str(directories[0] + datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + ".stl") # Waarschijnlijk maar 1 resultaat, moeten we testen

	print(str(dst_path))
	#shutil.copy(src_path,dst_path)

s = SaveToSD() 
s.save()
