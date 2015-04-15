a = [36, 5, 12, 9, 21]
print 'array sorted: '
print sorted(a)
print '\n'

def revert_sort(x, y):
    if x > y:
        return -1
    elif x < y:
        return 1
    else:
        return 0
print 'array revert_sort:'
print sorted(a, revert_sort)
print '\n'



