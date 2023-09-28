def random_password_generator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like to use in your password? : "))
    nr_symbols = int(input("How many symbols would you like to use? : "))
    nr_numbers = int(input("How many numbers would you like to use? : "))
    
    total = int(nr_letters + nr_symbols + nr_numbers)

    chosen_letters = []
    for i in range(nr_letters):
        choose_letter = random.choice(letters)
        chosen_letters.append(choose_letter)
        
        
    chosen_numbers= []
    for x in range(nr_numbers):
        choose_number = random.choice(numbers)
        chosen_numbers.append(choose_number)

    chosen_symbols = []
    for y in range(nr_symbols):
        choose_number = random.choice(symbols)
        chosen_symbols.append(choose_number)

    _all = chosen_letters + chosen_numbers + chosen_symbols
    print(_all)
    
    random.shuffle(_all)
    
    password = "".join(_all)
    print(password)

def main():
    random_password_generator()

main()
