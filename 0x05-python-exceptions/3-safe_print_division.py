#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides a and b and return result"""

    try:
        res = a / b
    except (TypeError, ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return (res)