def merge(a, b):
    list(a)
    list(b)
    c = []
    i = 0
    j = 0
    while True:
        if i >= len(a):
            c += list(b[j:b[-1]])
            break

        if j >= len(b):
            c += list(a[i:a[-1]])
            break

        if a[i] < b[j]:
            c.append(a[i])
            i += 1

        else:
            c.append(b[j])
            j += 1

    return c

arr = []
s = input()
arr = s.split('=')
print(eval(arr[1]))

