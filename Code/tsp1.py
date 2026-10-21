# from ortools.sat.python import cp_model
# print("A - Bat dau nhap du lieu", flush=True)
# n = int(input())
# cost = []
# for i in range(n):
#     col = list(map(int, input().split()))
#     col.append(col[0])
#     cost.append(col)
# print("B - Da nhap xong du lieu", flush=True)
# max_cost = float("-inf")
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             continue
#         max_cost = max(max_cost, cost[i][j])
# # create solver
# model = cp_model.CpModel()

# # create var
# X = [model.NewIntVar(1, n, f"X[{i}]") for i in range(n)]
# Y = [model.NewIntVar(0, max_cost * n, f"Y[{i}]") for i in range(n+1)]
# c = [[model.NewBoolVar(f"c[{i}][{j}]") for j in range(n+1)] for i in range(n)]

# # create constraint

# # X[i] != X[j]
# M = 10000
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             continue
#         model.Add(X[i] != X[j])

# # Start at city 1
# model.Add(Y[0] == 0)

# # travel all city
# for i in range(n):
#     model.Add(X[i] != i)

# # Calculate total cost
# for i in range(n):
#     for j in range(n+1):
#         model.Add(X[i] == j).OnlyEnforceIf(c[i][j])
#         model.Add(X[i] != j).OnlyEnforceIf(c[i][j].Not())
# for i in range(n):
#     for j in range(n+1):
#         model.Add(Y[j] == Y[i] + cost[i][j]).OnlyEnforceIf(c[i][j])
# print("C - Da tao xong mo hinh", flush=True)

# # Objective function
# model.Minimize(Y[n])

# # Solver
# solver = cp_model.CpSolver()
# solver.parameters.max_time_in_seconds = 10.0
# solver.parameters.log_search_progress = True
# print("D - Bat dau Solve", flush=True)
# status = solver.Solve(model)
# if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
#     print(solver.ObjectiveValue())
# else:
#     print(-1)
# print("E - Solve da ket thuc:", solver.StatusName(status), flush=True)
# print("Status:", solver.StatusName(status))

from ortools.sat.python import cp_model

model = cp_model.CpModel()
x = model.NewIntVar(0, 10, "x")
model.Minimize(x)

solver = cp_model.CpSolver()
solver.parameters.max_time_in_seconds = 5.0

print("Bat dau", flush=True)
status = solver.Solve(model)
print("Ket thuc:", solver.StatusName(status), flush=True)