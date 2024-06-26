import math

def main():
    p = int(input("Введите p: "))
    q = int(input("Введите q: "))
    m, n = 5, 5
    r = [0] * m
    e = [0] * 4
    a = []
    b = []

    for k in range(m):
        r[k] = p + q + k + 1

    # Находим ЭДС
    e[0] = 2 * (p + q) + 30
    e[1] = 2 * (p + q) + 60
    e[2] = 3 * (p + q) + 80
    e[3] = 8 * (p + q) + 100

    b = [0, 0, e[0] + e[2], e[1], e[2] + e[3]]

    # В результате решения СЛАУ находим распределение токов в электрической цепи
    a = [[-1, 0, 1, -1, 0],
         [1, -1, 0, 0, 1],
         [r[0], 0, r[2], 0, -1 * r[4]],
         [0, r[1], 0, 0, r[4]],
         [0, 0, r[2], r[3], 0]]

    for k in range(m):
        # Проверка ведущего элемента (элемент, лежащий на главной диагонали текущей строки)
        if a[k][k] == 0:
            # Ведущий элемент равен 0, меняем уравнения местами (переставляем строки матрицы)
            # Ищем не нулевой элемент среди элементов столбца, лежащих ниже
            max_val = 0
            imax = k
            for l in range(k + 1, n):
                if abs(a[l][k]) > max_val:
                    max_val = abs(a[l][k])
                    imax = l

            # Меняем уравнения местами
            for j in range(k, n):
                a[k][j], a[imax][j] = a[imax][j], a[k][j]

            b[k], b[imax] = b[imax], b[k]

        akk = a[k][k]
        b[k] /= akk  # Делим правую часть на ведущий элемент
        for j in range(k, n):
            a[k][j] /= akk  # Делим текущую строку на ведущий элемент

        for l in range(k + 1, n):
            # Перебираем последующие строки, получаем 0 в k-ом столбце
            if a[l][k] != 0:
                aik = a[l][k]
                b[l] /= aik
                b[l] -= b[k]

                for j in range(k, n):
                    a[l][j] /= aik
                    a[l][j] -= a[k][j]

    # Обратный ход методом Гауса
    for l in range(n - 2, -1, -1):
        for j in range(l + 1, n):
            b[l] -= a[l][j] * b[j]

    print("\nРасчёт распределения токов в электрической цепи")
    print("Ляшенко И.Д.")
    print(f"p = {p}, q = {q}")
    for k in range(m):
        print(f"r[{k}] = {r[k]}")
    print("Значение токов в ветвях")
    for k in range(m):
        print(f"i[{k + 1}] = {round(b[k] * 1000) / 1000}")
    print(f"Значение ЭДС 2-го источника равно {0.8 * e[1]}")

if __name__ == "__main__":
    main()


