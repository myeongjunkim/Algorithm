
def pairSum(arr, target_sum):
    result_arr = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                if arr[j]>=0:
                    result_s = str(arr[i]) + "+" + str(arr[j])
                else:
                    result_s = str(arr[i]) + str(arr[j])
                result_arr.append(result_s)
    return result_arr

result = pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7)
print(result)