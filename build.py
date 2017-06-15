def solution(list_of_nums):
    """Enter Code Here"""
    even = 0
    odd = 0
    dic = {}
    for i in list_of_nums:
        if(i % 2 == 0):
            even = even + 1
        else:
            odd = odd + 1

    dic['ODD'] = odd
    dic['EVEN'] = even
    return dic

solution([1, 2, 3, 5, 8, 9])
