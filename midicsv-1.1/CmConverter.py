import os
import subprocess
from os import listdir

os.chdir(os.getcwd())

errfd = open("CsvToMidi_err.txt", "w+")
#outfd = open("CsvToMidi_outputs\\final_" + "out.txt", "w")
# subprocess.call(["midicsv", "-v", nmid+".mid"], stdout=outfd, stderr=errfd)
midi_files = os.listdir(os.getcwd()+"\CsvToMidi_inputs")

for file_names in midi_files:
    outfd = open("CsvToMidi_outputs\\mid_" + file_names.replace(".txt",".mid"), "w+")
    subprocess.call(["csvmidi", "-v", "CsvToMidi_inputs\\"+file_names], stdout=outfd, stderr=errfd)

errfd = open("CsvToMidi_err.txt", "r")
print(errfd.read())
outfd.close()
errfd.close()
