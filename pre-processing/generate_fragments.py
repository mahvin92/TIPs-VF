import random

def process_fasta(input_file, output_file):
    with open(input_file, 'r') as file:
        # Read the entire fasta file content
        fasta_content = file.read()

    # Split the content into parts based on '>'
    sequences = fasta_content.split('>')

    # Remove any empty elements from splitting
    sequences = [seq for seq in sequences if seq.strip()]

    # Process each sequence
    processed_sequences = []
    for seq in sequences:
        # Split the sequence name and the sequence data
        lines = seq.strip().split('\n')
        seq_name = lines[0]
        seq_data = ''.join(lines[1:])  # Join all the sequence lines

        # Step 1: Trim to 15,000 nucleotides
        trimmed_sequence = seq_data[:15000]

        # Add the trimmed sequence with the original name
        processed_sequences.append(f">{seq_name}\n{trimmed_sequence}")

        # Step 2: Generate 100 random subsequences of 12,500 nucleotides each
        sequence_length = len(trimmed_sequence)
        generated_positions = set()

        for i in range(100):
            while True:
                # Randomly choose a valid starting position
                start = random.randint(0, sequence_length - 12500)
                
                # Ensure no duplicate starting positions
                if start not in generated_positions:
                    generated_positions.add(start)
                    break
            
            # Extract the subsequence
            end = start + 12500
            subsequence = trimmed_sequence[start:end]
            processed_sequences.append(f">{seq_name}-{i+1}\n{subsequence}")

    # Write the result to a new file
    with open(output_file, 'w') as out_file:
        out_file.write('\n'.join(processed_sequences))


# Example usage
input_file = 'chr3.txt'  # Replace with your input file name
output_file = 'chr3-subseq.txt'  # Replace with your desired output file name
process_fasta(input_file, output_file)
