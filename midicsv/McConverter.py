import os
import subprocess

def convert():
    print("|-------------------------------------|")
    print("| Midi to Csv converter is working... |")
    print("|-------------------------------------|")
    os.chdir(os.getcwd())

    errfd = open("MidiToCsv_err.txt", "w+")
    midi_files = os.listdir(os.getcwd() + "\midicsv\MidiToCsv_inputs")

    for file_names in midi_files:
        print(file_names, "converted to csv")
        buf = file_names.replace(".mid", ".txt")
        buf = buf.replace(".MID", ".txt")
        outfd = open("midicsv/MidiToCsv_outputs\\csv_" + buf, "w+")
        outfd2 = open("txt_inputs/csv_" + buf,"w+")
        subprocess.call(["midicsv/midicsv", "-v", os.getcwd() + "midicsv/MidiToCsv_inputs\\" + file_names], stdout=outfd, stderr=errfd)
        subprocess.call(["midicsv/midicsv", "-v", os.getcwd() + "midicsv/MidiToCsv_inputs\\" + file_names], stdout=outfd2, stderr=errfd)
        outfd.close()

    errfd = open("CsvToMidi_err.txt", "w+")
    print(errfd.read())

    errfd.close()


# os.chdir(os.getcwd())
#
# errfd = open("MidiToCsv_err.txt", "w+")
# midi_files = os.listdir(os.getcwd()+"\MidiToCsv_inputs")
#
# for file_names in midi_files:
#     buf = file_names.replace(".mid",".txt")
#     buf = buf.replace(".MID",".txt")
#     outfd = open("MidiToCsv_outputs\\csv_" + buf, "w+")
#     subprocess.call(["midicsv", "-v", "MidiToCsv_inputs\\"+file_names], stdout=outfd, stderr=errfd)
#
# errfd = open("CsvToMidi_err.txt", "r")
# print(errfd.read())
# errfd.close()


