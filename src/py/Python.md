* Division by integer
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

