# DecodeLabs-Internship_RandomPassword_generator
# Random Password Generator

## Description
The Random Password Generator is a Python-based application developed as part of the DecodeLabs Python Internship Program. This project generates random passwords based on the length specified by the user. It uses Python's built-in `random` and `string` modules to create passwords containing letters and numbers.

## Features
- Generate random passwords instantly
- User-defined password length
- Uses uppercase and lowercase letters
- Includes numeric digits
- Input validation for positive password length
- Simple and beginner-friendly implementation

## Technologies & Tools Used
- Python 3
- Visual Studio Code(VS code)
- GitHub
  
## Modules Used
- Random Module (`random`)
- String Module (`string`)

## Source Code

```python
import random
import string

print("=== Random Password Generator ===")

length = int(input("Enter password length: "))

if length <= 0:
    print("Please enter a positive number.")
else:
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)
```

## How to Run

1. Install Python 3 on your system.
2. Save the code as `password_generator.py`.
3. Open Terminal or Command Prompt.
4. Navigate to the project folder.
5. Run the following command:

```bash
python password_generator.py
```

## Sample Output

```text
=== Random Password Generator ===
Enter password length: 8
Generated Password: A7kP2xQm
```

## Learning Outcomes
- Understanding Python modules
- Importing and using built-in libraries
- String manipulation
- User input handling
- Random password generation
- Basic input validation

## Future Enhancements
- Include special characters for stronger passwords.
- Add a password strength checker.
- Develop a graphical user interface (GUI) using Tkinter.
- Allow users to save generated passwords securely.
- Implement cryptographically secure password generation using the `secrets` module.
- Add options to customize password composition (letters, numbers, and symbols).

## Conclusion
This project successfully generates random passwords based on user-defined length. It demonstrates the use of Python modules, string manipulation, user interaction, and basic validation techniques while helping users create secure passwords.

---
### Developed as part of the DecodeLabs Python Internship Program
