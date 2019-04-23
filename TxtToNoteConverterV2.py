import os
import subprocess

def max_val(channels):
    maxval = 0
    for i in range(len(channels)):
        if maxval < int(channels[i][-1][1]):
            maxval = int(channels[i][-1][1]) + 1
    return maxval


def txt_filter(file_name):
    counter = 0
    with open("txt_inputs\\" + file_name, "r") as f:
        data = f.readlines()
        i = 0
        j = 0
        resolution = round(int(data[i].split(", ")[5]) / 8)
        tracks = []
        channels = []
        while i < len(data):
            if data[i].find("Start_track") != -1:
                while data[i].find("End_track") == -1:
                    if data[i].find("Note") != -1:
                        params = data[i].split(", ")
                        params[5] = params[5][0:-1]
                        params[1] = str(round(int(params[1]) / resolution))
                        tracks.append(params)
                    i = i + 1
                channels.append(tracks)
            i = i + 1
        max_time = max_val(channels)
        result = []
        for i in range(0, max_time):
            result.append(" ")
        for i in range(0, len(channels)):
            for j in range(0, len(channels[i])):
                params = channels[i][j]
                if result[int(params[1])].find(chr(int(params[4]))) == -1:
                    result[int(params[1])] = result[int(params[1])].strip()
                    result[int(params[1])] += chr(int(params[4]))

        i = 0
        out = ""
        for i in range(len(result)):
            out += result[i]+" "
    with open("txt_outputs\\note_" + file_name, "w") as of:
        of.write(out)
    print(result)


txt_files = os.listdir(os.getcwd() + "/txt_inputs")

for file in txt_files:
    txt_filter(file)
