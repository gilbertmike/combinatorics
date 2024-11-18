from collections.abc import Callable, Sequence


def dependent_product(spaces: Sequence[Callable]):
    """
    Creates the product of the spaces that are constructed using the
    yielded value of the last space.

    For example, if spaces is [s0, s1, s2], then the resulting generator
    is equivalent to the following.
    ```
    for result0 in s0():
        for result1 in s1(*result0):
            for result2 in s2(*result1):
                yield result2
    ```
    """
    iterators = [iter(spaces[0]())] + [iter(range(0))]*(len(spaces)-1)

    cur_idx = len(spaces)-1
    while True:
        try:
            intermediate_result = next(iterators[cur_idx])
            if cur_idx < len(spaces)-1:
                cur_idx += 1
                if isinstance(intermediate_result, tuple):
                    new_iter = iter(spaces[cur_idx](*intermediate_result))
                else:
                    new_iter = iter(spaces[cur_idx](intermediate_result))
                iterators[cur_idx] = new_iter
            else:
                assert cur_idx == len(spaces) - 1
                yield intermediate_result
        except StopIteration as e:
            if cur_idx > 0:
                cur_idx -= 1
            else:
                assert cur_idx == 0
                return
