import torch

def main():
    #get input from the user
    userPass = input()

    #check length of password
    isLongEnough = lengthCheck(userPass)

    #check if it has a special character
    specialCharacter = hasSpecialCharacter(userPass)


def lengthCheck(passw):
    if len(passw) < 8:
        return False
    else:
        return True

def hasSpecialCharacter(passw):
    


if __name__ == "__main__":
    main()
