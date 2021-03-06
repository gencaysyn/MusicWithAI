in_file_name = "fil_out.txt"
out_file_name = "Final.txt"
with open("txt_outputs\\" + in_file_name, "r") as f:
    data = f.readlines()

final = open("note_outputs\\" + out_file_name, "w")

result = []
time = 0
noteON = "Note_on_c, 0, "
noteOFF = "Note_off_c, 0, "
repeat = []

for i in range(0, 127):
    repeat.append(0)

for note in data:
    result += note.split(" ")

final.write("0, 0, Header, 1, 2, 500\n")
final.writelines("1, 0, Start_track\n")
final.writelines("1, 0, Title_t, 'example'\n")
final.writelines("1, 0, Tempo, 500000\n")
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
    time += 500

final.writelines("2, "+str(time-500)+", End_track\n")
final.writelines("0, 0, End_of_file\n")

final.close()
