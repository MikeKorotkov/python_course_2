def arithmetic_mean(a, b):
    two_num_res = (a + b) // 2
    print('Arithmetic mean of entered numbers is: ', two_num_res)
    counter = 0
    for i in range(a, b + 1):
        counter += 1
    all_num_sum = sum(range(a, b + 1))
    all_num_res = all_num_sum / counter
    print('Arithmetic mean of entered range is: ', all_num_res)


while True:
    first_num = int(input('Enter first number: '))
    second_num = int(input('Enter second number: '))
    arithmetic_mean(first_num, second_num)
