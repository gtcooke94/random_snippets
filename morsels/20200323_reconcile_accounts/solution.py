from collections import Counter
from datetime import datetime, timedelta


def row_with_status(row, found):
    if found:
        return [*row, 'FOUND']
    else:
        return [*row, 'MISSING']


def surrounding(transaction):
    """Return the row key with date shifted by 1 on either side."""
    date_string, *rest = transaction
    date = datetime.strptime(date_string, '%Y-%m-%d').date()
    return [
        (str(date+timedelta(days=i)), *rest)
        for i in [-1, 0, 1]
    ]


def get_matches(to_search_for, search_in):
    """Return dictionary of each row and its successful matches."""
    groups = Counter(search_in)
    matches = Counter()
    for row in sorted(to_search_for):
        for key in surrounding(row):
            if groups[key]:
                matches[row] += 1
                groups[key] -= 1
                break
    return matches


def reconcile_accounts(transactions1, transactions2):
    """Return both transaction lists with FOUND/MISSING status added."""
    transactions1 = [tuple(r) for r in transactions1]
    transactions2 = [tuple(r) for r in transactions2]
    matches1 = get_matches(transactions1, transactions2)
    new1 = []
    for row in transactions1:
        new1.append(row_with_status(row, found=matches1[row] > 0))
        matches1[row] -= 1
    matches2 = get_matches(transactions2, transactions1)
    new2 = []
    for row in transactions2:
        new2.append(row_with_status(row, found=matches2[row] > 0))
        matches2[row] -= 1
    return new1, new2
