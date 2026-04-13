#This functiosn collects the data from the user
def user_data():
    grand_total = 0
    store = []

    for i in range(1, 11):
        print() #To format it nicely
        total = 0  # Reset for each salesman
        items = []
        salesman_name = input(f"Name of salesman {i}: ")

        for j in range(1, 6):
            
            while True:
                try:
                    user_input = int(input(f"Enter sales for item {j}: "))
                    break
                except ValueError:
                    print("Enter a number!")
                    continue

            total += user_input
            grand_total += user_input
            items.append(user_input)
        store.append({"name":salesman_name, "items":items, "total":total})
        print(f"{salesman_name}'s total: {total}")
    return store, grand_total

#This function, takes the collected data and displays it in a table format  
def display_table(store, grand_total):
    print("Name      Item 1  Item 2  Item 3  Item 4  Item 5  total")
    print("-"*54)

    for seller in store:
        row = f"{seller['name']:<11}"  # start with the name
        for item in seller["items"]:
            row += f"{item:<8}"  # keep adding each item
        row += f"{seller['total']:<8}"  # add total at the end
        print(row)

    print("-"*54)

    print(f"Grand Total: {grand_total}")

    print("-"*54)


def main():
    store, grand_total = user_data()
    display_table(store, grand_total)

main()