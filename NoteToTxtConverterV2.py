import os
import subprocess


def noteToTxtConverter(in_file_name, out_file_name):
    with open(in_file_name, "r") as f:
        data = f.read()

    final = open(out_file_name, "w")

    result = []
    noteON = "Note_on_c, 0, "
    noteOFF = "Note_off_c, 0, "
    # for note in data:
    #   result += note.split(" ")
    result = []
    i = 0
    while i < len(data):
        if data[i] == " ":
            result.append(" ")
        else:
            j = i
            result.append("")
            while data[j] != " ":
                result[-1] += data[j]
                j += 1
                i = j-1
        i += 1
    print(data)
    print(result)
    resolution = 512
    final.write("0, 0, Header, 1, 2, " + str(resolution) + "\n")
    final.writelines("1, 0, Start_track\n")
    final.writelines("1, 0, Title_t, 'example'\n")
    final.writelines("1, 0, Tempo, 413793\n")
    final.writelines("1, 0, Time_signature, 4, 2, 24, 8\n")
    final.writelines("1, 0, End_track\n")
    final.writelines("2, 0, Start_track\n")
    final.writelines("2, 0, Title_t, 'Instrument Track 01'\n")
    final.writelines("2, 0, Program_c, 6, 6\n")

    repeat = [0]*128
    i = 0
    time = -(resolution // 16)
    while i < len(result):
        if result[i] != " ":
            time += (resolution // 16)
            j = 0
            while j < len(result[i]):
                note = ord(result[i][j])
                if result[i].count(chr(note)) < 2:
                    if repeat[note] == 0:
                        print("2, " + str(time) + ", " + noteON + str(note) + ", 100")
                        final.writelines("2, " + str(time) + ", " + noteON + str(note) + ", 100\n")
                        repeat[note] = 1
                    else:
                        print("2, " + str(time) + ", " + noteOFF + str(note) + ", 64")
                        final.writelines("2, " + str(time) + ", " + noteOFF + str(note) + ", 64\n")
                        repeat[note] = 0
                else:
                    if repeat[note] == 0:
                        print("2, " + str(time) + ", " + noteOFF + str(note) + ", 100")
                        final.writelines("2, " + str(time) + ", " + noteOFF + str(note) + ", 100\n")
                        repeat[note] = 1
                    else:
                        print("2, " + str(time) + ", " + noteON + str(note) + ", 64")
                        final.writelines("2, " + str(time) + ", " + noteON + str(note) + ", 64\n")
                        repeat[note] = 0

                j += 1
        else:
            time += (resolution // 16)
        i += 1

    final.writelines("2, " + str(time) + ", End_track\n")
    final.writelines("0, 0, End_of_file\n")
    final.close()


note_files = os.listdir(os.getcwd() + "/note_inputs")

for file_names in note_files:
    noteToTxtConverter("note_inputs/" + file_names, "note_outputs/noteToTxt_" + file_names)
