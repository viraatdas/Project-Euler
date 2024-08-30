# 4,000,000

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

fib_arr = [1,2]
def fib(n):
    global fib_arr


    while len(fib_arr) < n+1:
        fib_arr.append(0)
    
    if n <= 1:
        return n
    else:
        if fib_arr[n-1] == 0:
            fib_arr[n-1] = fib(n-1)
        if fib_arr[n-2] == 0:
            fib_arr[n-2] = fib(n-2)
    
    fib_arr[n] = fib_arr[n-2] + fib_arr[n-1]
    return fib_arr[n]

fib(35)

sum_el = 0
for i in range(1, len(fib_arr), 3):
    if fib_arr[i] > 4000000:
        break
    sum_el+= fib_arr[i]

print(sum_el)
# 1,2,3,5,8