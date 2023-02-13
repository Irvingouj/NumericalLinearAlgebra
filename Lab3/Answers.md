# Problem2 
from the code, we can see, we have two for-loops
with in each for-loop, we do one row add operation, which is 
1 division, 1 deduction, and n addition
for set values on I, we do 1 division
so, for each for loop, we have 1+1+1+n operations

and we do that for $\sum_{i=n-1}^{1} i= \frac{(n)*(n-1)}{2} \in O(n^2)$

if we multiply them together, we will have
$\frac{(n)*(n-1)}{2} * (3+n) \in O(n^3)$

# Problem 3
1）when running the problem against the matrix, the problem is that top-left sub matrix with dimension 2 is singular, so the pricple minor of order k is zero

2）