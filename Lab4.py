import math

PI = 3.14

# меню подстроенно для значений 2 1
def main():
    p = int(input("Введите p: "))
    q = int(input("Введите q: "))

    # Нахождение значения переменных
    a = 1 + 0.1 * (p + q + 2)
    A = 0.2 * (p + q + 1)
    B = 5 + p + q
    l = 10 + p + q
    h = l / 20
    R = A * math.pow(l, a) + B
    r = A * math.pow(0, a) + B

    # Нахождение точного ��начения интеграла Beta_V
    Beta_V = PI * (A * A * (math.pow(l, 2 * a + 1) / (2 * a + 1)) + 2 * A * B * (math.pow(l, a + 1) / (a + 1)) + B * B * l)

    # f(x)=A*pow(x,a) + B
    x = [k * h for k in range(21)]
    y = [math.pow(A * math.pow(x[k], a) + B, 2) for k in range(21)]  # y(x) = f(x)^2 

    # Нахождение массы цилиндрической загатовки
    Fe = 0.007856
    m_Cylinder = round(Fe * (PI * math.pow(R, 2) * l) * 100) / 100

    # Нахождение массы конусообразной загатовки
    m_Cone = round(Fe * (PI / 3 * l * (R * R + R * r + r * r)) * 100) / 100

    # Нахождение массы прямоугольников
    V = sum(PI * h * y[k] for k in range(1, 21))
    m_Rectangle = round(Fe * V * 100) / 100
    Beta_R = round(abs(Beta_V - V) / Beta_V * 10000) / 100

    # Нахождение массы трапеций
    V = PI * h * (y[0] + y[20]) / 2 + sum(PI * h * y[k] for k in range(1, 20))
    m_Trapezoid = round(Fe * V * 100) / 100
    Beta_T = round(abs(Beta_V - V) / Beta_V * 10000) / 100

    # находим result_R_Cy, result_R_Co, result_T_Cy, result_T_Co
    result_R_Cy = m_Cylinder - m_Rectangle
    result_R_Co = m_Cone - m_Rectangle
    result_T_Cy = m_Cylinder - m_Trapezoid
    result_T_Co = m_Cone - m_Trapezoid

    print(f"p = {p}\nq = {q}")
    print("Масса детали по формуле\t Масса заготовки | Масса отходов | Расхождение \t|")
    print("\t\t\t цилиндрическая\t | конусообразная|\t\t|")
    print(f"\t\t\t\t{m_Cylinder}\t |\t{m_Cone}\t |\t\t|")
    print(f"Прямоугольников\t{m_Rectangle}     {result_R_Cy}, {round(result_R_Cy / m_Cylinder * 10000) / 100}% | {result_R_Co}, {round(result_R_Co / m_Cone * 10000) / 100}% | {m_Cylinder - m_Cone},{(round(result_R_Cy / m_Cylinder * 10000) - round(result_R_Co / m_Cone * 10000)) / 100}%|")
    print(f"Тра��еций\t{m_Trapezoid}    {result_T_Cy}, {round(result_T_Cy / m_Cylinder * 10000) / 100}% | {result_T_Co}, {round(result_T_Co / m_Cone * 10000) / 100}% | {m_Cylinder - m_Cone},{(round(result_T_Cy / m_Cylinder * 10000) - round(result_T_Co / m_Cone * 10000)) / 100}%|\n")
    print("Отсносительная погрешность числ��нных меттодов вычисления объёма детали")
    print(f"Для квадратуры прямоугольников\t{Beta_R}%\nДля квадратуры трапеций\t\t{Beta_T}%\n")

if __name__ == "__main__":
    main()


