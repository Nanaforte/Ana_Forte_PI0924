s=int(input("Introduz os segundos: "))

if s >= 3600:  #se seg forem maiores ou iguais a 3600
    h = s // 3600   #div int para h
    resto = s % 3600  #resto seg com 3600   ex 3600=s   resto=65
    m = resto // 60  #min
    s = resto % 60  #seg

elif s >= 60:
    h = 0
    m = s // 60
    s = s % 60

else:
    h = 0
    m = 0

print(h, "hora(s),", m, "minuto(s) e", s, "segundo(s)")