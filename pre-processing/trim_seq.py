import re

# Input and output file names
input_file = "input_sequences.txt"
output_file = "cleaned_sequences.txt"

def clean_fasta_sequences(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        current_header = None
        current_sequence = []

        for line in infile:
            line = line.strip()
            
            if line.startswith(">"):
                # If a header is encountered and we have a sequence, process and write it
                if current_header and current_sequence:
                    # Combine the sequence and trim non-ATCG characters
                    cleaned_sequence = re.sub(r"[^ATCG]", "", "".join(current_sequence))
                    outfile.write(f"{current_header}\n{cleaned_sequence}\n")

                # Start a new header
                current_header = line
                current_sequence = []
            else:
                # Accumulate sequence lines
                current_sequence.append(line)

        # Process the last sequence in the file
        if current_header and current_sequence:
            cleaned_sequence = re.sub(r"[^ATCG]", "", "".join(current_sequence))
            outfile.write(f"{current_header}\n{cleaned_sequence}\n")

# Run the cleaning function
clean_fasta_sequences(input_file, output_file)

print(f"Sequences have been cleaned and saved to '{output_file}'.")
