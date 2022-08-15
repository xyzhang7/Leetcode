* Bitwise operation
```python
x = 5
x // 2     # = int(x/2)
x << 1     # = x * 2
x << 1 | 1 # = x * 2 + 1
x ^ 1      # find sibling of node in binary tree (root idx = 1)
            # x   = 1 2 3 4 5 6 7 8 9 ...
            # x^1 = 0 3 2 5 4 7 6 9 8 ...
if (x & 1): pass      # odd number if x & 1 == 1; even otherwise
```

* Math Package
```python
from math import log2, ceil, floor
```

* Max/Min

```python
import heapq
k, array = 0, list()

MAX = float('inf')                          # = Integer.MAX_VALUE
k_smallest = heapq.nsmallest(k, array)      # find k smallest in array (详见source code)
```

* Iteration

```python
from itertools import product
m, n = 0, 0
for i, j in product(range(m), range(n)):    # = for i in range(m):
    pass                                    #       for j in range(n): 
    
```

* Char to Integer

```python
>>> chr(97)    # Convert char <--> ASCII value
'a'
>>> ord('a')
97

number = '10'  # convert from string/char to integer value
int(number)
```
