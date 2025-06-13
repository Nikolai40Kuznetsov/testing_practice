import math as m

def equalize(a, b, c):
    try:
        y = (m.factorial(a) - m.sqrt(b)) / c**3
    except ZeroDivisionError:
        result = ["There is zero division",]
        raise ZeroDivisionError("htrhrrfgh")
    except ValueError:
        result = "Can't sqrt negative"
    except TypeError:
        result = "This is not number"
    else:
        result = round(y, 4)
    return result