def txt_filter(file_name):
    counter = 0
    with open("txt_inputs\\" + file_name, "r") as f:
        data = f.readlines()
        result = ""
        i = 0
        while i < len(data):
            if data[i].find("Start_track") != -1:
                while i < len(data):
                    if data[i].find("Program_c") != -1:
                        if int(data[i].split(", ")[4]) < 8:
                            while data[i].find("End_track") == -1:
                                if data[i].find("Note") != -1:
                                    if data[i - 1].find("Note") != -1:
                                        previous = int(data[i - 1].split(", ")[1])
                                    else:
                                        previous = -1
                                    if int(data[i].split(", ")[1]) == int(previous):
                                        result += chr(int(data[i].split(", ")[4]))
                                    else:
                                        result += " " + chr(int(data[i].split(", ")[4]))
                                    counter = counter + 1
                                i = i + 1
                    i = i + 1
            i = i + 1
    result = result[1:-1]
    print(result)
    with open("txt_outputs\\fil_" + file_name, "w") as of:
        of.write(result)


txt_filter("out.txt")
