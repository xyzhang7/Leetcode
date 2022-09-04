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

* Package: Math
```python
from math import log2, ceil, floor
int(1e10) == 10 ** 10       # 10^10
```

* Package: functools.lru_cache as DP memo
```python
from functools import lru_cache
@lru_cache
def recur_with_memo():
    pass
```

* Package: timeit.repeat to count program's running time

* Max/Min

```python
import heapq
k, array = 0, list()

MAX = float('inf')                          # = Integer.MAX_VALUE
k_smallest = heapq.nsmallest(k, array)      # find k smallest in array (详见source code)
```

* Iteration and Slice

```python
from itertools import product
m, n = 0, 0
for i, j in product(range(m), range(n)):    # = for i in range(m):
    pass                                    #       for j in range(n): 
    
arr = [1, 2, 3, 4]                          # given a string/list/tuple, slice the object in the reverse order
a = '1234'                                  # and the slice will just take a copy of each original element
arr[::-1]                                   # modify the slice will not change the original object
a[::-1]

board = [[0] * 10 for _ in range(10)]       # = if board[i][j] == 'S' or board[i][j] == 'X' and ...
if board[i][j] in 'SXE':                    # given a board of characters, it's Start position is 'S'
    pass                                    # and its end position is 'E', obstacle is 'X'                                                                          
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
