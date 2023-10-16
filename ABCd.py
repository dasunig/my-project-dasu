import random

def calculate_relationship_strength():
    your_name = input("Enter your name: ")
    partner_name = input("Enter your partner's name: ")
    
    shared_interests = random.randint(0, 100)
    shared_values = random.randint(0, 100)
    communication = random.randint(0, 100)
    
    compatibility_score = (shared_interests + shared_values + communication) / 3
    
    print(f"Compatibility between {your_name} and {partner_name}: {compatibility_score:.2f}%")
    
    relationship_strength = compatibility_score + random.randint(-20, 20)  # Simulating relationship strength
    
    print(f"Relationship Strength: {relationship_strength:.2f}%")
    
    divorce_probability = max(0, min(100, (100 - relationship_strength)))
    
    print(f"Probability of Divorce: {divorce_probability:.2f}%")
    
    if relationship_strength >= 70:
        print("Congratulations! Your relationship is strong. Keep nurturing it.")
    else:
        print("Remember, compatibility and relationship strength are not guarantees. Open communication and mutual effort are essential.")

if __name__ == "__main__":
    calculate_relationship_strength()
