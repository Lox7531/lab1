v1=10
a1=1
v2=9
a2=1.6
t1=1
t2=4
def s(v,a,t):
    S=v*t+a*(0.5*(t**2))
    return(S)
if s(v1,a1,t1)>s(v2,a2,t1):
    print("Через 1 час большее расстояние у первого. S1=",s(v1,a1,t1),"S2=",s(v2,a2,t1))

else:
    print("Через 1 час большее расстояние у второго. S1=",s(v1,a1,t1),"S2=",s(v2,a2,t1))
if s(v1,a1,t2)>s(v2,a2,t2):
    print("Через 4 часa большее расстояние у первого. S1=",s(v1,a1,t2),"S2=",s(v2,a2,t2))

else:
    print("Через 4 часa большее расстояние у второго. S1=",s(v1,a1,t2),"S2=",s(v2,a2,t2))
def T(v_first,v_second,a_first,a_second):
    t_meeting=(-2*(v_first-v_second))/(a_first-a_second)
    return print("Второй догонит первого через",round(T(v1,v2,a1,a2),2),"часа")
def(T(v1,v2,a1,a2))



