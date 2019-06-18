import os
import subprocess
from os import listdir

os.chdir(os.getcwd())

errfd = open("MidiToCsv_err.txt", "w+")
#outfd = open("MidiToCsv_outputs\\raw_" + "out.txt", "w+")
# subprocess.call(["midicsv", "-v", nmid+".mid"], stdout=outfd, stderr=errfd)
midi_files = os.listdir(os.getcwd()+"\MidiToCsv_inputs")

for file_names in midi_files:
    buf = file_names.replace(".mid",".txt")
    buf = buf.replace(".MID",".txt")
    outfd = open("MidiToCsv_outputs\\csv_" + buf, "w+")
    subprocess.call(["midicsv", "-v", "MidiToCsv_inputs\\"+file_names], stdout=outfd, stderr=errfd)

errfd = open("CsvToMidi_err.txt", "r")
print(errfd.read())
outfd.close()
errfd.close()
