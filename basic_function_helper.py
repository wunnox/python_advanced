"""
Define the C-variables and functions from the C-files that are needed in Python
"""
from ctypes import c_double, c_int, CDLL

lib_path = 'basic_function.so'
basic_function_lib = CDLL(lib_path)

python_c_square = basic_function_lib.c_square
python_c_square.restype = None

def do_square_using_c(list_in):
    """Call C function to calculate squares"""
    n = len(list_in)
    c_arr_in = (c_double * n)(*list_in)
    c_arr_out = (c_double * n)()

    python_c_square(c_int(n), c_arr_in, c_arr_out)
    return c_arr_out[:]
