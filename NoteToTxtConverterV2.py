import os
import subprocess

def noteToTxtConverter(in_file_name,out_file_name):
    with open(in_file_name, "r") as f:
        data = f.read()

    final = open(out_file_name, "w")

    result = []
    time = 0
    noteON = "Note_on_c, 0, "
    noteOFF = "Note_off_c, 0, "
    repeat = []

    for i in range(0, 127):
        repeat.append(0)

    for note in data:
        result += note.split(" ")
    print(result)
    final.write("0, 0, Header, 1, 2, 1024\n")
    final.writelines("1, 0, Start_track\n")
    final.writelines("1, 0, Title_t, 'example'\n")
    final.writelines("1, 0, Tempo, 250000\n")
    final.writelines("1, 0, Time_signature, 4, 2, 24, 8\n")
    final.writelines("1, 0, End_track\n")
    final.writelines("2, 0, Start_track\n")
    final.writelines("2, 0, Title_t, 'Instrument Track 01'\n")
    final.writelines("2, 0, Program_c, 6, 6\n")

    for word in result:
        for char in word:
            note = ord(char)
            if repeat[note] == 0:
                print("2, " + str(time) + ", " + noteON + str(note) + ", 100")
                final.writelines("2, " + str(time) + ", " + noteON + str(note) + ", 100\n")
                repeat[note] = 1
            else:
                print("2, " + str(time) + ", " + noteOFF + str(note) + ", 64")
                final.writelines("2, " + str(time) + ", " + noteOFF + str(note) + ", 64\n")
                repeat[note] = 0
        time += 1024

    final.writelines("2, "+str(time-500)+", End_track\n")
    final.writelines("0, 0, End_of_file\n")

    final.close()

note_files = os.listdir(os.getcwd()+"/txt_outputs")

for file_names in note_files:
    noteToTxtConverter("note_inputs/"+file_names,"note_outputs/noteToTxt_"+file_names)

