import matplotlib.pyplot as plt

t = 0
p = int(input("Введите число p: "))
q = int(input("Введите число q: "))
y0 = 101
c0 = y0
z0 = y0
i = p + q + 1
arr = []

def depositFunc(t, z0, i, c0):
        t += 1
        c0 += z0*0.1
        z0 += (z0 * (0.01 * i))+(c0)
        return z0, t, c0



x = depositFunc(t, z0, i,c0)
arr.append(x[0])
print("=====================================================================")
print(x[1], " | ", f"{round(z0, 2)}+{round(z0 * (0.01 * i), 2)}+{round(x[2],2)}={round(x[0], 2)}")
while x[0] <= (y0 * 5):
    z0 = x[0]
    t = x[1]
    c0 = x[2]
    x = depositFunc(t, z0, i,c0)
    arr.append(x[0])
    print("=====================================================================")
    print(x[1], " | ", f"{round(z0, 2)}+{round(z0 * (0.01 * i), 2)}+{round(x[2],2)}={round(x[0], 2)}")




plt.plot(arr)
plt.show()
