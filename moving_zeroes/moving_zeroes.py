'''
Input: a List of integers
Returns: a List of integers
'''


# def moving_zeroes(arr):
#     # Your code here

#     altered = [number for number in arr if number != 0]
#     zero = [number for number in arr if number is 0]
#     altered.extend(zero)
#     return altered


def moving_zeroes(arr):
    index = 0
    new_array = []
    end = len(arr)
    while index < end:
        number = arr[index]
        if number == 0:  # if the number at this index is zero we move it to the end
            # At the end (len(arr)) of the new_array, insert 0
            new_array.insert(end, 0)
        else:  # otherwise
            # At the beginning (new_array[0]), insert the number
            new_array.insert(0, number)
        index += 1
    return new_array


print(moving_zeroes([0, 3, 1, 0, -2]))
print(moving_zeroes([4, 2, 1, 5]))
if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
