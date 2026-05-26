# Password-strength-analyzer
A simple Python-based password strength checker that analyzes a password and determines whether it is strong based on common security criteria.

## Features

* Checks password length
* Checks for uppercase letters
* Checks for lowercase letters
* Checks for numbers
* Checks for special characters
* Assigns a strength score

## How It Works

The program evaluates a password using the following criteria:

* Minimum length of 9 characters
* At least one uppercase letter
* At least one lowercase letter
* At least one number
* At least one special character

Based on these checks, a score is calculated and the password is classified according to its strength.

## Requirements

* Python 3.x

No external libraries are required.

## Running the Program

1. Download or clone the repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python password_checker.py
```

## Example

```text
Enter the password: Hello123!
Score: 5
{'score': 5, 'strength': 'Very Strong', 'length': 9, 'has_upper': True, 'has_lower': True, 'has_number': True, 'has_special': True}
```

## Purpose

This project was created as a beginner Python project to practice:

* Variables
* Conditional statements
* Loops
* String methods
* Basic program design

## Future Improvements

* Graphical user interface (GUI) using Tkinter
* Password strength percentage
* Password generation feature
* Exporting results to a file

## Author

Manushka Raghav

```
```
