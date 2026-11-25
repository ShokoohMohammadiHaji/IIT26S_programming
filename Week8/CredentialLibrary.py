
import hashlib
import csv


CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hashPassword(PPassword: str) -> str:
    result = hashlib.md5(PPassword.encode())
    return result.hexdigest()


def readCredentials():
    Users = []

    try:
        file = open(CREDENTIALS_FILE, "r")
        reader = csv.reader(file, delimiter=DELIMITER)

        for Row in reader:
            if len(Row) == 3:
                Users.append(Row)

        file.close()

    except FileNotFoundError:
        pass

    return Users


def registerUser(PUsername: str, PPassword: str) -> None:
    Users = readCredentials()

    UserID = len(Users)
    PasswordHash = hashPassword(PPassword)

    file = open(CREDENTIALS_FILE, "a", newline="")
    writer = csv.writer(file, delimiter=DELIMITER)

    writer.writerow([UserID, PUsername, PasswordHash])

    file.close()
    return None


def authenticateUser(PUsername: str, PPassword: str):
    Users = readCredentials()
    PasswordHash = hashPassword(PPassword)

    for User in Users:
        if User[1] == PUsername and User[2] == PasswordHash:
            return User

    return None
