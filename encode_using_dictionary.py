
def encode_length(input_str):
    number_code={'1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'(','0':')'}
    output_str=''
    for c in input_str:
        if c in number_code:
            output_str=output_str+number_code[c]
        else:
            output_str=output_str+c
        print('Input Character: ',c,'Output String: ',output_str)
    print('Final Output String: ',output_str)
    return output_str
input_string='3a2b5c'
print("Input String:", input_string)
final_str=encode_length(input_string)
            