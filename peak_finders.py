def peak_finder_basic(data):
    for i in len(data):
        if i == 0 and data[i] > data[i+1]: return i
        if i == len(data) and data[i] > data[i-1]: return i
        if data[i] > data[i-1] and data[i] >= data[i+1]: return i
    return None

# Divide and conquer
def peak_finder_dac(data):
    midpoint = len(data)//2
    first = data[:midpoint]
    second = data[midpoint:]
    result = peak_finder_basic(first)
    if result == None:
        result = peak_finder_basic(second)
    return result

def peak_finder_dac_recursive(data):
    mid = len(data)//2
    first = data[:mid]
    second = data[mid:]
    result = None
    if mid >= mid+1 and mid >= mid-1:
        return mid
    if mid - 1 > mid:
        result = peak_finder_dac_recursive(first)
    if result == None and mid + 1 > mid:
        result = peak_finder_dac_recursive(second)
    return None
    
#this should "direct" where to search
def peak_finder_dac_better(data):
    midpoint = len(data)//2
    test = [data[midpoint-1], data[midpoint], data[midpoint+1]]
    result = peak_finder_basic(test)
    first = data[:midpoint]
    second = data[midpoint:]
    if result != None and result > midpoint:
        result = peak_finder_basic(second)
    result = peak_finder_basic(first)
    if result == None:
        result = peak_finder_basic(second)
    return result

def peak_finder_2d_basic(data):
    width = len(data)
    col = data[i]
    height = len(col)
    for o in height:
        for i in width:
            if data[i][o] >= data[i+1][o]:
                if data[i][o] >= data[i-1][o]:
                    if data[i][o] >= data[i][o+1]:
                        if data[i][o] >= data[i][o-1]:
                            return i, o

def _check(data, start):
    x = start[0]
    y = start[1]
    if data[x][y] >= data[x+1][y]:
        if data[x][y] >= data[x-1][y]:
            if data[x][y] >= data[x][y+1]:
                if data[x][y] >= data[x][y-1]:
                    return [x,y]
                else:
                    return [x, y-1]
            else:
                return [x, y+1]
        else:
            return [x-1,y]
    else:
        return [x+1, y]

def peak_finder_2d_smarter(data): # how would you even calc the complexity of this?
    start = [0,0]
    peak = None
    while peak == None:
        result = _check(data, start)
        if result == start:
            peak = result
        else:
            start = result


def _get_array_max(data):
    max = 0
    for i in len(data):
        if data[i] > data[max]:
            max = i
    return max

def peak_finder_2d_dac(data):
    mid = len(data)//2
    first = data[:mid]
    second = data[mid:]
    mid_max = _get_array_max(data[mid])
    if data[mid -1, mid_max] > data[mid, mid_max]:
        peak_finder_2d_dac(first)
    elif data[mid +1, mid_max] > data[mid, mid_max]:
        peak_finder_2d_dac(second)
    else:
        return [mid, mid_max]


