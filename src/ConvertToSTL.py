from xml.dom import minidom
import xml
import subprocess
import shlex

class FSMeshlabTask():

    def get_poitcloud_value_by_line(self, pointcloud_file, lookup):
        with open(pointcloud_file) as myFile:
            for num, line in enumerate(myFile, 1):
                if lookup in line:
                    number_of_pints = int(filter(str.isdigit, line))
                    return number_of_pints

    def prepare_down_sampling(self, file, pointcloud_size):

        try:
            xmldoc = minidom.parse(file)
            # itemlist = xmldoc.getElementsByTagName('filter')
            params = xmldoc.getElementsByTagName('Param')
            for param in params:
                if param.attributes['name'].value == "SampleNum":
                    param.setAttribute('value', str(int(pointcloud_size / 3)))

        except xml.parsers.expat.ExpatError as ex:
            print(ex)

        with open(file, "wb") as fh:
            xmldoc.writexml(fh)

    def run_command(command, blocking=False):

        if blocking:
            process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, _ = process.communicate()
            rc = process.returncode
        else:
            process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       shell=False)
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
            process.poll()

            rc = process.returncode

        return rc

    def run(self):
        mlx_script_path = "default_meshing.mlx"

        input = "/../temps/pointCloudTest.ply"
        output = "/../temps/STLFILE.stl"

        pointcloud_size = self.get_poitcloud_value_by_line(pointcloud_file=input, lookup="element vertex")
        self.prepare_down_sampling(mlx_script_path, pointcloud_size)

        return_code = self.run_command(
            "xvfb-run meshlabserver -i " + input + " -o " + output + " -s " + mlx_script_path + " -om vc vn")

        if return_code is 0:
            print("MESH is succesvol aangemaakt!")
        else:
            print("ERROR: MESH aanmaken mislukt.")