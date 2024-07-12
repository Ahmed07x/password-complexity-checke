import re

def password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None  # \W matches any non-word character
    
    # Count the number of criteria met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])
    
    # Assess strength
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return {
        "length": length_criteria,
        "uppercase": uppercase_criteria,
        "lowercase": lowercase_criteria,
        "number": number_criteria,
        "special": special_criteria,
        "strength": strength
    }

def password_feedback(result):
    feedback = []
    if not result["length"]:
        feedback.append("Password should be at least 8 characters long.")
    if not result["uppercase"]:
        feedback.append("Password should contain at least one uppercase letter.")
    if not result["lowercase"]:
        feedback.append("Password should contain at least one lowercase letter.")
    if not result["number"]:
        feedback.append("Password should contain at least one number.")
    if not result["special"]:
        feedback.append("Password should contain at least one special character.")
    return feedback

def main():
    password = input("Enter a password to check its strength: ")
    result = password_strength(password)
    print(f"Password Strength: {result['strength']}")
    feedback = password_feedback(result)
    if feedback:
        print("Suggestions to improve your password:")
        for f in feedback:
            print(f"- {f}")

if __name__ == "__main__":
    main()
