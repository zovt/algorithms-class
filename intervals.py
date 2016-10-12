import sys
from ast import literal_eval


def make_interval(start, end, unsorted_index):
    return {
            "start": start,
            "end": end,
            }


def parse_input():
    intervals = []
    for i, line in enumerate(sys.stdin):
        if line == 'q\n':
            return intervals

        tup = literal_eval(line.replace('\n', ''))
        intervals.append(make_interval(float(tup[0]), float(tup[1]), i))


def previous_dumb(intervals):
    for i, interval in enumerate(intervals):
        closest = -1
        cur_best_diff = float('inf')

        for j, other in enumerate(intervals):
            diff = intervals[i]['start'] - intervals[j]['end']

            if diff < cur_best_diff:
                if diff > 0:
                    closest = j
                    cur_best_diff = diff

        yield (i, closest)


def main():
    intervals = parse_input()
    res = list(previous_dumb(intervals))
    print('For input string: "q"')
    for indices in res:
        print("({}, {})".format(indices[0], indices[1]))


main()
