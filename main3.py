
def func(dct, ocher, num, ocher1):
    lng = len(ocher1)
    for i in dct[num]:
        if i not in ocher1 and i not in ocher:
            ocher1 += [i]
            break
    if len(ocher1) - lng == 1:
        func(dct, ocher, ocher1[-1], ocher1)
    return ocher1


string, numM = input().split(']],')


# print(string[3::])
spis = string[3::].split('], [')
# print(spis)
Data = []
for item in spis:
    Data += [[int(ch) for ch in item.split(', ')]]
# print(Data)
dct = dict()
i = -1
for item in Data:
    i += 1
    dct[i] = []
    for key in range(len(item)):

        if item[key] == 1 and key != i:
            dct[i] += [key]
ocher = []
# for key in dct:
#     print(key, dct[key])
for ch in range(len(dct)):
    if ch not in ocher:
        ocher1 = [ch]
        ocher += func(dct, ocher, ch, ocher1)

print(ocher, len(ocher), len(dct))


    # if ch == 0:
    #     ocher += [key]
    #     if len(dct[0] != 0):
    #         ocher += dct[ch][0]
    #     continue
    # if ch not in ocher:
    #     ocher += [ch]
    #     if len(dct[ch] != 0):
    #         ocher += dct[ch]
    #
    #
    #     for key in range(ch + 1, len(dct)):
    #         pass




# print(dct)
# print(numM[:-1])
numM = int(numM[:-1])
print(numM)
