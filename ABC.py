import random

def calculate_compatibility():
    your_name = input("Enter your name: ")
    partner_name = input("Enter your partner's name: ")
    
    compatibility_score = random.randint(0, 100)
    
    print(f"Compatibility between {your_name} and {partner_name}: {compatibility_score}%")
    
    if compatibility_score >= 70:
        print("Congratulations! You have a high compatibility score. Maybe love is in the air!")
    else:
        print("Compatibility doesn't necessarily determine love, but you can still be great friends!")

if __name__ == "__main__":
    calculate_compatibility()
