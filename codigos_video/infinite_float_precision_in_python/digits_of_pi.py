from fractions import Fraction
from decimal import *
getcontext().prec=100
pi_frac=Fraction(0,1)

for k in range(100):
    pi_frac+=Fraction(1,16**k)*(Fraction(4,8*k+1)-Fraction(2,8*k+4)-Fraction(1,8*k+5)-Fraction(1,8*k+6))
numerator,denominator=pi_frac.as_integer_ratio() 
print(Decimal(numerator)/Decimal(denominator))

 