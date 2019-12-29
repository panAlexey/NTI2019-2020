
def func(dct, ocher, num, ocher1):
    lng = len(ocher1)
    for i in dct[num]:
        if i not in ocher1 and i not in ocher:
            ocher1 += [i]
            break
    if len(ocher1) - lng == 1:
        func(dct, ocher, ocher1[-1], ocher1)
    return ocher1


def func2(dct, ocher, num, ocher1):
    pass


def funcEnumarationQueue(ocher3, dct):
    ocher3end = [ocher3.pop(0)]
    # print('--------', ocher3end, ocher3)

    for ch in range(len(ocher3)):
        # print(dct[ocher3end[-1]])
        lng = len(ocher3end)
        for chi in range(len(dct[ocher3end[-1]])):
            if dct[ocher3end[-1]][chi] in ocher3:
                other = dct[ocher3end[-1]][chi]
                ocher3end.append(other)
                ocher3.remove(other)
                # print(ocher3, ocher3end)
                break
        if len(ocher3) != 0 and len(ocher3end) - lng > 0:
            ocher3end.append(ocher3.pop(0))
    return ocher3end

def funcCNT(superOcher, numM):
    cnt = 0
    for j in range(len(superOcher)):
        if len(superOcher[j]) <= numM:
            cnt += 1
            continue
        ost = len(superOcher[j]) % numM
        cnt += len(superOcher[j]) // numM
        if ost != 0:
            cnt += 1
    return cnt

def funcTakeQueue(ocher, dct):
    for ch in range(len(dct)):
        if ch not in ocher:
            ocher1 = [ch]
            ocher += func(dct, ocher, ch, ocher1)
    return ocher

def funcFormOcher(ocher, superOcher, dct):
    prev = 0
    for i in range(len(ocher) - 1):
        if ocher[i + 1] not in dct[ocher[i]]:
            superOcher.append(ocher[prev:i + 1])
            prev = i + 1
    if prev <= i + 1:
        superOcher.append(ocher[prev:])
    return superOcher


string, numM = input().split(']],')

numM = int(numM[:-1])
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
#      print(key, dct[key])
cntM = []
while True:
    ocher = funcTakeQueue(ocher, dct)

    # print(ocher, len(ocher), len(dct))
    superOcher = []
    superOcher = funcFormOcher(ocher, superOcher, dct)
    # print(superOcher)

    superOcher2 = []
    superOcher3 = []
    for ocher in superOcher:
        if len(ocher) % numM != 0:
            superOcher3.append(ocher)
        else:
            superOcher2.append(ocher)

    ocher3 = []
    for och in superOcher3[::-1]:
        ocher3.extend(och[::-1])
    # print(ocher3)

    ocher3end = funcEnumarationQueue(ocher3, dct)

    superOcher3 = []
    superOcher3 = funcFormOcher(ocher3end, superOcher3, dct)
    for ch in superOcher2:
        superOcher3.append(ch)
    # print(superOcher3)

    cnt1 = funcCNT(superOcher3, numM)

    cnt = funcCNT(superOcher, numM)

    print(min(cnt, cnt1))
    cntM += [cnt]

    break



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

