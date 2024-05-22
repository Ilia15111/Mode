import pulp

# Define the problem
prob = pulp.LpProblem("Production_Planning", pulp.LpMaximize)

# Decision variables
x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')
x3 = pulp.LpVariable('x3', lowBound=0, cat='Continuous')
x4 = pulp.LpVariable('x4', lowBound=0, cat='Continuous')

# Coefficients
profit = [12, 8, 10, 13]
time_required = [
    [12, 18, 16, 24],
    [10, 4, 8, 7],
    [64, 56, 60, 80],
    [30, 0, 18, 24],
    [21, 15, 8, 30]
]
time_available = [72000, 56000, 111760, 36000, 42000]

# Objective function
prob += 12*x1 + 8*x2 + 10*x3 + 13*x4, "Total Profit"

# Constraints
prob += 12*x1 + 18*x2 + 16*x3 + 24*x4 <= 72000
prob += 10*x1 + 4*x2 + 8*x3 + 7*x4 <= 56000
prob += 64*x1 + 56*x2 + 60*x3 + 80*x4 <= 111760
prob += 30*x1 + 18*x3 + 24*x4 <= 36000
prob += 21*x1 + 15*x2 + 8*x3 + 30*x4 <= 42000

# Решаем задачу
prob.solve(pulp.PULP_CBC_CMD(msg=False))

# Выводим результаты
print(f"Статус: {pulp.LpStatus[prob.status]}")
print(f"x1 (км кабеля типа 1): {x1.varValue}")
print(f"x2 (км кабеля типа 2): {x2.varValue}")
print(f"x3 (км кабеля типа 3): {x3.varValue}")
print(f"x4 (км кабеля типа 4): {x4.varValue}")
print(f"Общая прибыль: {pulp.value(prob.objective)}")

# Случай 2: С минимальными требованиями к производству по контрактам
# Определяем задачу
prob_contracts = pulp.LpProblem("Планирование_Производства_Контракты", pulp.LpMaximize)

# Переменные решения
x1_contract = pulp.LpVariable('x1', lowBound=1000, cat='Continuous')
x2_contract = pulp.LpVariable('x2', lowBound=200, cat='Continuous')
x3_contract = pulp.LpVariable('x3', lowBound=20, cat='Continuous')
x4_contract = pulp.LpVariable('x4', lowBound=10, cat='Continuous')

# Целевая функция
prob_contracts += 12*x1_contract + 8*x2_contract + 10*x3_contract + 13*x4_contract, "Общая прибыль"

# Ограничения
prob_contracts += 12*x1_contract + 18*x2_contract + 16*x3_contract + 24*x4_contract <= 72000
prob_contracts += 10*x1_contract + 4*x2_contract + 8*x3_contract + 7*x4_contract <= 56000
prob_contracts += 64*x1_contract + 56*x2_contract + 60*x3_contract + 80*x4_contract <= 111760
prob_contracts += 30*x1_contract + 18*x3_contract + 24*x4_contract <= 36000
prob_contracts += 21*x1_contract + 15*x2_contract + 8*x3_contract + 30*x4_contract <= 42000

# Решаем задачу
prob_contracts.solve(pulp.PULP_CBC_CMD(msg=False))

# Выводим результаты
print(f"Статус: {pulp.LpStatus[prob_contracts.status]}")
print(f"x1 (км кабеля типа 1): {x1_contract.varValue}")
print(f"x2 (км кабеля типа 2): {x2_contract.varValue}")
print(f"x3 (км кабеля типа 3): {x3_contract.varValue}")
print(f"x4 (км кабеля типа 4): {x4_contract.varValue}")
print(f"Общая прибыль: {pulp.value(prob_contracts.objective)}")