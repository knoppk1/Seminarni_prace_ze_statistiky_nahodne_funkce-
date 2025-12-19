from random import randint

def getrandomint (iterations, amount_of_numbers):
    dict_num = {}
    num_iterations = iterations
    num_amount = amount_of_numbers
    check = 1
    check_portion = num_iterations/4

    for i in range(num_iterations):
        
        random_number = randint(1,num_amount)
        if random_number in dict_num:
            dict_num[random_number] += 1
        else:
            dict_num[random_number] = 1

    
        if i == round(check_portion*check):
            print(f"random lib: {check}/4")
            check += 1
    
    print(f"random lib: Done")

    return dict_num




        