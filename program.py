string_name = "N^MZC"
num_values = range(5,15)
encrypted_value_matrix=[]

for element in string_name:
    rowList = []
    for number in num_values:
        element_values = [chr(ord(element)^number)]
        rowList.append(element_values)
    encrypted_value_matrix.append(rowList)


print(encrypted_value_matrix)

init_var=0
for first_element_index in range(len(encrypted_value_matrix[init_var])):
    for secound_element_index in range(len(encrypted_value_matrix[init_var+1])):
        for third_element_index in range(len(encrypted_value_matrix[init_var+2])):
            for forth_element_index in range(len(encrypted_value_matrix[init_var+3])):
                for fifth_element_index in range(len(encrypted_value_matrix[init_var+4])):
                    word=str(''.join(encrypted_value_matrix[init_var][first_element_index])
                    +''.join(encrypted_value_matrix[init_var+1][secound_element_index])
                    +''.join(encrypted_value_matrix[init_var+2][third_element_index])
                    +''.join(encrypted_value_matrix[init_var+3][forth_element_index])
                    +''.join(encrypted_value_matrix[init_var+4][fifth_element_index]))
                    print(word)
        






   


    