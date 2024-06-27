class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.currentCount = 0
        self.occupiedSlots = []

    def parkVehicle(self):
        if self.currentCount < self.capacity:
            plateNumber = input("Enter vehicle plate number to park: ")
            self.occupiedSlots.append(plateNumber)
            self.currentCount += 1
            print(f"Vehicle with plate number {plateNumber} parked successfully.")
        else:
            print("Sorry, the parking lot is full. Cannot park vehicle.")

    def exitVehicle(self):
        plateNumber = input("Enter vehicle plate number to exit: ")
        if plateNumber in self.occupiedSlots:
            self.occupiedSlots.remove(plateNumber)
            self.currentCount -= 1
            print(f"Vehicle with plate number {plateNumber} exited successfully.")
        else:
            print(f"Vehicle with plate number {plateNumber} not found in parking lot.")

    def displayStatus(self):
        print(f"Current number of vehicles parked: {self.currentCount}/{self.capacity}")
        print("Vehicles parked with plate numbers: ", self.occupiedSlots)

parkingLot = ParkingLot(20)

while True:
    print("\nMenu:")
    print("1. Park a vehicle")
    print("2. Exit a vehicle")
    print("3. Display parking status")
    print("4. Exit the program")
    choice = input("Please choose an option (1/2/3/4): ")

    if choice == '1':
        parkingLot.parkVehicle()
    elif choice == '2':
        parkingLot.exitVehicle()
    elif choice == '3':
        parkingLot.displayStatus()
    elif choice == '4':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
