import random

def calculate_compatibility():
    your_name = input("Enter your name: ")
    partner_name = input("Enter your partner's name: ")
    
    shared_interests = random.randint(0, 100)
    shared_values = random.randint(0, 100)
    communication = random.randint(0, 100)
    
    compatibility_score = (shared_interests + shared_values + communication) / 3
    
    print(f"Compatibility between {your_name} and {partner_name}: {compatibility_score:.2f}%")
    
    if compatibility_score >= 70:
        print("Congratulations! You have a relatively high compatibility score. Keep working on your relationship.")
    else:
        print("Compatibility is just one aspect of a relationship. Work on communication and understanding each other.")

if __name__ == "__main__":
    calculate_compatibility()
