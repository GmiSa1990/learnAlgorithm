
# bubble sort
def bubble_sort(lst, N):
	# lst: 列表，包含了N个元素
    for p in reversed(range(1,N)):
        flag = 0
        for i in range(p):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                flag = 1
        if flag:
            break
    return lst

# insertion sort
def insertion_sort(lst, N):
    for p in range(1,N):
        for i in reversed(range(p)):
            if lst[i] <= lst[p]:
                i += 1
                break
        lst[i], lst[i+1:p+1] = lst[p], lst[i:p]
    return lst

# shell sort
def shell_sort(lst, N):
    D = N // 2
    while D >= 1:
        # insertion sort
        for p in range(D, N):
            tmp = lst[p]
            for i in range(p-D,-1,-D):
                if lst[i] > tmp:
                    lst[i+D] = lst[i]
                else:
                    i = i + D
                    break
                lst[i] = tmp
        D = D // 2
    return lst

# shell sort
def shell_sort2(lst, N):
    D = [929, 505,209,109,41,19,5,1,0]
    idx = 0
    while D[idx] > N:
        idx += 1

    while D[idx] >= 1:
        # insertion sort
        D_cur = D[idx]
        for p in range(D_cur, N):
            tmp = lst[p]
            for i in range(p-D_cur,-1,-D_cur):
                if lst[i] > tmp:
                    lst[i+D_cur] = lst[i]
                else:
                    i = i + D_cur
                    break
                lst[i] = tmp
        idx += 1
    return lst

def heap_sort(lst, N):


if __name__ == "__main__":
    lst = [5,3,6,1,9,8,7,4,2]
    print(shell_sort2(lst, len(lst)))