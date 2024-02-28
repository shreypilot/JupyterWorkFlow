def my_map(my_func, my_list):
    result = []
    for item in my_list:
        result.append(my_func(item))
    return result

nums = [3,4,5,6,7]

cubed = my_map(lambda x: x**3, nums)
print(cubed)