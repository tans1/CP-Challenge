def consecutiveCombo(arr1, arr2):
    combined = arr1 + arr2
    combined.sort()

    for i in range(len(combined) - 1):
        if combined[i] + 1 != combined[i + 1]:
            return False

    return True

def isExactlyThree(num):
    # brute force way
    if num <= 2:
        return False
    
    # every number (composite or prime) is divisible by itself or for 1
    for i in range(2,num-1):
        if num % i == 0:
            return True
    
    return False
    
def freqCount(nested_list, element):
    
    freq = {}
    def dfs(nst_list, level):
        if level not in freq:
            freq[level] = 0

        for item in nst_list:
            if isinstance(item, list):
                dfs(item, level + 1)
            elif item == element:
                freq[level] += 1

    dfs(nested_list, 0)

    max_level = max(freq.keys(), default=-1)
    result = [[i, freq.get(i, 0)] for i in range(max_level + 1)]
    return result
