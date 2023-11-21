from operator import mul
from operator import mod
from operator import ifloordiv
# def falling(n, k):
#     """Compute the falling factorial of n to depth k.
#
#     >>> falling(6, 3)  # 6 * 5 * 4
#     120
#     >>> falling(4, 3)  # 4 * 3 * 2
#     24
#     >>> falling(4, 1)  # 4
#     4
#     >>> falling(4, 0)
#     1
#     """
#     "*** YOUR CODE HERE ***"
#     if k == 0:
#         return 1
#
#     count = 1
#     product = n
#     for i in range(k-1):
#         if count <= k:
#             product = mul(product, n - count)
#         count += 1
#
#     return product
#
# print(falling(6,3))

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    y = 1
    while n:
        right_digit = n % 10
        n = n // 10
        left_digit = n % 10

        # right_digit = n % mul(10, y)
        # y = mul(10, y)
        # left_digit = ifloordiv(n % mul(10, y),y)
        if right_digit == left_digit == 8:
            return True
    return False
