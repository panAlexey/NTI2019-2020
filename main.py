# koefPascal = [[5, 10, 10, 5, 1], [6, 15, 20, 15, 6, 1], [7, 21, 35, 35, 21, 7, 1], [8, 28, 56, 70, 56, 28, 8, 1],
#               [9, 36, 84, 126, 126, 84, 36, 9, 1], [10, 45, 120, 210, 252, 210, 120, 45, 10, 1]]

# def analisProducts(Clothes):
#     pass
#
# def analisGosha(Gosha):
#     Gosha.sort()
#     mnojestvoGosha = set()
#     print(Gosha)
#     # for ch in range(len(Gosha) - 1):
#
# def sumGosha():
#     pass


def smGosha(Gosha, cnt):
    # print('-------------------------', cnt, len(Gosha))
    if cnt == len(Gosha):
        return [sum(Gosha)]
    if cnt == 1:
        return Gosha
    k = 0
    sm2 = []
    # print('summa:', len(Gosha) - 1, Gosha)
    for i in range(len(Gosha) - 1):
         sm1 = smGosha(Gosha[i + 1:], cnt - 1)
         # print(sm1)
         for j in range(len(sm1)):
             sm1[j] += Gosha[i]
         sm2.extend(sm1)
         # print(i, cnt, '---', sm1, sm2)
    return sm2


def smProduct(Gosha, cnt, sm):
    print('-------------------------', cnt, len(Gosha))
    if cnt == len(Gosha):
        return [sum(Gosha), cnt]
    if cnt == 1:
        cntM = [1] * len(Gosha)
        print(cntM)
        print(Gosha)
        print(list(zip(Gosha, cntM)))
        return list(map(list,list(zip(Gosha, cntM))))
    k = 0
    sm2 = []
    print('----------------------summa:', len(Gosha) - 1, Gosha)
    for i in range(len(Gosha) - 1):
         sm1 = smProduct(Gosha[i + 1:], cnt - 1, sm)
         # print(sm1)
         for j in range(len(sm1)):
             sm1[j][0] += Gosha[i]
             sm1[j][1] += 1
         sm2.extend(sm1)
         print(i, cnt, '---', sm1, sm2)
    print(sm2)
    return sm2


def analisProducts(Gosha):
    # print(Gosha, len(Gosha))
    # print('Hello')
    sm = []
    for ch in range(len(Gosha)):
         # sm = []
         # lengthSM = koefPascal[len(Gosha) - 5]
         # print(ch, '---- koef Pascal: ', lengthSM)
         # for i in range(lengthSM[ch]):
         #     sm += [0] # ch + 1 - по сколько чисел суммируем
         # print(ch + 1, '****************************************************************************')
         # for cnt in range(1, len(Gosha) + 1):
         sm1 = smGosha(Gosha, ch + 1)
         sm2 = [ch + 1] * len(sm1)
         sm += list(zip(sm1, sm2))
         # print(ch + 1, '---------------------------------------------------------------->', sm, 'len = ', len(sm))


    return list(set(sm))


def analisGosha2(Gosha):
    # print(Gosha, len(Gosha))
    # print('Hello')
    sm = []
    for ch in range(len(Gosha)):
         # sm = []
         # lengthSM = koefPascal[len(Gosha) - 5]
         # print(ch, '---- koef Pascal: ', lengthSM)
         # for i in range(lengthSM[ch]):
         #     sm += [0] # ch + 1 - по сколько чисел суммируем
         # print(sm)
         # for cnt in range(1, len(Gosha) + 1):
         sm.extend(smGosha(Gosha, ch + 1))

         # print(ch + 1, '---------------------------------------------------------------->', sm, 'len = ', len(sm))
    return list(set(sm))


# def analisGosha3(prom, current, mn, num, sm):
#     if num == 1:
#         for ch in len(sm):
#             sm[ch] += prom[ch]

string = input().split('],[')
# print(string)
string[0] = string[0][1:]
string[2] = string[2][:-1]
Gosha = [int(i) for i in string[0].split(', ')]
Kassir = [int(i) for i in string[1].split(', ')]
Clothes = [int(i) for i in string[2].split(', ')]

# print(Gosha, Kassir, Clothes, sum(Gosha), sum(Kassir), sum(Clothes))
moneyKassir = analisGosha2(Kassir)
moneyKassir.sort()
moneyGosha = analisGosha2(Gosha)
moneyGosha.sort()
maxGosha = max(moneyGosha)
moneyProduct = analisProducts(Clothes)
print('money Products: ', moneyProduct)
print('moneyGosha: ', moneyGosha)
print('moneyKassir', moneyKassir)



moneyProduct = list(filter(lambda x: x[0] <= maxGosha, moneyProduct))
print('money Products: ', moneyProduct)
maxProductCnt = max(moneyProduct, key=lambda x: x[1])[1]
print("maxProductCnt", maxProductCnt)
sumGosha = 0
cntGosha = 0
for i in range((maxProductCnt), -1, -1):
    moneyProductTmp = list(filter(lambda x: x[1] == i, moneyProduct))
    print(moneyProductTmp)
    moneyProductTmp = sorted(list(map(lambda x: x[0], moneyProductTmp)))
    print(moneyProductTmp)
    for item in moneyProductTmp:
        if item in moneyGosha:
            sumGosha = item
            cntGosha = i
            break
    money2 = list(filter(lambda x: x >= min(moneyProductTmp), moneyGosha))
    print(money2)
    if sumGosha != 0:
        break

print(sumGosha, cntGosha)




Products= []
