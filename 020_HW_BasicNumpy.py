from numpy import *

# Array Creation
# a.
array_1d = arange(10)
print("1D Array:", array_1d)

# b.
matrix_3x3 = arange(1, 10).reshape(3, 3)
print("\n3x3 Matrix:")
print(matrix_3x3)

# c.
random_integers = random.randint(50, 101, 10)
print("\n1D Array of 10 Random Integers between 50 and 100:", random_integers)

# d.
matrix_3x4 = random.rand(3, 4)
print("\n3x4 Matrix of Random Floating-point Numbers between 0 and 1:")
print(matrix_3x4)

# Array Indexing
# a.
even_numbers = array_1d[array_1d % 2 == 0]
print("\nEven Numbers from the 1D Array:", even_numbers)

# b.
second_row = matrix_3x3[1, :]
print("\nSecond Row from the 3x3 Matrix:")
print(second_row)

# c.
element_32 = matrix_3x3[2, 1]
print("\nElement at the Third Row and Second Column of the 3x3 Matrix:", element_32)

# d.
elements_gt_05 = matrix_3x4[matrix_3x4 > 0.5]
print("\nElements greater than 0.5 from the 3x4 Matrix:")
print(elements_gt_05)

# Basic Math Operations
# a.
A = random.randint(1, 11, (4, 4))
B = random.randint(1, 11, (4, 4))

sum_AB = A + B
product_AB = A * B
print("\nElement-wise Sum of A and B:")
print(sum_AB)
print("\nElement-wise Product of A and B:")
print(product_AB)

# b.
array_1d_times_5 = array_1d * 5
print("\n1D Array multiplied by 5:")
print(array_1d_times_5)

# c.
array_1d_minus_mean = array_1d - mean(array_1d)
print("\n1D Array subtracted by its mean:")
print(array_1d_minus_mean)

# Basic Statistical Calculations
# a.
mean_1d, median_1d, std_dev_1d = mean(array_1d), median(array_1d), std(array_1d)
print("\nMean, Median, and Standard Deviation of the 1D Array:")
print("Mean:", mean_1d, "Median:", median_1d, "Standard Deviation:", std_dev_1d)

# b.
min_value, max_value = min(matrix_3x4), max(matrix_3x4)
print("\nMinimum and Maximum Values of the 3x4 Matrix:")
print("Minimum:", min_value, "Maximum:", max_value)

# c.
min_index, max_index = argmin(random_integers), argmax(random_integers)
print("\nIndex of Minimum and Maximum Values in the 1D Array:")
print("Index of Minimum:", min_index, "Index of Maximum:", max_index)

# Bonus (Optional)
# a.
dot_product = dot(np.random.rand(5), random.rand(5))
print("\nDot Product of Two 1D Arrays of Length 5:", dot_product)

# b.
reshaped_matrix_1d = matrix_3x3.flatten()
print("\nReshaped 3x3 Matrix into a 1D Array of Length 9:")
print(reshaped_matrix_1d)
