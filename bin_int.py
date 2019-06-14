def int_to_bin(x):
    result = ''
    
    while x > 1:
        result = str(x % 2) + result
        x = x // 2
        
    return str(x) + result

def dec_to_bin(x, k):
    result = ''
    
    for i in range(k):
        x = x * 2
        y = int(x >= 1)
        result += str(y)
        x = x - y 
        
    return result

def bin_to_int(x):
    result = 0.0
    
    for i in range(len(x)):
        result += int(x[-i-1])*2**i
        
    return result

def bin_to_dec(x):
    result = 0.0
    
    for i in range(len(x)):
        result += int(x[i])/2**(i+1)
        
    return result
