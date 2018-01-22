# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Given a collection of intervals which are already sorted by start number, merge all overlapping intervals.
# For example,
# Given [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]],
# return [[1, 10], [11, 18], [19, 22]]


def merge_intervals(intervals):

    start = intervals[0][0]
    end = intervals[0][1]
    lst = []

    for i, v in enumerate(intervals):
        if i == 0:
            continue

        if v[0] <= end:
            end = v[1]
            if i == len(intervals)-1:
                lst.append([start, end])
        else:
            lst.append([start, end])
            start = v[0]
            end = v[1]
            if i == len(intervals) - 1:
                lst.append([start, end])

        # print(f"start:{start} end:{end} lst:{lst}")
    return lst


if __name__ == '__main__':
    lst = [[1, 3],[2, 6],[5, 10],[11, 16],[15,18],[19,22]]
    result = merge_intervals(lst)
    print(result)