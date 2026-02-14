password = input ("Enter a strong password: ")
if len(password) < 8:
    print("Password must be at least 8 characters long.")


if (len(password) >=8   
    and any (char.isupper() for char in password)
    and any (char.islower()for char in password)
    and any (char.isdigit()for char in password)
    and any (not char.isalnum() for char in password)):
    print ("Password is strong")

elif (len(password) >= 8
    and any (char.isupper() for char in password)
    and any (char.islower()for char in password)
    and any (char.isdigit()for char in password)):
    print ("Password is medium")

elif (len(password) >= 8
    and any (char.isupper() for char in password)
    and any (char.islower()for char in password)
    and any (not char.isalnum() for char in password)):
    print ("Password is medium")

elif (len(password) >= 8
    and any(char.isupper() for char in password)
    and any(char.isdigit() for char in password)
    and any(not char.isalnum() for char in password)):
    print("Password is medium")

elif (len(password) >= 8
    and any(char.islower() for char in password)
    and any(char.isdigit() for char in password)
    and any(not char.isalnum() for char in password)):
    print("Password is medium")

elif (len(password) >= 8
      and any(char.isupper() for char in password)
      and any(char.islower() for char in password)):
    print("Password is weak")

elif (len(password) >= 8
      and any(char.isupper() for char in password)
      and any(char.isdigit() for char in password)):
    print("Password is weak")

elif (len(password) >= 8
      and any(char.isupper() for char in password)
      and any(not char.isalnum() for char in password)):
    print("Password is weak")

elif (len(password) >= 8
      and any(char.islower() for char in password)
      and any(char.isdigit() for char in password)):
    print("Password is weak")

elif (len(password) >= 8
      and any(char.islower() for char in password)
      and any(not char.isalnum() for char in password)):
    print("Password is weak")

elif (len(password) >= 8
      and any(char.isdigit() for char in password)
      and any(not char.isalnum() for char in password)):
    print("Password is weak")   