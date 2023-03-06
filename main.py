"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

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
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    ### TODO
		x_vec,y_vec = pad(x.binary_vec,y.binary_vec)
		x_left,x_right = split_number(x_vec)
		y_left,y_right = split_number(y_vec)

		if x.decimal_val == 0 or y.decimal_val == 0:
			return BinaryNumber(0)
		if x.decimal_val == 1 and y.decimal_val == 1:
			return BinaryNumber(1)

		x_sum = BinaryNumber(x_left.decimal_val + x_right.decimal_val)
		y_sum = BinaryNumber(y_left.decimal_val + y_right.decimal_val)

		product1 = subquadratic_multiply(x_left, y_left)
		product2 = subquadratic_multiply(x_right,y_right)
		product3 = subquadratic_multiply(x_sum,y_sum)

		shift_sum = BinaryNumber(product3.decimal_val - product1.decimal_val - product2.decimal_val)

		return BinaryNumber(bit_shift(product1,len(x_vec)).decimal_val + bit_shift(shift_sum, len(x_vec)//2).decimal_val + product2.decimal_val)
		
		
    ###

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(323895239587), BinaryNumber(1203934097234)).decimal_val == 323895239587*1203934097234

def time_multiply(x, y, f):
		start = time.time()
		# multiply two numbers x, y using function f
		f(BinaryNumber(x),BinaryNumber(y))
		return (time.time() - start)*1000

    
print(time_multiply(1234,5678,subquadratic_multiply))

