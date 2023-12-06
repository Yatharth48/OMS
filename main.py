from Auth import login, register, logout
from organisation import add_employee, list_employees, add_department, list_departments, current_user

def main():
    while True:
        print("\nWelcome to the Organization Management System")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login(username, password):
                user_menu()
            else:
                print("Invalid credentials. Try again.")
        elif choice == '2':
            register()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu():
    while True:
        print("\nUser Menu")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Add Department")
        print("4. List Departments")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            list_employees()
        elif choice == '3':
            add_department()
        elif choice == '4':
            list_departments()
        elif choice == '5':
            logout()
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
