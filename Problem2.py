def numadd(n):
    previous_num = 0
    for i in range(0, n):
        x_sum = previous_num + i
        print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
        previous_num = i
        

numadd(10)
    