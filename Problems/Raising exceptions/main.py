class NegativeSumError(Exception):
    pass


def sum_with_exceptions(a, b):
    sum_ = a + b
    if sum_ >= 0:
        return sum_
    else:
        raise NegativeSumError
