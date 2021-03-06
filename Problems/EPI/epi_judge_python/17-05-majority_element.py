from test_framework import generic_test


def majority_search(stream):
    candidate, candidate_count = None, 0
    for s in stream:
        if candidate_count == 0:
            candidate, candidate_count = s, candidate_count + 1
        elif candidate == s:
            candidate_count += 1
        else:
            candidate_count -= 1

    return candidate


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("17-05-majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
