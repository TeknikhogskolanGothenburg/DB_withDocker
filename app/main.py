from db import Base, engine, session
from models.users import User
from models.cars import Car
from models.parents import Parent
from models.children import Child


def add_user():
    user_name = input("Enter new user name: ")
    first_name = input("Enter new first name: ")
    last_name = input("Enter new last name: ")
    email = input("Enter new email: ")
    user = User(user_name=user_name, first_name=first_name, last_name=last_name, email=email)
    session.add(user)
    session.commit()


def show_all_users():
    users = session.query(User).all()
    for user in users:
        print(user)


def add_car():
    pass


def show_all_cars():
    pass


def show_all_parents():
    parents = session.query(Parent).all()
    for parent in parents:
        print(parent)


def show_all_children():
    children = session.query(Child).all()
    for child in children:
        print(child)


def main():
    Base.metadata.create_all(engine)

    running = True
    while running:
        print("Main Menu")
        print("=========\n")
        print("1. Add User")
        print("2. Show All Users")
        print("3. Add Car")
        print("4. Show All Cars")
        print("5. Show All Parents")
        print("6. Show All Children")
        print("9. Quit")

        selected = input("> ")
        if selected == "1":
            add_user()
        elif selected == "2":
            show_all_users()
        elif selected == "3":
            add_car()
        elif selected == "4":
            show_all_cars()
        elif selected == "5":
            show_all_parents()
        elif selected == "6":
            show_all_children()
        else:
            running = False


if __name__ == '__main__':
    main()