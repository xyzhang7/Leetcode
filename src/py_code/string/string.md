# Compare Two Strings
## Method1
compare after sorting the two array

Example: group strings by anagram
```python
from typing import List
import collections
def groupAnagram(strs:List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)
    for s in strs:
        # we should convert sorted(s) List into tuple, so it will be hashable
        ans[tuple(sorted(s))].append(s)  
    return ans.values()
```