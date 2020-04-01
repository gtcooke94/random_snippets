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
