def replace_non_atcg(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    with open(file_name, 'w') as file:
        for line in lines:
            if line.startswith('>'):
                # Write the line as is if it starts with '>'
                file.write(line)
            else:
                # Replace any character other than A, T, C, G with N
                updated_line = ''.join([char if char in 'ATCG' else 'N' for char in line.strip()])
                file.write(updated_line + '\n')

# Example usage
file_name = "seqData.txt"
replace_non_atcg(file_name)
