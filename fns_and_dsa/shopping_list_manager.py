# Shopping List Manager
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip().lower()
    
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"{item} has been added to your shopping list.")
            pass
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from your shopping list.")
            else:
                print(f"{item} is not in your shopping list.")
            pass
        elif choice == '3':
            if shopping_list:
                print("Your shopping list contains:")
                for idx, item in enumerate(shopping_list, start=1):
                   print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, 4.")

if __name__ == "__main__":
    main()