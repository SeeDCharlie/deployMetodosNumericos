import struct

## float to binary
def float_bin(number, places = 3): 
  
    whole, dec = str(number).split(".") 
    whole = int(whole) 
    dec = int (dec) 
    res = bin(whole).lstrip("0b") + "."

    for x in range(places): 

        whole, dec = str((decimal_converter(dec)) * 2).split(".") 
        dec = int(dec) 
        res += whole 
  
    return res 

def decimal_converter(num):  
    while num > 1: 
        num /= 10
    return num 

## float to octal

def float_octal(number, places = 3): 

    whole, dec = str(number).split(".") 
    whole = int(whole) 
    dec = int (dec) 
    res = oct(whole).lstrip("0o") + "."

    for x in range(places): 

        whole, dec = str((decimal_converter(dec)) * 8).split(".") 
        dec = int(dec) 
        res += whole 
  
    return res 

##float to hex

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])