import decimal
from decimal import Decimal
from numbers import Number
import cmath

def is_perfect_square(num, *, complex=False):
    if not isinstance(num, Number):
        raise TypeError("Not a numeric type")
    nums = []
    input_not_complex = False
    try:
        Decimal(num)
        input_not_complex = True
    except TypeError:
        # Number is complex
        if not complex:
            raise TypeError("Complex number given but complex=False")
        else:
            sqrt = cmath.sqrt(num)
            return is_whole(Decimal(sqrt.real)) and is_whole(Decimal(sqrt.imag))

    if input_not_complex:
        if num < 0 and not complex:
            return False
            #  raise TypeError("Can't have negative number and complex=False")
        num = abs(num)
        sqrt = Decimal(num).sqrt()
        return is_whole(sqrt)

def is_whole(num):
    return num == num.to_integral_exact()


# ================================================================================
# Full solution from morsels
import cmath

def is_perfect_square(number, *, complex=False):
    """Return True if given number is the square of an integer."""
    if complex:
        root = cmath.sqrt(number)
        return root.real.is_integer() and root.imag.is_integer()
    if number < 0:
        return False
    digit_count = len(str(number))
    with localcontext(Context(prec=digit_count*2)):
        return int(Decimal(number).sqrt())**2 == number
