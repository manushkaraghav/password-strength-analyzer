def password_checker(Password):
    Password = input("Enter the password: ")
    score = 0

    has_number = False
    has_upper = False
    has_lower = False
    has_symbol = False

    if len(Password) >= 9:
        score = score + 1
    else:
        print("Password should be greater than 9 characters")
    for i in Password:
        if i.isdigit():
            has_number = True
        if i.isupper():
            has_upper = True
        if i.islower():
            has_lower = True
        if i.isalnum() == False:
            has_symbol = True
    if has_number:
        score = score + 1
    else:
        print("Password should contain a number")
    if has_upper:
        score = score + 1
    else:
        print("Password should contain an uppercase letter")
    if has_lower:
        score = score + 1
    else:
        print("Password should contain a lowercase letter")
    if has_symbol:
        score = score + 1
    else:
        print("Password should contain a special character")
    print("Score:", score)
    if score <= 2: 
        strength = "Weak" 
    elif score == 3: 
        strength = "Medium" 
    elif score == 4:
         strength = "Strong" 
    else: 
        strength = "Very Strong"
    return { "score": score, "strength": strength, "length": len(Password), "has_upper": has_upper, "has_lower": has_lower, "has_number": has_number, "has_special": has_symbol }
password_info = password_checker("Password")
print(password_info)