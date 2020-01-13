import open3d as o3d
import trimesh
import numpy as np

def ConvertToSTL():
    pointcloud = o3d.io.read_point_cloud("temps\pointCloudTest.ply")
    pointcloud.estimate_normals()

    # estimate radius voor de rolling ball
    distances = pcd.compute_nearest_neighbor_distance()
    avg_dist = np.mean(distances)
    radius = 1.5 * avg_dist

    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
                pcd, o3d.utility.DoubleVector([radius, radius*2]))

    output = trimesh.Trimesh(np.asarray(mesh.vertices), np.asarray(mesh.triangles),
                vertex_normals=np.asarray(mesh.vertex_normals))

    output.export('eindresultaat.stl')


ConvertToSTL()
