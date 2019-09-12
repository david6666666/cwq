def maxDiff(numbers):
    if numbers == None or len(numbers) <2:
        return 0
    min = numbers[0]
    maxdiff = numbers[1] - min
    for i in range(2,len(numbers)):
        if numbers[i-1] < min:
            min = numbers[i-1]
        currentdiff = numbers[i] - min
        if currentdiff > maxdiff:
            maxdiff = currentdiff
    return maxdiff
print(maxDiff([9,11,8,5,7,12,16,14]))