import random

def generate_giftcard_code():
    # Generates a random 12-character alphanumeric gift card code
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    code = ''.join(random.choice(characters) for _ in range(12))
    return code

def is_valid_giftcard_code(code):
    # Check if the code is valid (for demonstration, all codes are considered valid)
    # You should replace this with your own validation logic
    return True

if __name__ == "__main__":
    while True:
        user_input = input("Enter a gift card code (q to quit): ").strip()
        
        if user_input.lower() == 'q':
            break
        
        if is_valid_giftcard_code(user_input):
            print(f"The gift card code '{user_input}' is valid.")
        else:
            print(f"The gift card code '{user_input}' is invalid.")
