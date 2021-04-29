num_lst = []
while True:
    enter_num = int(input('Enter your number: '))
    num_lst.append(enter_num)
    enter_more = input('Press Enter to enter another number or type "sort" to sort them: ')
    if enter_more == 'sort':
        print(sorted(num_lst))
