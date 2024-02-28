import matplotlib.pyplot as plt
p = int(input("Введите число p: "))
q = int(input("Введите число q: "))
t = 0
y0 = 1
c0 = y0
z0 = y0
z_max = 10*(100+4*p+3*q+1)
i = p + q + 1
arr = []

def depositFunc(t, z0, i, c0):
        t += 1
        c0 += z0*0.1
        z0 += (z0 * (0.01 * i))+(c0)
        return z0, t, c0

x = depositFunc(t, z0, i, c0)

while True:
    if x[1] < 5:
        z0 = x[0]
        t = x[1]
        c0 = x[2]
        x = depositFunc(t, z0, i,c0)
        arr.append(x[0])
    elif x[1] == 5:
        if x[0] > (z_max):
              print("минимальное число ", y0," число ", round(x[0],2))
              exit()
        else:
            y0+=1
            z0=y0
            c0=y0
            t = 0
            x = depositFunc(t, z0, i, c0)
            


