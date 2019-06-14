def int_to_bin(x):
    result = ''
    
    while x > 1:
        result = str(x % 2) + result
        x = x // 2
        
    return str(x) + result
