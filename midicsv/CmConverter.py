import os
import subprocess


def convert():
    print("|-------------------------------------|")
    print("| Cvs to Midi converter is working... |")
    print("|-------------------------------------|")
    os.chdir(os.getcwd())

    errfd = open("CsvToMidi_err.txt", "w+")
    midi_files = os.listdir(os.getcwd() + "\midicsv\CsvToMidi_inputs")

    for file_names in midi_files:
        print(file_names,"converted to midi.")
        outfd = open(os.getcwd() + "/midicsv/CsvToMidi_outputs\\mid_" + file_names.replace(".txt", ".mid"), "w+")
        subprocess.call([os.getcwd() + "/midicsv/csvmidi", "-v", "CsvToMidi_inputs\\" + file_names], stdout=outfd, stderr=errfd)
        outfd.close()

    errfd = open("CsvToMidi_err.txt", "w+")
    print(errfd.read())
    errfd.close()


# os.chdir(os.getcwd())
#
# errfd = open("CsvToMidi_err.txt", "w+")
# midi_files = os.listdir(os.getcwd() + "\midicsv\CsvToMidi_inputs")
#
# for file_names in midi_files:
#     outfd = open("midicsv\midicsvCsvToMidi_outputs\\mid_" + file_names.replace(".txt", ".mid"), "w+")
#     subprocess.call(["csvmidi", "-v", "CsvToMidi_inputs\\" + file_names], stdout=outfd, stderr=errfd)
#     outfd.close()
#
# errfd = open("CsvToMidi_err.txt", "r")
# print(errfd.read())
# errfd.close()
