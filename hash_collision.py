import hashlib
import os

def hash_collision(k):
    
    from hashlib import sha256

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
    str1 = "HELLO"
    byte_str1 = str1.encode('utf-8')

    h_x = sha256(x).hexdigest()
    h_y = sha256(y).hexdigest()
    for j in range(k):
        #print(j)
        #print("h_x=" + h_x[j])
        #print("h_y=" + h_y[j])
        #print("======")
        if(h_x[j]!=h_y[j]):
            break
                
    return( x, y )
    pass


# The python interpreter actually executes the function body here
print("Answer: ")
print(hash_collision(3))
