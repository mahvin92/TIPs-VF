import random
from Bio import SeqIO

# Define the junction sequence
JUNCTION_SEQUENCE = (
    "cagccttccctggctccctccccatttcctctcatgggcatttcttctaataaaatctgcagaccatattgggtctaatcccatctccagtctgcttcttggaggaaccagactaacatgactctgccctatataatacaaataattattttccatatatctgatttttagctttgcatttactttaaatcatgcttcaattaaagacacaccttctttaatcattttattagtatttctaagtatgatg"
)

# Function to generate random subsequences
def generate_random_subsequence(sequence, length):
    start = random.randint(0, len(sequence) - length)
    return sequence[start : start + length]

# Function to generate synthetic sequences
def generate_synthetic_sequences(seq1, seq2, include_junction=True):
    synthetic_sequences = []
    for i in range(1000):
        part1 = generate_random_subsequence(seq1, 1500)
        part2 = generate_random_subsequence(seq2, 1500)
        if include_junction:
            synthetic_sequence = part1 + JUNCTION_SEQUENCE + part2
        else:
            synthetic_sequence = part1 + part2
        synthetic_sequences.append(synthetic_sequence)
    return synthetic_sequences

# Function to invert sequences while keeping the junction in the middle
def invert_sequences(sequences, include_junction=True):
    inverted_sequences = []
    for seq in sequences:
        if include_junction:
            part1, junction, part2 = seq[:1500], seq[1500:1500+len(JUNCTION_SEQUENCE)], seq[1500+len(JUNCTION_SEQUENCE):]
            inverted_sequence = part2[::-1] + junction + part1[::-1]
        else:
            part1, part2 = seq[:1500], seq[1500:]
            inverted_sequence = part2[::-1] + part1[::-1]
        inverted_sequences.append(inverted_sequence)
    return inverted_sequences

# Write sequences to a FASTA file
def write_to_fasta_file(sequences, list_name, output_file):
    with open(output_file, "a") as f:
        for i, seq in enumerate(sequences):
            f.write(f">{list_name}-{i+1}\n{seq}\n")

# Main function
def main():
    # Input file containing two FASTA sequences
    input_file = "seq1-2.txt"
    output_file = "junction-assessment.txt"

    # Read the two sequences from the input file
    records = list(SeqIO.parse(input_file, "fasta"))
    if len(records) != 2:
        raise ValueError("The input file must contain exactly two FASTA sequences.")
    seq1, seq2 = str(records[0].seq), str(records[1].seq)

    # Generate the four lists of synthetic sequences
    list1 = generate_synthetic_sequences(seq1, seq2, include_junction=True)
    list2 = invert_sequences(list1, include_junction=True)
    list3 = generate_synthetic_sequences(seq1, seq2, include_junction=False)
    list4 = invert_sequences(list3, include_junction=False)

    # Clear the output file if it exists
    open(output_file, "w").close()

    # Write the sequences to the output file in FASTA format
    write_to_fasta_file(list1, "list1", output_file)
    write_to_fasta_file(list2, "list2", output_file)
    write_to_fasta_file(list3, "list3", output_file)
    write_to_fasta_file(list4, "list4", output_file)

    print(f"Synthetic sequences have been saved to {output_file}.")

if __name__ == "__main__":
    main()
