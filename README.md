Pascal's Triangle
Overview
This Python script implements a function to generate Pascal's triangle up to a specified number of rows. Pascal's triangle is a triangular array of binomial coefficients, where each number is the sum of the two numbers directly above it.

Implementation
The pascal_triangle function takes a non-negative integer n as input, representing the number of rows to generate. It returns a list of lists, where each inner list represents a row of the triangle.

The algorithm follows these steps:

If n is less than or equal to 0, an empty list is returned.
The first row, containing only 1, is initialized.
A loop iterates from 1 to n-1 to generate subsequent rows.
Each new row starts and ends with 1.
The remaining elements of the row are calculated by summing adjacent elements from the previous row.
Usage
To use the pascal_triangle function:

Import the function from your script.
Call the function with the desired number of rows as an argument.
Python
from pascal_triangle import pascal_triangle

result = pascal_triangle(5)
print(result)
Use code with caution.

This will output:

[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
Time and Space Complexity
The time complexity of the pascal_triangle function is O(n^2), where n is the number of rows. The space complexity is also O(n^2) due to the storage of the generated triangle.
