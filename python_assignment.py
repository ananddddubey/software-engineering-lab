class Process:
    def __init__(self, p_id, name, start_time, priority):
        self.p_id = p_id
        self.name = name
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def sort_by_p_id(self):
        self.processes.sort(key=lambda process: process.p_id)

    def sort_by_start_time(self):
        self.processes.sort(key=lambda process: process.start_time)

    def sort_by_priority(self):
        priority_order = {"Low": 1, "MID": 2, "High": 3}
        self.processes.sort(key=lambda process: priority_order[process.priority])

    def display_table(self):
        for process in self.processes:
            print(f"P_ID: {process.p_id}, Process: {process.name}, Start Time: {process.start_time}, Priority: {process.priority}")

def main():
    flight_table = FlightTable()

    flight_table.add_process(Process("P1", "VSCode", 100, "MID"))
    flight_table.add_process(Process("P23", "Eclipse", 234, "MID"))
    flight_table.add_process(Process("P93", "Chrome", 189, "High"))
    flight_table.add_process(Process("P42", "JDK", 9, "High"))
    flight_table.add_process(Process("P9", "CMD", 7, "High"))
    flight_table.add_process(Process("P87", "NotePad", 23, "Low"))

    while True:
        print("Sorting options:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            flight_table.sort_by_p_id()
        elif choice == 2:
            flight_table.sort_by_start_time()
        elif choice == 3:
            flight_table.sort_by_priority()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please choose a valid option.")

        print("\nSorted Flight Table:")
        flight_table.display_table()
        print()

if __name__ == "__main__":
    main()
