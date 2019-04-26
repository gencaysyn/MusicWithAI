import os


def overlap_cleaner(file_name):
    with open("txt_inputs\\" + file_name, "r") as f:
        data = f.readlines()
    repeat = [0] * 128
    params = []
    tracks = []
    print(data)
    for i in range(len(data)):
        if data[i].find("Note") != -1:
            params = data[i].split(", ")
            print(params)
            if params[2] == "Note_off_c" or params[5][0:-1] == 0:

            if repeat[int(params[4])] > 0:
                data.insert(i,)

txt_files = os.listdir(os.getcwd() + "/txt_inputs")

for file in txt_files:
    overlap_cleaner(file)
