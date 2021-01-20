import hashlib
import os

# Write a function called “hash_collision” that takes a single input, k, where k is an integer. 
# The function “hash_collision” should return two variables, x and y, such that that the SHA256(x) and SHA256(y) match on their final k bits. 
# Your algorithm should be randomized, i.e., hash_collision(k) should not always return the same colliding pair.

def hash_collision(k):
 
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
    
    #Collision finding code goes here
    x = b'\x00'
    y = b'\x00'

    #The return variables, x and y, should be encoded as bytes.
    #To encode a string as bytes
    str = "Hello World"
    byte_str = str.encode('utf-8')
    hsh = hashlib.sha256().update(byte_str)
    print(hsh)

    
    print(x, y)

    return( x, y )
    pass


# The python interpreter actually executes the function body here
print("Answer: ")
hash_collision(3)
