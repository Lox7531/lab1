"""
12.вычислить при заданном x сумму s = 1+1/x+1/x^2+...+1/x^10.
"""
print("Введите x, при этом x не должен быть равен 0")
x=int(input())
s=0
for i in range(11):
    s+=(1/x)**i
print("Cумма равна",s)
"""
при x=1
s=0
for i in range(11):
    s+=(1/x1)**i
print("Cумма равна",s)
if s==11:
    print("Okay")
else:
    print("Its not fine")
"""
