#!/usr/bin/python3

def magic_calculation(a, b):
    final_result = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception('long!!, try again')
            final_result += a ** b / j
        except Exception:
            final_result = b + a
            break
    return final_result
