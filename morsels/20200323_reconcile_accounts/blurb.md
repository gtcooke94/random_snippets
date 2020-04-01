Base solution

The naive solution would be to do a
```
for item in list1:
    for item in list2:
         do things
```

This is `O(n^2)`. We can definitely do better.


Make things sets, so the `in` operation is `O(1)` instead of `O(n)`

```
def reconcile_accounts(translist_1, translist_2):
    transset_1 = {tuple(transaction): None for transaction in translist_1}
    transset_2 = {tuple(transaction): None for transaction in translist_2}
    append_missing_1 = transset_1.keys() - transset_2.keys()
    append_missing_2 = transset_2.keys() - transset_1.keys()
    result_1 = [build_result(transaction, append_missing_1) for transaction in transset_1.keys()]
    result_2 = [build_result(transaction, append_missing_2) for transaction in transset_2.keys()]
    return result_1, result_2


def build_result(transaction, append_missing):
    trans_list = list(transaction)
    trans_list.append("MISSING" if transaction in append_missing else "FOUND")
    return trans_list
```


To do the second part, we had to allow for duplicate transaction and match the earlier ones in the lists first
After some pain, I came up with the below. Get the `skip` dict for each set of transactions. These represent the "FOUND" transactions. Subtract one from this as you go through. If the value in this for a transction is 0, the transaction is missing.
```
from collections import Counter
def reconcile_accounts(translist_1, translist_2):
    translist_1 = [tuple(transaction) for transaction in translist_1]
    translist_2 = [tuple(transaction) for transaction in translist_2]
    trans_counter1 = Counter(translist_1)
    trans_counter2 = Counter(translist_2)
    append_missing_1 = trans_counter1 - trans_counter2
    append_missing_2 = trans_counter2 - trans_counter1
    skip1 = trans_counter1 - append_missing_1
    skip2 = trans_counter2 - append_missing_2
    result_1 = [build_result(transaction, skip1) for transaction in translist_1]
    result_2 = [build_result(transaction, skip2) for transaction in translist_2]
    return result_1, result_2


def build_result(transaction, not_missing):
    """
    MODIFIES not_missing 
    """
    trans_list = list(transaction)
    if not_missing[transaction] != 0:
        not_missing[transaction] -= 1
        trans_list.append("FOUND")
    else:
        trans_list.append("MISSING")
    return trans_list
```

Second bonus is to allow a slip of 1 day in either direction.
First thought: subclass python's `date` to allow equality within one day. However, everything above depends on hashes of tuples, because I'm using sets and maps. And you can't make the hash for a date be equal to the value one greater and one lower than it, because then every date would hash to the same value.

His solution is stored in `solution.py`. He took the approach of making a function that created a duplicate record with the 3 dates, doing some extra sorting before, and keeping counters. This allowed him to keep using the dict/hash/counter approach.
