def get_element_counts(input_list):
    """
    For each unique element in the list, counts the number of occurrences of the element.
    :param input_list: An iterable of some sort with immutable data types
    :return: A dictionary where the keys are the elements and the values are the corresponding
             number of occurrences.
    """

    unique_elements = set(input_list)
    elem_counts = {}
    for elem in unique_elements:
        elem_counts[elem] = count_element(input_list, elem)

    return elem_counts


def count_element(input_list, target):
    """
    Given a list and a target, counts how many times the target element occurs in the input list.
    :param input_list: An iterable of some sort
    :param target: An immutable data type
    :return: A non-negative integer
    """

    count = 0
    for elem in input_list:
        if elem == target:
            count += 1

    return count
