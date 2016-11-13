arr = [19,56,4,22,6,90,5,72]
def sort(arg):
    if len(arg) == 1:
        return arg
    else:
        mid = len(arg)/2
        left = sort(arg[0:mid])
        right = sort(arg[mid:])
        if (left == None) or (right == None): return
        if left[0] > right[0]:
            temp = left[0]
            left[0] = right[0]
            left.append(temp)
        else:
            left.append(right[0])
        print(left + right)
