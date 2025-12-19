from secrets import choice

def getsecretint (iterations, amount_of_numbers):
    dict_num = {}
    num_array = []
    num_iterations = iterations
    num_amount = amount_of_numbers
    check = 1
    check_portion = num_iterations/4

    for num in range(num_amount):
        num_array.append(num+1)

    for i in range(num_iterations):
        
        random_number = choice(num_array)

        if random_number in dict_num:
            dict_num[random_number] += 1
        else:
            dict_num[random_number] = 1

        if i == round(check_portion*check):
            print(f"secret lib: {check}/4")
            check += 1
    
    print(f"secret lib: Done")

    return dict_num

