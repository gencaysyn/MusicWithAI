import os
import subprocess


def max_val(channels):
    maxval = 0
    for i in range(len(channels)):
        if maxval < int(channels[i][1]):
            maxval = int(channels[i][1]) + 1
    return maxval


def txt_filter(file_name):
    counter = 0
    with open("txt_inputs\\" + file_name, "r") as f:
        data = f.readlines()
        i = 0
        j = 0
        resolution = round(int(data[i].split(", ")[5]) / 8)
        tracks = []
        while i < len(data):
            if data[i].find("Start_track") != -1:
                while data[i].find("End_track") == -1:
                    if data[i].find("Note") != -1:
                        params = data[i].split(", ")
                        params[5] = params[5][0:-1]
                        params[1] = str(round(int(params[1]) / resolution))  # time
                        tracks.append(params)
                    i = i + 1
            i = i + 1
        max_time = max_val(tracks)
        result = []
        for i in range(max_time):
            result.append(" ")

        for row in tracks:
            params = row
            if result[int(params[1])].count(params[4]) < 3:
                result[int(params[1])] = result[int(params[1])].strip()
                result[int(params[1])] += chr(int(params[4]))

        out = ""
        for i in range(len(result)):
            out += result[i] + " "
        print(out)
    with open("txt_outputs\\note_" + file_name, "w") as of:
        of.write(out)


txt_files = os.listdir(os.getcwd() + "/txt_inputs")

for file in txt_files:
    txt_filter(file)
