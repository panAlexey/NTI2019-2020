koefPascal = [[5, 10, 10, 5, 1], [6, 15, 20, 15, 6, 1], [7, 21, 35, 35, 21, 7, 1], [8, 28, 56, 70, 56, 28, 8, 1],
              [9, 36, 84, 126, 126, 84, 36, 9, 1], [10, 45, 120, 210, 252, 210, 120, 45, 10, 1]]

def analisProducts(Clothes):
    pass

def analisGosha(Gosha):
    Gosha.sort()
    mnojestvoGosha = set()
    print(Gosha)
    # for ch in range(len(Gosha) - 1):

def analisGosha2(Gosha, num, mn):
    print(Gosha, len(Gosha))
    print('Hello')

    for ch in range(len(Gosha)):
         sm = []
         lengthSM = koefPascal[len(Gosha) - 5]
         for i in range(lengthSM[ch]):
             sm += [0]
         print(sm)

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
