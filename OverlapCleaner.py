import os
import itertools


class Parameters:
    def __init__(self, index, time, position, note, velocity):
        self.time = time
        self.position = position
        self.note = note
        self.index = index
        self.velocity = velocity

    def to_string(self):
        print(self.index, self.time, self.position, self.note, self.velocity)


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
        index[i] = list(index[i] for index[i], _ in itertools.groupby(index[i]))
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

    repeat = [0] * 128
    i = 0
    while i < len(data):
        if data[i].find("Note") != -1:
            params = data[i].split(", ")
            note = int(params[4])
            if params[2] == "Note_on_c" and params[5][0:-1] != 0:
                repeat[note] += 1
                if repeat[note] > 1:
                    buffer = data[i]
                    data.insert(i, buffer.replace("Note_on_c", "Note_off_c"))
                    i += 1
            else:
                data[i].replace("Note_on_c", "Note_off_c")
                if repeat[note] > 1:
                    data.pop(i)
                    i = i - 1
                    repeat[note] -= 1
                else:
                    repeat[note] -= 1
        i += 1

    # Aynı anda birden fazla on - off durumunun temizlenmesi için yazılmıştır
    # Hep ikinci olanı sildiğinden hatalıdır

    params = []

    for i in range(len(data)):
        if "Note" in data[i]:
            p = data[i].split(", ")
            params.append(Parameters(i, p[1], p[2], p[4], p[5][0:-1]))
        else:
            data[i] = 0

    same_times = reverse_same_time(params.copy())

    sts_note = reverse_same_note(same_times)

    need_delete = []

    for i in range(len(sts_note)):
        if sts_note[i][0].position == sts_note[i][-1].position:
            for k in range(len(sts_note[i]) - 1):
                need_delete.append(sts_note[i][k].index)
        else:
            if sts_note[i][-1].position == "Note_off_c":
                for k in range(len(sts_note[i]) - 1):
                    need_delete.append(sts_note[i][k].index)
            else:
                if len(sts_note[i]) > 2:
                    for k in range(1, len(sts_note[i]) - 1):
                        need_delete.append(sts_note[i][k].index)

    for i in range(len(need_delete)):
        data[int(need_delete[i])] = 0
    for i in data:
        print(i)
    data = list(filter((0).__ne__, data))

    with open("txt_inputs\\" + "TEST_" + file_name, "w") as f:
        f.writelines(data)


txt_files = os.listdir(os.getcwd() + "/txt_inputs")

for file in txt_files:
    overlap_cleaner(file)
