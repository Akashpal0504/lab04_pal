# Sample data
data = [
    ("P1", "VSCode", 100, "MID"),
    ("P23", "Eclipse", 234, "MID"),
    ("P93", "Chrome", 189, "High"),
    ("P42", "JDK", 9, "High"),
    ("P9", "CMD", 7, "High"),
    ("P87", "NotePad", 23, "Low"),
]

def print_table(data):
    print("P_ID\tProcess\tStart Time (ms)\tPriority")
    print("="*40)
    for row in data:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}")

def sort_by_pid(data):
    return sorted(data, key=lambda x: x[0])

def sort_by_start_time(data):
    return sorted(data, key=lambda x: x[2])

def sort_by_priority(data):
    priority_order = {"Low": 0, "MID": 1, "High": 2}
    return sorted(data, key=lambda x: priority_order[x[3]])

print("Flight Table Sorting Program")
print("1. Sort by P_ID")
print("2. Sort by Start Time")
print("3. Sort by Priority")

choice = int(input("Enter your choice: "))

if choice == 1:
    sorted_data = sort_by_pid(data)
elif choice == 2:
    sorted_data = sort_by_start_time(data)
elif choice == 3:
    sorted_data = sort_by_priority(data)
else:
    print("Invalid choice")
    exit()

print("\nSorted Table:")
print_table(sorted_data)


