import re

def assess_password_strength(password):
    strength_criteria = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digits': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    
    score = sum(strength_criteria.values())
    
    feedback = []
    if not strength_criteria['length']:
        feedback.append("Password should be at least 8 characters long.")
    if not strength_criteria['uppercase']:
        feedback.append("Password should contain at least one uppercase letter.")
    if not strength_criteria['lowercase']:
        feedback.append("Password should contain at least one lowercase letter.")
    if not strength_criteria['digits']:
        feedback.append("Password should contain at least one digit.")
    if not strength_criteria['special']:
        feedback.append("Password should contain at least one special character.")
    
    return score, feedback

def main():
    print("Password Strength Checker")
    while True:
        password = input("Enter a password to assess: ")
        score, feedback = assess_password_strength(password)
        
        strength_levels = {
            5: "Very Strong",
            4: "Strong",
            3: "Moderate",
            2: "Weak",
            1: "Very Weak",
            0: "Extremely Weak"
        }
        
        print(f"Password Strength: {strength_levels.get(score, 'Undefined')}")
        if feedback:
            print("Feedback to improve your password:")
            for f in feedback:
                print(f"- {f}")

        if score >= 4:
            print("Successfully set strong password")
            break

        another = input("Do you want to try to make a stronger password? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()