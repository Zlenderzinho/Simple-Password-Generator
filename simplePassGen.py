import random, os, string

def CheckPasswordStrength(passwd):
    # Length Check
    lenScore = min(len(passwd) / 12, 1)

    # Variety Check
    hasUppercase = any(char.isupper() for char in passwd)
    hasLowercase = any(char.islower() for char in passwd)
    hasDigit = any(char.isdigit() for char in passwd)
    hasSpecial = any(not char.isalnum() for char in passwd)

    varietyScore = sum([hasUppercase, hasLowercase, hasDigit, hasSpecial]) / 4

    # Final Score
    strength = (lenScore + varietyScore) / 2
    return strength

def GeneratePassword(len, incUp, incLo, incDi, incPu):
    chars = ''

    # Set characters to use in the generation process
    if incUp:
        chars += string.ascii_uppercase
    if incLo:
        chars += string.ascii_lowercase
    if incDi:
        chars += string.digits
    if incPu:
        chars += string.punctuation
    
    if not chars:
        return 'No characters were selected for password generation'

    # Generate Password
    passwd = ''.join(random.choice(chars) for _ in range(len))
    return passwd

def main():
    os.system('cls')

    # Get Length of the Password
    pwdLen = int(input('Password Length: '))

    # Password Generation Settings
    includeUppercase = input('Include Uppercase Letters? (Y/N): ').upper() == 'Y'
    includeLowercase = input('Include Lowercase Letters? (Y/N): ').upper() == 'Y'
    includeDigits = input('Include Digits? (Y/N): ').upper() == 'Y'
    includePunctuation = input('Include Punctuation? (Y/N): ').upper() == 'Y'

    # Generate Password
    password = GeneratePassword(pwdLen, includeUppercase, includeLowercase, includeDigits, includePunctuation)
    
    # Strength Check
    passStrength = CheckPasswordStrength(password)
    if passStrength >= .75:
        outStrength = 'Strong Password'
    elif 0.5 <= passStrength < 0.75:
        outStrength = 'Moderately Strong Password'
    else:
        outStrength = 'Weak Password'

    # Print the generated password, its strength and the generation options
    os.system('cls')
    print(f'==================================\nSecurity: {outStrength}\nPassword: {password}\n==================================\n\tGeneration Options\n\nLength: {pwdLen}\nUppercase Characters: {includeUppercase}\nLowercase Characters: {includeLowercase}\nDigits: {includeDigits}\nPunctuation: {includePunctuation}')

if __name__ == '__main__':
    main()
