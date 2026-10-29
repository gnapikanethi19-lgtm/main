class MedicalStore:
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def display_customer(self):
        print("Customer Name:", self.customer_name)


class Medicine(MedicalStore):
    def __init__(self, customer_name):
        super().__init__(customer_name)

        self.medicines = {
            1: ("Paracetamol", 20),
            2: ("Vitamin C", 50),
            3: ("Antacid", 30),
            4: ("Cough Syrup", 100)
        }

    def display_medicines(self):
        print("\nAVAILABLE MEDICINES")
        print("-------------------")

        for number, details in self.medicines.items():
            name, price = details
            print(number, name, "- Rs.", price)

    def purchase_medicine(self):
        total = 0

        while True:
            try:
                choice = int(
                    input("\nEnter medicine number (0 to finish): ")
                )

                if choice == 0:
                    break

                if choice not in self.medicines:
                    print("Invalid medicine number.")
                    continue

                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue

                name, price = self.medicines[choice]
                amount = price * quantity
                total += amount

                print(name, "Amount: Rs.", amount)

            except ValueError:
                print("Please enter a valid number.")

        print("\n========== MEDICAL BILL ==========")
        self.display_customer()
        print("Total Amount: Rs.", total)
        print("==================================")


print("MEDICAL STORE MANAGEMENT SYSTEM")

customer = input("Enter customer name: ")

store = Medicine(customer)

store.display_medicines()
store.purchase_medicine()


