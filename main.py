"""
CMPS 6610  Problem Set 2
See problemset-02.pdf for details.
"""
import time
import tabulate

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

# some useful utility functions to manipulate bit vectors
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y
    
def quadratic_multiply(x: BinaryNumber, y: BinaryNumber):

    result_val = 0
    for i, bit in enumerate(reversed(y.binary_vec)):
        if bit == '1':
            result_val += x.decimal_val << i
    return BinaryNumber(result_val)


def subquadratic_multiply(x: BinaryNumber, y: BinaryNumber):
    
    if x.decimal_val < 10 or y.decimal_val < 10:
        return BinaryNumber(x.decimal_val * y.decimal_val)

    X, Y = pad(x.binary_vec, y.binary_vec)
    n = len(X)

    xL, xR = split_number(X)
    yL, yR = split_number(Y)

    xLyL = subquadratic_multiply(xL, yL)
    xRyR = subquadratic_multiply(xR, yR)
    xLxR_yLyR = subquadratic_multiply(BinaryNumber(xL.decimal_val + xR.decimal_val),
                                  BinaryNumber(yL.decimal_val + yR.decimal_val))

    xLyR_xRyL = xLxR_yLyR.decimal_val - xLyL.decimal_val - xRyR.decimal_val

    m = n // 2
    result_val = (xLyL.decimal_val << (2*m)) + (xLyR_xRyL << m) + xRyR.decimal_val
    return BinaryNumber(result_val)


## Feel free to add your own tests here.
def test_multiply():
    assert binary2int(quadratic_multiply(BinaryNumber(2), BinaryNumber(2))) == 2*2

# some timing functions here that will make comparisons easy    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000
    
def compare_multiply():
    res = []
    for n in [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]:
        qtime = time_multiply(BinaryNumber(n), BinaryNumber(n), quadratic_multiply)
        subqtime = time_multiply(BinaryNumber(n), BinaryNumber(n), subquadratic_multiply)        
        res.append((n, qtime, subqtime))
    print_results(res)


def print_results(results):
    print("\n")
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'quadratic', 'subquadratic'],
            floatfmt=".2f",
            tablefmt="github"))

    
if __name__ == '__main__':
    compare_multiply()
