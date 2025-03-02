# Given sets
aset = {'a', 'b', 'c', 'd', 'g', 'f'}
bset = {'l', 'm', 'o', 'h', 'c', 'b'}
cset = {'c', 'h', 'k', 'i', 'j', 'f', 'd'}

# Dictionary to store results
results = {}

# a. Number of elements in A and B (Union)
results["Number of elements in set A and B:"] = len(aset | bset)

# b. Number of elements in B that are not in A and C
results["Number of elements in B that are not in A and C:"] = len(bset - (aset | cset))

# c. Showing results using set operations

# Elements in C but not in A [h, i, j, k]
results["i. Elements in C but not in A:"] = sorted(cset - aset)

# Common elements in A and C [c, d, f]
results["ii. Common elements in A and C:"] = sorted(aset & cset)

# Elements in A and B, or in B and C [b, c, f]
results["iii. Elements in A and B, or in B and C:"] = sorted((aset & bset) | (bset & cset))

# Elements in both A and C but not in B [d, f]
results["iv. Elements in both A and C but not in B:"] = sorted((aset & cset) - bset)

# Elements common to all three sets [c]
results["v. Elements common to all three sets:"] = sorted(aset & bset & cset)

# Elements unique to B [l, m, o]
results["vi. Elements unique to B:"] = sorted(bset - (aset | cset))

# Print the results
for key, value in results.items():
    print(f"{key} {value}")
