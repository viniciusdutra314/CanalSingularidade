from sys import getsizeof
x=1
for i in range(1,100_000): 
    print(f"tamanho em bytes : {sys.getsizeof(x):E} ({len(str(x))} dígitos )")
    x*=i

with open("result.txt","w") as file:
    file.write(str(x))