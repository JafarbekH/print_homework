x=2567
# x 4 xonali son. shuni taeskari yozilganni chiqarishimiz kerak ya'ni 7652
x1=x%10
x2=x%100//10
x3=x%1000//100
x4=x//1000
print(x1*10**3+x2*10**2+x3*10+x4)