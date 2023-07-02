def decode_length(input_char):  
    symbol_code = {'!': '1', '@': '2', '#': '3', '$': '4', '%': '5', '^': '6', '&': '7', '*': '8', '(': '9', ')': '0'}
    str_output = ''    
    for c in input_char:
        if c in symbol_code:
            str_output += symbol_code[c]
        else:
            str_output += c
        print("Input Character =", c, ", Output String =", str_output) 
    print("Final Output String:", str_output) 
    return str_output

# Test Example 
input_string = "!a@b$c" 
print("Input String:", input_string) 
decode_length(input_string)

