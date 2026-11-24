#=========================================================
# TASK 1: Create a list genes containing "BRCA1", "TP53", "EGFR".
# Print the list and its data type
#=========================================================

genes = ["BRCA1", "TP53", "EGFR"]
print(genes)
print(type(genes))

#==========================================================
# Task 2: Create dna_sequences = ["ATGC", "GCTA", "TTAG"] and print it.
#==========================================================

dna_sequences = ["ATGC", "GCTA", "TTAG"]
print(dna_sequences)

#===========================================================
# TASK 3: Using the list below, print the first sequence, second sequence, and first character of the first sequence. Remember indexing starts at 0.
# dna_sequences = ["ATGC", "GCTA", "TTAG"]
#===========================================================

dna_sequences = ["ATGC", "GCTA", "TTAG"]
print(dna_sequences[0])
print(dna_sequences[1])
print(dna_sequences[0][0])

#============================================================
# TASK 4: Use len() to print how many items are in this list.
# dna_sequences = ["ATGC", "GCTA", "TTAG", "CCGA"]
#============================================================

dna_sequences = ["ATGC", "GCTA", "TTAG", "CCGA"]
print(len(dna_sequences))

#============================================================
# TASK 5: Print the length of the second sequence.
# dna_sequences = ["ATGC", "GCTAGG", "TTAG"]
#============================================================

dna_sequences = ["ATGC", "GCTAGG", "TTAG"]
print(len(dna_sequences[1]))

#============================================================
# TASK 6: Use append() to add "CCGA" to the end and print the updated list.
# Do not put append() inside print().
# dna_sequences = ["ATGC", "GCTAGG", "TTAG"]
#============================================================

dna_sequences = ["ATGC", "GCTAGG", "TTAG"]
dna_sequences.append("CCGA")
print(dna_sequences)

#===============================================================
# TASK 7: Use insert() to insert "GCTA" at index 1. Print the updated list
# dna_sequences = ["ATGC", "TTAG", "CCGA"]
#===============================================================

dna_sequences = ["ATGC", "TTAG", "CCGA"]
dna_sequences.insert(1, "GCTA")
print(dna_sequences)

#================================================================
# TASK 8: Use remove() to remove the first occurrence of "GCTA".
# Print the updated list
# dna_sequences = ["ATGC", "GCTA", "TTAG", "CCGA"]
#================================================================

dna_sequences = ["ATGC", "GCTA", "TTAG", "CCGA"]
dna_sequences.remove("GCTA")
print(dna_sequences)

#================================================================
# TASK 9: Use pop(3) to remove the item at index 3. Print the updated list
# dna_sequences = ["ATGC", "GCTA", "TTAG", "CCGA"]
#================================================================

dna_sequences = ["ATGC", "GCTA", "TTAG", "CCGA"]
removed_sequence = dna_sequences.pop(3)
print(removed_sequence)
print(dna_sequences)

#================================================================
# TASK 10: Use index() to print the index of "TTAG"
# dna_sequences = ["ATGC", "GCTA", "TTAG", "CCGA"]
#================================================================

dna_sequences = ["ATGC", "GCTA", "TTAG", "CCGA"]
print(dna_sequences.index("TTAG"))

#================================================================
# TASK 11: Use count() to find how many times the exact item "ATGC" appears in this list. Print the count.
# dna_sequences = ["ATGC", "GCTA", "ATGC" "TTAG", "ATGC"]
#================================================================

dna_sequences = ["ATGC", "GCTA", "ATGC", "TTAG", "ATGC"]
print(dna_sequences.count("ATGC"))

#================================================================
# TASK 12: Compare remove() and pop().
# A. Remove the first occurrence of "GCTA" using remove(), then print.
# B. Reset the list to its original values.
# C. Use pop(4), then print the updated list.
# dna_sequences = ["ATGC", "GCTA", "TTAG", "CCGA", "GCTA"]
#================================================================

dna_sequences = ["ATGC", "GCTA", "TTAG", "CCGA", "GCTA"]
dna_sequences.remove("GCTA")
print(dna_sequences)
dna_sequences = ["ATGC", "GCTA", "TTAG", "CCGA", "GCTA"]
removed_sequence = dna_sequences.pop(4)
print(removed_sequence)
print(dna_sequences)