import subprocess

part_names = "part_a_", "part_b_", "part_b2_", "part_c_", "part_d_", "part_e_"

#NOTE(meawoppl) I can't get this to work 
# nominally it should override the `part` variable in the scad file
# but it doesn't seem to work and I eventally just hand jammed it in
for part_name in part_names:
    print(
        subprocess.check_output(['openscad', "FiGO.scad", "-o", "{part_name}_1.stl", "-D", "part={part_name}"])
        .decode()
    )