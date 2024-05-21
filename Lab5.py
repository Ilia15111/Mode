import math



PI = 3.14
g = 9.8

def main():
    p = int(input("Введите p: "))
    q = int(input("Введите q: "))
    print(f"p = {p}\nq = {q}")

    # Нахождение значения переменных
    k1 = 0.2 + 0.1 * p
    k2 = 0.04 + 0.01 * p
    h = H = 5 * (20 + 2 * p + q) ** 2
    m = 200 + 20 * p + 10 * q
    v_c = (600 + 2 * p + 4 * q) * 1000 / 3600
    v_k = (60 + p + q) * 1000 / 3600
    v = t = x = 0
    Tau = 0.2  # Шаг по времени

    print(f"\nk1 = {k1}\nk2 = {k2}\nm = {m} кг\nv_самолёта = {round(v_c, 2)} м/c\nv_колонны = {round(v_k, 2)} м/с\nH = {H} м\n")

    # Решение поставленной задачи
    print("t, с\tv, м/с\t\tx, м\t\ty, м\t\th, м")
    while h > 0:
        A = Tau * k2 / m
        B = 1 + Tau * k1 / m
        C = v + Tau * g
        x = x + Tau * v
        v = (math.sqrt(B * B + 4 * A * C) - B) / (2 * A)
        h_previous = h
        h = H - x
        t_previous = t
        t += Tau
        print(f"{round(t, 2)}\t{round(v, 2)}\t\t{round(x, 2)}\t\t{round(v_c * t, 2)}\t\t{round(h, 2)}")

    t_fall = t_previous - (h_previous / (h - h_previous)) * (t - t_previous)
    l = (v_c - v_k) * t_fall
    print(f"\nВремя падения: {round(t_fall, 2)} с\nУпреждение: {round(l, 2)} м")

if __name__ == "__main__":
    main()
