'''
Input: a List of integers
Returns: a List of integers
'''


# def product_of_all_other_numbers(arr):
#     # Your code here
#     results = []

#     for index, number in enumerate(arr):
#         product = 1
#         excluding_current = arr[:index] + arr[index + 1:]
#         for number in excluding_current:
#             product *= number
#         results.append(product)
#     return results


def product_of_all_other_numbers(arr):

    new_array = [1]
    length = len(arr)

    # Run forwards through the list muliplying by the cumulative product of the elements before
    running_product = 1
    for i in arr[:-1]:
        running_product *= i
        new_array.append(running_product)

    pass
    # Run backwards though the list multiplying by the cumulative product of the elements after
    running_product = 1
    for i in range(length-1, 0, -1):
        running_product *= arr[i]
        new_array[i - 1] *= running_product

    return new_array


print(product_of_all_other_numbers([1, 7, 3, 4]))


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
