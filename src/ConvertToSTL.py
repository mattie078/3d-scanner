import os

class MeshlabTask():

    def run():
        mlx_script_path = "default_meshing.mlx"
        input = "../temps/pointCloud.ply"
        output = "../temps/STLFILE.stl"
        os.system("xvfb-run meshlabserver -i " + input + " -o " + output + " -s " + mlx_script_path + " -om vc vn > tmp")
        print (open('tmp', 'r').read())
        os.remove('tmp')

MeshlabTask.run()
