from fractions import Fraction
from decimal import Decimal,getcontext
getcontext().prec=100
def f(x:Decimal): return x**2
for exponent in range(1,30):
    dx=Decimal(f"3.0001e-{exponent}");x=Decimal("1")
    df=f(x+dx)-f(x)
    derivative=df/dx
    print(f"{derivative}, {exponent=}")