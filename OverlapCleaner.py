import os
import itertools


class Parameters:
    def __init__(self, index, channel, time, position, note, velocity):
        self.time = time
        self.position = position
        self.note = note
        self.index = index
        self.velocity = velocity
        self.channel = channel

    def to_string(self):
        print(self.index, self.channel, self.time, self.position, self.note, self.velocity)


def reverse_same_time(params):
    same_times = [[]]
    k = 0
    loop_flag = False
    i = 0

    while i < len(params) - 1:
        j = i
        while j < len(params) - 1 and (params[j].time == params[j + 1].time):
            same_times[k].append(params[j])
            loop_flag = True
            j += 1
        if loop_flag:
            same_times[k].append(params[j])
            same_times.append([])
            i = j
            k += 1
            loop_flag = False
        else:
            i += 1
    return same_times


def indices(mylist, value):
    arr = []
    for i in mylist:
        arr.append(i.note)
    return [i for i, x in enumerate(arr) if x == value]


def reverse_same_note(same_times):
    index = []
    sts_note = []
    for i in range(len(same_times)):
        buffer = []
        for j in range(len(same_times[i])):
            buffer.append(indices(same_times[i], same_times[i][j].note))
        index.append(buffer.copy())

    for i in range(len(index)):
        index[i].sort()
        index[i] = list(index[i] for index[i], _ in itertools.groupby(index[i])).copy()
        for j in range(len(index[i])):
            row = []
            if len(index[i][j]) > 1:
                for k in range(len(index[i][j])):
                    row.append(same_times[i][int(index[i][j][k])])
                sts_note.append(row.copy())

    return sts_note


def overlap_cleaner(file_name):
    with open("txt_inputs\\" + file_name, "r") as f:
        data = f.readlines()

    data = sorted(data, key=lambda x: int(x.split(", ")[1]))
    resolution = round(int(data[0].split(", ")[5]) / 8)

    # with open("C:/Users\genca\Documents\GitHub\MusicWithAI/test/" + "SORTED_" + file_name, "w") as f:
    #     f.writelines(data)

    repeat = [0] * 128
    i = 0
    while i < len(data):
        # print(file_name, data[i])
        if data[i].find("Note_o") != -1:
            params = data[i].split(", ")
            note = int(params[4])
            if params[2] == "Note_on_c" and params[5][0:-1] != 0:
                repeat[note] += 1
                if repeat[note] > 1:
                    buffer = data[i]
                    data.insert(i, buffer.replace("Note_on_c", "Note_off_c"))
                    i += 1
            else:
                if repeat[note] > 1:
                    data.pop(i)
                    i = i - 1
                    repeat[note] -= 1
                else:
                    if repeat[note] > 0:
                        repeat[note] -= 1
        i += 1

    params = []
    for i in range(1, len(data)):
        if "Note_o" in data[i]:
            p = data[i].split(", ")
            if int(p[5][0:-1]) == 0:
                p[2] = "Note_off_c"
                data[i] = data[i].replace("Note_on_c", "Note_off_c")
            p[1] = str(int(p[1]) // resolution)
            params.append(Parameters(i, p[0], p[1], p[2], p[4], p[5][0:-1]))
        else:
            data[i] = '0'

    same_times = reverse_same_time(params.copy())
    sts_note = reverse_same_note(same_times.copy())

    # for i in sts_note:
    #     for j in i:
    #         j.to_string()
    #     print()

    need_delete = []
    for note in sts_note:
        con = 0
        coff = 0
        for j in note:
            if j.position == "Note_off_c":
                coff += 1
            else:
                con += 1
        if con > 0 and coff > 0:
            data[note[0].index] = data[note[0].index].replace("Note_on_c", "Note_off_c")
            data[note[1].index] = data[note[1].index].replace("Note_off_c", "Note_on_c")
            buf = data[note[1].index].split(", ")
            data[note[1].index] = data[note[1].index][::-1].replace(buf[5][::-1], "\n99", 1)[::-1]
            for x in range(2, len(note)):
                need_delete.append(note[x].index)
        else:
            for x in range(1, len(note)):
                need_delete.append(note[x].index)

    for i in range(len(need_delete)):
        data[int(need_delete[i])] = '0'

    data = list(filter('0'.__ne__, data))
    # for i in data:
    #     print(i,end="")

    with open("C:/Users\genca\Documents\GitHub\MusicWithAI/test/" + "TEST_" + file_name, "w") as f:
        f.writelines(data)


txt_files = os.listdir(os.getcwd() + "/txt_inputs")

print(len(txt_files), "files revealed !")
ind = 0
for file in txt_files:
    overlap_cleaner(file)
    print(ind,file, " created.")
    ind += 1

x = input("Press enter...")
