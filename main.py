from src.pass_gen import password_generator


if __name__ == "__main__":
    min_lenght = int(input("Enter the minimum length:"))
    number = input("Do you want to have number (y/n)?:").lower() == 'y'
    special_character = input("Do you want to have special characters (y/n)?:").lower() == 'y'

    my_pass = password_generator(min_lenght, number , special_character)
    print(my_pass)
