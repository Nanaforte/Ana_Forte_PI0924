"""
2
3
5
7
#num so deixa de ser primo se encontrar um divisor
"""

num=2
contador=0

#vai repetir ate encontrar 10 nums primos
while contador<10:   
    for i in range(2, num):
        if num % i == 0:
            #n primo
            break
    else:
        #n tem divisor primo
        print(num)        
        contador+=1   #+1 num primo ate chegar a 10

    num+=1 #next number