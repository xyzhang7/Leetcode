## Common Usage
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

while number > 0:
    number, digit = divmod(number, 10)  # get each digit of number
```


* Package: timeit.repeat to count program's running time <br>


* Max/Min
```python
import heapq
k, array = 0, list()

MAX = float('inf')                          # = Integer.MAX_VALUE
k_smallest = heapq.nsmallest(k, array)      # find k smallest in array (详见source code)
```


* Iteration, Slice, Counter

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

from collections import Counter             # use Counter to count the frequency of each object/char/..
chars = Counter()
chars['a'] += 1                             # increment 
chars['a'] -= 1

>>> a = [1, 1, 2, 2, 3, 4]
>>> counter = Counter(a)                    # Directly convert a list to hashmap counter
>>> counter
Counter({1: 2, 2: 2, 3: 1, 4: 1})
>>> counter[10] > 0                         # Safe for invalid keys

from collections import defaultdict
count_word = defaultdict(int)               # = count_word = dict()
count_word["hello"] += 1                    # = if "hello" in count_word:
                                            #       count_word["hello"] += 1
                                            #   else:
                                            #       count_word["hello"] = 0

from collections import OrderedDict
dic = OrderedDict()                         # first in first out dict
val = dic.get(key)
if val is not None:                         # 不可以用 if val: pass 代替
    pass                                    # 因为 val 可能是 0, False 之类的值
dic.popitem(False)                          # First In First Out
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

## Data Structures
`heapq` *Min* heap
```python
import heapq

nums = [10, 50, 60, 20, 70]         # unordered data
heapq.heapify(nums)                 # nums -> heap
heapq.heappush(nums, 20)            # push new number to the heap nums         
```

`queue.PriorityQueue()` Concurrent *Min* Heap
uses the same `heapq` implementation internally and thus has the same time complexity. <br>
However, it is different in two key ways. <br>
Firstly, it is synchronized, so it supports concurrent processes (you can read more about here). <br>
Secondly, it is a class interface instead of the function based interface of heapq. <br>
Thus, PriorityQueue is the classic OOP style of implementing and using Priority Queues. <br>
* Use `min_q.put((val, object))` if val is unique, Otherwise, if val1 = val2, it will compare object, and return an error
* Or use `min_q.put((val, id(object), object))` is val is not unique
```python
from queue import PriorityQueue
min_q = PriorityQueue()  # Default is Min Queue
min_q.put(('a', node1))  # we can also put tuple, it is sorted by val of first element
min_q.put(('b', node2))
val, node = min_q.get()  # remove element from priority queue

max_q = PriorityQueue()
reverse = -1
max_q.put(reverse * val) # use some reverse to make Max Queue
val = max_q.get() * reverse
```

* `functools.lru_cache` as DP memo
```python
from functools import lru_cache
@lru_cache
def recur_with_memo():
    pass
```


## Functions
* Sort list (by keys) <br>
Sort list of tuple/ object by specific attribute 
```python
>>> student_tuples = [
...     ('john', 'A', 15),
...     ('jane', 'B', 12),
...     ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
>>> class Student:
...     def __init__(self, name, grade, age):
...         self.name = name
...         self.grade = grade
...         self.age = age
...     def __repr__(self):
...         return repr((self.name, self.grade, self.age))

>>> student_objects = [
...     Student('john', 'A', 15),
...     Student('jane', 'B', 12),
...     Student('dave', 'B', 10),
... ]
>>> sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```