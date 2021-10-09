#Matrix row simplifier implementation.    Designed and Developed by : Mobin Nesari
def simplifier(mat):
    for i in range(len(mat)-1):
        row = mat[i]
        target_index = non_zero_finder(row)
        row = row_multiplier(row, 1 / row[target_index])
        mat[i] = row
        for j in range(0, len(mat)):
            if j != i:
                next_row = mat[j]
                two_row_negativator(next_row, row_multiplier_returner(row, next_row[i]))
                mat[j] = next_row    
    row = mat[len(mat) - 1]
    target_index = non_zero_finder(row)
    row = row_multiplier(row, 1 / row[target_index])
    mat[len(mat) - 1] = row
    for j in range(0, len(mat) - 1):
        next_row = mat[j]
        two_row_negativator(next_row, row_multiplier_returner(row, next_row[len(next_row) - 1]))
        mat[j] = next_row 

def row_multiplier(arr, coefficient):
    for i in range(len(arr)):
        arr[i] = arr[i] * coefficient
    return arr

def row_summator(arr, coefficient):
    for i in range(len(arr)):
        arr[i] = arr[i] + coefficient
    return arr

def row_negativator(arr, coefficient):
    for i in range(len(arr)):
        arr[i] = arr[i] - coefficient
    return arr

def row_divider(arr, coefficient):
    for i in range(len(arr)):
        arr[i] /= coefficient
    return arr

def two_row_summator(arr1, arr2):
    for i in range(len(arr1)):
        arr1[i] += arr2[i]
    return arr1

def two_row_negativator(arr1, arr2):
    for i in range(len(arr1)):
        arr1[i] -= arr2[i]
    return arr1

def row_multiplier_returner(arr, coefficient):
    answer = []
    for i in arr:
        answer.append(i * coefficient)
    return answer

def row_divider_returner(arr, coefficient):
    answer = []
    for i in arr:
        answer.append(i * coefficient)
    return answer

def non_zero_finder(arr):
    for i in range(len(arr)):
        if (arr[i] != 0):
            return i
    return -1

def print_matrix(mat):
    for i in range(len(mat)):
        print(mat[i])

m,n = [int(x) for x in input("Enter m and n:").split()]
mat = []
for i in range(m):
    row = []
    r = input("Enter row elements with a space between every element: ").split()
    for j in r:
        row.append(int(j))
    mat.append(row)
simplifier(mat)
print_matrix(mat)
