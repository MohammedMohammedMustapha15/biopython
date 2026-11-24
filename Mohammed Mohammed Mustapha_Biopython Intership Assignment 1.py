# ==================================================
# TASK 1: STORE AND DISPLAY A DNA SEQUENCE
# ==================================================

# Create a variable named dna_sequence and store "ATGCGTAC" in it.
# Then print the sequence.

dna_sequence = "ATGCGTAC"
print(dna_sequence)

#====================================================
# Task 2: DISPLAY THE SEQUENCE LENGTH
#====================================================

print(len(dna_sequence))

#====================================================
# Task 3: COMBINE BIOLOGICAL INFORMATION
#====================================================

# Create two variables:
# gene_name = "TP53"
# Organism = "Homo sapiens"
# Combine them into one line of text with a space between them
# Expected format: TP53 Homo sapiens

gene_name = "TP53 "
organism = "Homo sapiens"
print(gene_name + organism)

#======================================================
# Task 4: CHANGE LETTER CASE
#======================================================

# Store the sequence "atgcctga" in a variable named dna_sequence.
# Print it in uppercase.
# Then print it in lowercase after storing the uppercase version.

dna_sequence = "atgcctga"
print(dna_sequence.upper())
print(dna_sequence.lower())

#======================================================
# Task 5: COUNT NUCLEOTIDES
#======================================================

# Store this sequence: "AAGCTTAGA"
# Print how many times each of these nucleotides appears:
# A, T, G, and C.
# Hint: Use count () and write each nucleotide inside quatation marks.

dna_sequence = "AAGCTTAGA"
print(dna_sequence.count("A"))
print(dna_sequence.count("T"))
print(dna_sequence.count("G"))
print(dna_sequence.count("C"))

#==================================================================
# Task 6: STORE A COUNT IN A VARIABLE
#==================================================================

# Store the DNA sequence "ATATGCA" in a variable named dna_sequence.
# Count the number of A nucleotides and store the result in a variable 
# named adenine_count. Print adenine_count.

dna_sequence = "ATATGCA"
adenine_count = dna_sequence.count("A")
print(adenine_count)

#==================================================================
# Task 7: INDEXING
#==================================================================

# Store "GATTACA" in a variable named dna_sequence.
# Print:
# - the first nucleotide
# - the third nucleotide
# - the last nucleotide
# Reminder: Python indexing starts from 0.

dna_sequence = "GATTACA"
print(dna_sequence[0])
print(dna_sequence[2])
print(dna_sequence[6])

#=============================================================
# Task 8: SLICING
#=============================================================

# Store "ATGCCGTTA" in a variable named dna_sequence.
# Print the first four nucleotides.
# Then print the section from index 2 up to, but not including, index 6.

dna_sequence = "ATGCCGTTA"
print(dna_sequence[0:4])
print(dna_sequence[2:6])

#=============================================================
# Task 9: PROTEIN SEQUENCE PRACTICE
#=============================================================

# Store the protein sequence "MKTWLL" in a variable named protein.
# Print the number of amino-acid letters in the sequence
# Print the first amino-acid letter.
# Print the first three letters.
# Hint: Use len(), indexing, and slicing

protein = "MKTWLL"
print(len(protein))
print(protein[0])
print(protein[0:3])

#================================================================
# Task 10: MINI SEQUENCE REPORT
#================================================================

# Store this DNA sequence: "atgcaagc"
# Your program should:
# 1. Print the original sequence.
# 2. Convert the sequence to uppercase and store it back in the variable
# 3. Print the uppercase sequence.
# 4. Print its length
# 5. Count and print the number of A nucleotides
# 6. Print the first nucleotide
# 7. Print the first four nucleotides
# Use the concepts from lesson 5 only

dna_sequence = "atgcaagc"
print(dna_sequence)
dna_sequence = "ATGCAAGC"
print(dna_sequence.upper())
print(len(dna_sequence))
print(dna_sequence.count("A"))
print(dna_sequence[0])
print(dna_sequence[0:4])

#=======================================================
# BONUS CHALLENGE (OPTIONAL)
#=======================================================

# Store "ATGATGATG" in a variable named dna_sequence.
# Count how many times the substring "ATG" appears.
# Hint: count() can count a group of characters as well as one letter.

dna_sequence = "ATGATGATG"
print(dna_sequence.count("ATG"))
