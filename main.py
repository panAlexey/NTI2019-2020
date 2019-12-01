koefPascal = [[5, 10, 10, 5, 1], [6, 15, 20, 15, 6, 1], [7, 21, 35, 35, 21, 7, 1], [8, 28, 56, 70, 56, 28, 8, 1],
              [9, 36, 84, 126, 126, 84, 36, 9, 1], [10, 45, 120, 210, 252, 210, 120, 45, 10, 1]]

def analisProducts(Clothes):
    pass

def analisGosha(Gosha):
    Gosha.sort()
    mnojestvoGosha = set()
    print(Gosha)
    # for ch in range(len(Gosha) - 1):

def sumGosha():
    pass

def smGosha(Gosha, cnt, sm):
    print('-------------------------', cnt, len(Gosha))
    if cnt == len(Gosha):
        return [sum(Gosha)]
    if cnt == 1:
        return Gosha
    k = 0
    sm2 = []
    print('summa:', len(Gosha) - 1, Gosha)
    for i in range(len(Gosha) - 1):
         sm1 = smGosha(Gosha[i + 1:], cnt - 1, sm)
         for j in range(len(sm1)):
             sm1[j] += Gosha[i]
         sm2.extend(sm1)
         print(sm1, sm2)
    return sm1


def analisGosha2(Gosha, num, mn):
    print(Gosha, len(Gosha))
    print('Hello')
    for ch in range(len(Gosha)):
         sm = []
         lengthSM = koefPascal[len(Gosha) - 5]
         print(ch, '---- koef Pascal: ', lengthSM)
         for i in range(lengthSM[ch]):
             sm += [0] # ch + 1 - по сколько чисел суммируем
         print(sm)
         # for cnt in range(1, len(Gosha) + 1):
         sm = smGosha(Gosha, ch + 1, sm)
         print(ch + 1, '->', sm)



def analisGosha3(prom, current, mn, num, sm):
    if num == 1:
        for ch in len(sm):
            sm[ch] += prom[ch]

string = input().split('],[')
# print(string)
string[0] = string[0][1:]
string[2] = string[2][:-1]
Gosha = [int(i) for i in string[0].split(', ')]
Kassir = [int(i) for i in string[1].split(', ')]
Clothes = [int(i) for i in string[2].split(', ')]

print(Gosha, Kassir, Clothes, sum(Gosha), sum(Kassir), sum(Clothes))
analisGosha2(Gosha, 1, 0)
Products= []
