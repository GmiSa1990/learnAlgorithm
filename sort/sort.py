
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
        for p in range(D):
            for i in range(p,N,D):
                if lst[i] 


        D = D // 2
    return lst

def heap_sort(lst, N):
    pass

if __name__ == "__main__":
    lst = [5,3,6,1,9,8,7,4,2]
    print(insertion_sort(lst, len(lst)))