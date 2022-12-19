import os
from pathlib import Path
import subprocess

#This will run all the mx3 files in a given directory
#mumax directory 
#mx3 file directory
mx3_dir = Path.cwd() / "DMI_DW"

#Get all the files
files = mx3_dir.glob("*.mx3")

os.chdir("/Users/{NAME OF USER}/Desktop/mumax3.10_windows_cuda11.0/DMI_DW")
#Run all the files

for current_file in files:
    filename = current_file.name
    subprocess.run(f"mumax3 {filename}") 
    #orgainlly format = test_Dind=-1.11e-04.mx3
    outfilename = filename.replace("mx3", "out")
    # os.chdir(f"/Users/Wayne&May/Desktop/mumax3.10_windows_cuda11.0/DMI_DW/{outfilename}")
    # subprocess.run("mumax3-convert.exe -arrows 10 -jpg *.ovf")
    # os.chdir("/Users/Wayne&May/Desktop/mumax3.10_windows_cuda11.0/DMI_DW")
