def encode_length(input_str):  
    output_str = ''  
    current_position = ''    
    for i in range(len(input_str)):  
        current_position=symbol_code(input_str[i])       
        # Counting of characters in each iteration 
        print("Input Character =", input_str[i], ", Output String =", output_str)  
        output_str = output_str + current_position       
    # Final output string 
    print("Final Output String:", output_str) 
    return output_str
def symbol_code(c):
    if c == '1':
        return '!'
    elif c == '2':
        return '@'
    elif c == '3':
        return '#'
    elif c == '4':
        return '$'
    elif c == '5':
        return '%'
    elif c == '6':
        return '^'
    elif c == '7':
        return '&'
    elif c == '8':
        return '*'
    elif c == '9':
        return '('
    elif c=='0':
        return ')'
    else:
        return c
# Test Example 
input_string = "20a2b3c" 
print("Input String:", input_string) 
encode_length(input_string) 