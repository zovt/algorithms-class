import math
import sys
from ast import literal_eval


def make_interval(start, end, unsorted_index):
    return {
            "start": start,
            "end": end,
            "unsorted_index": unsorted_index,
            }


def parse_input():
    intervals = []
    for i, line in enumerate(sys.stdin):
        if line == 'q\n':
            return intervals

        tup = literal_eval(line.replace('\n', ''))
        intervals.append(make_interval(float(tup[0]), float(tup[1]), i))


def previous_dumb(intervals):
    comparisons = 0
    for i, interval in enumerate(intervals):
        closest = -1
        cur_best_diff = float('inf')

        for j, other in enumerate(intervals):
            diff = intervals[i]['start'] - intervals[j]['end']

            comparisons += 1
            if diff < cur_best_diff:
                comparisons += 1
                if diff > 0:
                    closest = j
                    cur_best_diff = diff

        yield (i, closest)
    yield comparisons


def previous_smart(intervals):
    comparisons = 0

    def merge(l1, l2, comparator):
        nonlocal comparisons
        comparisons += 1
        if len(l1) == 0:
            return l2

        el1 = l1[0]
        el2 = l2[0]

        comparisons += 1
        if comparator(el1, el2) < 0:
            return [el1] + merge(l1[1:], l2, comparator)
        else:
            return [el2] + merge(l2[1:], l1, comparator)

    def merge_sort(xs, comparator):
        nonlocal comparisons
        length = len(xs)

        comparisons += 1
        if (length <= 1):
            return xs

        first = xs[:math.floor(length / 2)]
        second = xs[math.floor(length / 2):]

        return merge(merge_sort(first, comparator), merge_sort(second, comparator), comparator)

    def comparator(int1, int2):
        nonlocal comparisons
        comparisons += 1
        return (-1 if int1['end'] <= int2['end'] else 1)

    def find_closest(interval, intervals, ind = 0):
        if len(intervals) == 1:
            print(ind)
            return ind
        
        half = math.floor(len(intervals) / 2)
        print(half)
        print(ind)
        if (interval['end'] >= intervals[half]['start']):
            print('left')
            return find_closest(interval, intervals[half:], ind)
        else:
            print('right')
            return find_closest(interval, intervals[:half], ind + half)
        
        
    
    sorted = merge_sort(intervals, comparator)

    for i, interval in enumerate(intervals):
        print('-------------------------')
        closest = find_closest(interval, sorted)

        yield (i, sorted[closest]['unsorted_index'])
    yield comparisons


def main():
    intervals = parse_input()
    print(list(previous_dumb(intervals)))
    print(list(previous_smart(intervals)))


main()
