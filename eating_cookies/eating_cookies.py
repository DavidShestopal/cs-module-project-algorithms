'''
Input: an integer
Returns: an integer
'''


# def eating_cookies(n):
#     # Your code here
#     # base case
#     if n == 0:

#         return 1

#     if n < 0:

#         return 0

#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


def eating_cookies(n, cache=None):

    # first pass solution in class
    # base case no more cookies
    if n == 0:  # first we check if there are zero cookies left
        return 1

    elif n < 0:  # then we check if there is any negative amount of cookies
        return 0
    # after that we init the cache if we don't have it yet
    # and then add a case to check the cache
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = {i: 0 for i in range(n+1)}
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
