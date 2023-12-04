# birthday_wish.py

def personalized_birthday_wish(name):
    return f"Happy Birthday, {name}! 🎉🎂 Wishing you a fantastic day and an amazing year ahead!"

def main():
    recipient_name = input("Kiddoo: ")
    birthday_message = personalized_birthday_wish(recipient_name)
    print(birthday_message)

if __name__ == "__main__":
    main()
