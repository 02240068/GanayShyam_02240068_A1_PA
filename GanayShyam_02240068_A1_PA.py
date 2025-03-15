def is_prime(n):
    """Check if the number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

def sum_prime(x, y):
    """Return sum of prime numbers between x and y (inclusive)"""
    total = 0  
    for i in range(x, y + 1):
        if is_prime(i):
            total += i
    return total

def length_converter(value, direction):
    "convert meters to feet or feet to meters"
    if direction.upper() == 'M':
        print(value,"M==", round(value * 3.28084, 2)," F")
    elif direction.upper() == 'F':
        print(value,"F==",round(value/3.28084, 2)," M")
    else:
        print("Invalid conversion direction. Use 'M' or 'F'.")

def count_consonants(s):
    """Count the number of consonants in a string without using inbuilt functions."""
    consonants = [
        'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
        'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
    ]
   

    count = 0
    for i in s:
        if i in consonants:
            count+=1
    return count


def min_max_finder():
    """Find the smallest and largest number from a user-created list without built-in functions."""
   
    n = int(input("How many numbers do you want to enter? "))  
    
    if n <= 0:
        print("Invalid input. Enter at least one number.")
        return

    numbers = [] 

    for i in range(n):  
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    min_num = numbers[0]  
    max_num = numbers[0]  

    for num in numbers:  
        if num < min_num:  
            min_num = num  
        if num > max_num:  
            max_num = num  

    print(f"Smallest: {min_num}, Largest: {max_num}")

def is_palindrome(s):
    """Check if a string is a palindrome, ignoring spaces and case (convert everything to uppercase)."""
    
    cleaned = []
    for char in s:
        if char.isalpha(): 
            cleaned.append(char.upper()) 
    
    reversed_cleaned = cleaned.copy()
    reversed_cleaned.reverse()

    if cleaned == reversed_cleaned:
        return True  
    else:
        return False  


def word_counter(file_path):
    """Counts occurrences of specific words in a file without using regex."""
    
    target_words = {"the": 0, "was": 0, "and": 0}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                
                for word in words:
                    cleaned_word = "".join(char.lower() for char in word if char.isalnum())  
                
                    if cleaned_word in target_words:
                        target_words[cleaned_word] += 1
                        
    except FileNotFoundError:
        return "File not found."
    
    return target_words


while True:
    print("\nMenu:")
    print("1. Prime Number sum Calculator")
    print("2. Length unit Converter")
    print("3. Consonant Counter")
    print("4. Min-Max Number Finder")
    print("5. Palindrome Checker")
    print("6. Word Counter (from file)")
    print("7. Exit")
    
    choice = input("Select an option(1-7): ")
    
    if choice == "1":
        try:
            start = int(input("Enter start of range: "))
            end = int(input("Enter end of range "))
            print(f"Sum of primes between {start} and {end}: {sum_prime(start, end)}")
        except ValueError:
            print("invalid input. please enter integers.")
            
    elif choice == '2':
        value = float(input("Enter the length value: "))
        direction = input("Enter 'M' for meters to feet or 'F' for feet to meters: ")
        length_converter(value, direction)
        
        
    elif choice == '3':
        text = input("Enter text: ")
        print("Number of consonants: ", count_consonants(text))
        
    elif choice == '4':
        min_max_finder()
        
    elif choice == '5':
        text = input("Enter text: ")
        print("palindrome:", is_palindrome(text))
        
    elif choice == '6':
        file_path = input("Enter the path to the text file.")
        print("Word count:", word_counter(file_path))
        
    elif choice == '7':
        print("Exitng program. ")
        break
    else:
        print("Invalid selection. Please choose a valid option")
        


