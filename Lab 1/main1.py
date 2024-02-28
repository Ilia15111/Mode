import matplotlib.pyplot as plt

t = 0
p = int(input("Введите число p: "))
q = int(input("Введите число q: "))
y0 = 101
z0 = y0
i = p + q + 1
arr = []

def depositFunc(t, z0, i):
    t += 1
    z0 = z0 + (z0 * (0.01 * i))
    return z0, t

x = depositFunc(t, z0, i)
arr.append(x[0])
print("=====================================================================")
print(x[1], " | ", f"{round(z0, 2)}+{round(z0*(0.01*i), 2)}={round(x[0], 2)}")
while x[0] <= (y0 * 2):
    z0 = x[0]
    t = x[1]
    x = depositFunc(t, z0, i)
    arr.append(x[0])
    print("=====================================================================")
    print(x[1], " | ", f"{round(z0, 2)}+{round(z0*(0.01*i), 2)}={round(x[0], 2)}")

plt.plot(arr)
plt.show()
