# Given a sorted integer array without duplicates,
# return the summary of its ranges.
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

"""
[] -> []
[1] -> ["1"]
[1,2] -> ["1->2"]
[1,2,3] -> ["1->3"]
[1,2,3,5] -> ["1->3","5"]

"""


def summary(array):

    """
    Given a sorted integer array without duplicates,
     return the summary of its ranges.
    For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
    :param array: a sorted int array without duplicates
    :return: a str array with a summary of the ranges
    """

    if len(array) < 1:
        return array

    curr_summary = ""
    curr_number = array[0]
    summary_list = []

    curr_summary += curr_number.__str__()

    for index, number in enumerate(array):

        if index == len(array)-1:  # if its the last number

            if number == array[index-1]+1:  # if equals to the previous+1
                curr_summary += "->"+number.__str__()
                summary_list.append(curr_summary)

            else:                           # else not the number right after the previous
                summary_list.append(curr_summary)

        else:  # not the last number

            if number+1 == array[index+1]:  # if the next number is one more than the current
                curr_number = array[index+1]

            else:                           # not summary
                if index != 0:
                    if number-1 != array[index-1]:  # if its the number right after the prvo
                        curr_summary = curr_number.__str__()

                    else:
                        curr_summary += "->"+curr_number.__str__()

                summary_list.append(curr_summary)
                curr_number = array[index+1]
                curr_summary = ""
                curr_summary += curr_number.__str__()

        # print(summary_list)

    return summary_list


if __name__ == '__main__':
    result = summary([0, 1, 2, 4, 5, 7])
    result = summary([0, 1, 2, 4, 5, 9, 10])



