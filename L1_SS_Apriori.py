"""
Description     : Simple Python implementation of the Apriori Algorithm

Usage:
    $python apriori.py -f DATASET.csv -s minSupport  -c minConfidence
    python apriori.py -f dataset.csv

    $python apriori.py -f DATASET.csv -s 0.15 -c 0.6
"""

import sys

from itertools import chain, combinations
from collections import defaultdict
from optparse import OptionParser
import time

num_scan_times = 0


def subsets(arr):
    """ Returns non empty subsets of arr"""
    return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])


def returnItemsWithMinSupport(CandidateSet, transactionList, minSupport, freqSet, L1_transaction_dict: dict, mode):
    """
    Function:
        calculates the support for items in the itemSet and returns a subset
        of the itemSet each of whose elements satisfies the minimum support
    
    Args:
        CandidateSet: Candidate set C_k created by (k-1)-itemset L_k-1 
        transactionList: all the trasctions in the database
        minSupport: minimum support value
        freqSet: frequency of items in itemSet
        L1_transaction_dict: key is L1-item, value is the transaction id that contain the L1-item

    Returns:
        ItemSet: L_k itemset selected from C_k
    """
    global num_scan_times
    _itemSet = set()
    localSet = defaultdict(int)

    for idx, item in enumerate(CandidateSet):
        if mode == 'SS-Apriori':
            # 1. find the min item in the itemset
            min_item = min(item, key=lambda x: len(L1_transaction_dict[x]))

            # 2. only have to scan the transaction that contain the min item
            for transaction_idx in L1_transaction_dict[min_item]:
                num_scan_times += 1
                if item.issubset(transactionList[transaction_idx]):
                    freqSet[item] += 1
                    localSet[item] += 1
        else:
            # tradition Apriori
            for transaction in transactionList:
                num_scan_times += 1
                if item.issubset(transaction):
                    freqSet[item] += 1
                    localSet[item] += 1

    for item, count in localSet.items():
        support = float(count) / len(transactionList)

        if support >= minSupport:
            _itemSet.add(item)

    return _itemSet


def joinSet(itemSet, length):
    """Join a set with itself and returns the n-element itemsets"""
    return set(
        [i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length]
    )


def getItemSetTransactionList(data_iterator):
    transactionList = list()
    itemSet = set()
    L1_transaction_dict = dict()
    for idx, record in enumerate(data_iterator):
        transaction = frozenset(record)
        transactionList.append(transaction)
        for item in transaction:
            if item not in L1_transaction_dict:
                L1_transaction_dict[item] = set()
                L1_transaction_dict[item].add(idx)
            else:
                L1_transaction_dict[item].add(idx)
            itemSet.add(frozenset([item]))  # Generate 1-itemSets
    return itemSet, transactionList, L1_transaction_dict


def runApriori(data_iter, minSupport, minConfidence, mode):
    """
    run the apriori algorithm. data_iter is a record iterator
    Return both:
     - items (tuple, support)
     - rules ((pretuple, posttuple), confidence)
    """
    start = time.time()
    itemSet, transactionList, L1_transaction_dict = getItemSetTransactionList(data_iter)

    freqSet = defaultdict(int)
    largeSet = dict()
    # Global dictionary which stores (key=n-itemSets,value=support)
    # which satisfy minSupport

    oneCSet = returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet, L1_transaction_dict, mode)

    cnt = 0
    for item, transactions in L1_transaction_dict.items():
        if frozenset([item]) in oneCSet:
            cnt += len(transactions)
    print(f'additional transaction storage: {cnt}')


    currentLSet = oneCSet
    k = 2
    while currentLSet != set([]):
        largeSet[k - 1] = currentLSet
        currentCSet = joinSet(currentLSet, k)
        currentLSet = returnItemsWithMinSupport(
            currentCSet, transactionList, minSupport, freqSet, L1_transaction_dict, mode
        )
        k = k + 1
    
    end = time.time()
    print(f'Time elapse: {end - start}s')
    def getSupport(item):
        """local function which Returns the support of an item"""
        return float(freqSet[item]) / len(transactionList)
        # return freqSet[item]

    toRetItems = []
    for key, value in largeSet.items():
        toRetItems.extend([(tuple(item), getSupport(item)) for item in value])

    toRetRules = []
    for key, value in list(largeSet.items())[1:]:
        for item in value:
            _subsets = map(frozenset, [x for x in subsets(item)])
            for element in _subsets:
                remain = item.difference(element)
                if len(remain) > 0:
                    confidence = getSupport(item) / getSupport(element)
                    if confidence >= minConfidence:
                        toRetRules.append(((tuple(element), tuple(remain)), confidence))
    return toRetItems , toRetRules


def printResults(items, rules):
    """prints the generated itemsets sorted by support and the confidence rules sorted by confidence"""
    for item, support in sorted(items, key=lambda x: x[1]):
        print("item: %s , %.3f" % (str(item), support))
    # print("\n------------------------ RULES:")
    # for rule, confidence in sorted(rules, key=lambda x: x[1]):
    #     pre, post = rule
    #     print("Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence))


def to_str_results(items, rules):
    """prints the generated itemsets sorted by support and the confidence rules sorted by confidence"""
    i, r = [], []
    for item, support in sorted(items, key=lambda x: x[1]):
        x = "item: %s , %.3f" % (str(item), support)
        i.append(x)

    for rule, confidence in sorted(rules, key=lambda x: x[1]):
        pre, post = rule
        x = "Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence)
        r.append(x)

    return i, r


def dataFromFile(fname):
    """Function which reads from the file and yields a generator"""
    with open(fname, "r", encoding='utf-8') as file_iter:
        for line in file_iter:
            line = line.strip().rstrip(",")  # Remove trailing comma
            record = frozenset(line.split(","))
            yield record


if __name__ == "__main__":

    optparser = OptionParser()
    optparser.add_option(
        "-f", "--inputFile", dest="input", help="filename containing csv", default=None
    )
    optparser.add_option(
        "-s",
        "--minSupport",
        dest="minS",
        help="minimum support value",
        default=0.01,
        type="float",
    )
    optparser.add_option(
        "-c",
        "--minConfidence",
        dest="minC",
        help="minimum confidence value",
        default=0.6,
        type="float",
    )

    optparser.add_option(
        "-m",
        "--mode",
        dest="mode",
        help="mode to select itemset",
        default='SS-Apriori',
        type="str",
    )

    (options, args) = optparser.parse_args()

    inFile = None
    if options.input is None:
        inFile = sys.stdin
    elif options.input is not None:
        inFile = dataFromFile(options.input)
    else:
        print("No dataset filename specified, system with exit\n")
        sys.exit("System will exit")

    minSupport = options.minS
    minConfidence = options.minC
    mode = options.mode

    items, rules = runApriori(inFile, minSupport, minConfidence, mode)

    printResults(items, rules)

    print(f'number of scan times: {num_scan_times}')
