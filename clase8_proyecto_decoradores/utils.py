import os

import csv
import re


def get_users(file_name: str) -> list:
    """
    Read a csv file with all the users of the application and return them as a list of dictionaries.
    :param file_name: str
    :return: list
    """
    with open(f"{os.path.dirname(__file__)}/{file_name}", "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    return data


def authenticate(username: str, pwd: str) -> bool:
    """
    Validate if a user exist in the users file.
    :param username: str
    :param pwd: str
    :return: boolean
    """
    user = {
        "username": username,
        "password": pwd
    }
    all_users = get_users("users.csv")
    if user in all_users:
        return True
    else:
        return False


def is_valid_password(pwd: str) -> bool:
    """
    Checks if the inputted password follows the next conditions:
    - At least 8 characters
    - Must be restricted to, though does not specifically require any of:
        - uppercase letters: A-Z
        - lowercase letters: a-z
        - numbers: 0-9
        - any of the special characters: @#$%^&+=
    :param pwd: string
    :return: boolean
    """
    if re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", pwd):
        return True
    else:
        return False
