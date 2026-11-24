#=======================================================
# TASK 1: Print each DNA sequence on a seperate line.
# dna_sequences = ["ATGC", "GCTA", "TTAG", "CCGA"]
#=======================================================

dna_sequences = ["ATGC", "GCTA", "TTAG", "CCGA"]
print(dna_sequences[0])
print(dna_sequences[1])
print(dna_sequences[2])
print(dna_sequences[3])

#=======================================================
# TASK 2: Use a for loop and len() to print each sequence's length.
# dna_sequences = ["ATGA", "GCTAGG", "TTAG"]
#=======================================================

dna_sequences = ["ATGA", "GCTAGG", "TTAG"]
for seq in dna_sequences:
    print(len(seq))

#=========================================================
# TASK 3: Print each sequence with its length, e.g. ATGA 4.
# dna_sequences = ["ATGA", "GCTAGG", "TTAG"]
#=========================================================

dna_sequences = ["ATGA", "GCTAGG", "TTAG"]
for seq in dna_sequences:
    print(seq, len(seq))

#=========================================================
# TASK 4: Print each sequence and how many A characters it contains.
# dna_sequences = ["AATG", "GCTA", "TTTT", "AGAA"]
#=========================================================

dna_sequences = ["AATG", "GCTA", "TTTT", "AGAA"]
for seq in dna_sequences:
    print(seq, seq.count("A"))

#=========================================================
# TASK 5: Use .count("C") to print the number of C characters in each sequence.
# dna_sequences = ["ACGT", "CCCC", "ATAT", "GCCA"]
#=========================================================

dna_sequences = ["ACGT", "CCCC", "ATAT", "GCCA"]
for seq in dna_sequences:
    print(seq.count("C"))

#=========================================================
# TASK 6: Find the total number of A characters across all sequences.
# Hint: Start total_A at 0 and add each sequence's count.
# dna_sequences = ["ATGA", "GCTA", "TTAG"]
#=========================================================

dna_sequences = ["ATGA", "GCTA", "TTAG"]
total_A = 0
for seq in dna_sequences:
    total_A = total_A + seq.count("A")
print(total_A)

#=========================================================
# TASK 7: Print each nucleotide in the string on its own line.
# dna_sequences = "ATGCCATA"
#=========================================================

dna_sequences = "ATGCCATA"
for nucleotide in dna_sequences:
    print(nucleotide)

#=========================================================
# TASK 8: Practise looping through a string . Print each character.
# For this task, do not use .count().
# dna_sequences = "AAGCTTA"
#=========================================================

dna_sequences = "AAGCTTA"
for seq in dna_sequences:
    print(seq)

#=========================================================
# TASK 9: Use enumerate() to print each nucleotide with its index. 
# Print the index first and the nucleotide second.
# dna_sequences = "GCTA"
#=========================================================

dna_sequences = "GCTA"
for position, nucleotide in enumerate(dna_sequences):
    print(position, nucleotide)

#=========================================================
# TASK 10: Use enumerate() to print the index and each sequence in this list.
# dna_sequences = ["ATGC", "GCTA", "TTAG"]
#=========================================================

dna_sequences = ["ATGC", "GCTA", "TTAG"]
for position, seq in enumerate(dna_sequences):
    print(position, seq)

#=========================================================
# TASK 11: Use enumerate() to print each sequence like:
# Index: 0 Sequence: ATGC
# dna_sequences = ["ATGC", "GCTA", "TTAG"]
#=========================================================

dna_sequences = ["ATGC", "GCTA", "TTAG"]
for position, seq in enumerate(dna_sequences):
    print(position, seq)

#=========================================================
# TASK 12: For each sequence, print the sequence, its length, and the number of A characters it contains
# dna_sequences = ["ATGAA", "GCTAAC", "TTAG"]
#=========================================================

dna_sequences = ["ATGAA", "GCTAAC", "TTAG"]
for seq in dna_sequences:
    print(seq, len(seq), seq.count("A"))

#=========================================================
# Optional challenge: Calculate the total number of G characters across all sequences and print the final total.
# dna_sequences = ["ATGC", "GGTA", "CCGG"]
#=========================================================

dna_sequences = ["ATGC", "GGTA", "CCGG"]
total_G = 0
for seq in dna_sequences:
    total_G = total_G + seq.count("G")
print(total_G)