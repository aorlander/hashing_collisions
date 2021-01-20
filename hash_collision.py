import hashlib
import os
import random

def hash_collision(k):
    
    from hashlib import sha256
    from random import randrange

    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
    
    #Collision finding code goes here
    
    upper_bound = round(pow(2,k),0)
    #The return variables, x and y, should be encoded as bytes.
    #To encode a string as bytes
    seed = str(randrange(upper_bound))
    byte_seed = seed.encode('utf-8')
    x = byte_seed
    y = byte_seed * 2
    
    for i in range(upper_bound):
        h_x = sha256(x).hexdigest()
        h_y = sha256(y).hexdigest()
        #You're checking the last k bits of the hash produced 
        # by the sha256. You'll have to convert the hex number 
        # into binary and look at the last k digits.
        b_x = "{0:08b}".format(int(h_x, 16)) 
        b_y = "{0:08b}".format(int(h_y, 16))

        if ((b_x)[-k:] == (b_y)[-k:]):
            print("MATCH!")
            print("--------------H(x)-----------------")
            print((b_x))
            print("--------------H(y)-----------------")
            print((b_y))
            print("-------------------------------")
            print("Last " + str(k) + " digits") 
            print("-------------------------------")
            print((b_x)[-k:])
            print((b_y)[-k:]) 
            break
        else:
            x = int(x)
            y = int(y)
            x=x+randrange(upper_bound)
            y=y+randrange(upper_bound)
            x = str(x).encode('utf-8')
            y = str(y).encode('utf-8')

    # n bits long digest is at most as secure as a symmetric 
    # encryption algorithm keyed with n/2 bits
    x=int(x)
    y=int(y)
    return( x, y )
    pass


# The python interpreter actually executes the function body here
print("Answer: ")
print(hash_collision(5))
