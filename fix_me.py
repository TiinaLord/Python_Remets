def calculate_average(__nums__):
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
