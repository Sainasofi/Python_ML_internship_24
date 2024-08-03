#write a code to print the following pattern.
def print_right_angled_triangle(rows):

  for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("*" * (i + 1))

rows = 5
print_right_angled_triangle(rows)
# #create a program that prompts the user to input two numbers snd performs division. Handle the arithemeticException that might occur if the user attempts to divide by zero and any potential numberFormatException that might occur during the conversion. in such cases, infrom the user about the error and ask for input again.
def divide_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 / num2
            print("Result:", result)
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except ZeroDivisionError:
            print("Division by zero is not allowed.")

if __name__ == "__main__":
    divide_numbers()
 
#sports equipment rental system POC: Create a class equiptment that stores Eid,Ename,Brand,Total quantity,avalaible quantity, add equipment to stock, delete equipment from stock, update the quantity, print the list of available equipments.
#create a new dictionary that stores the record of the students who take the sports equipment and name is as rental. Dictionary contains: Name, roll no., Eid,Ename,nstatus, return_condition. 
#create two functions as rent_item abd return_item. rent_item: this function will generate the new record to the dictionary rental and fill all the details and mark the condition as good and status as rented.
#return_item: this function will mark the status as returned if student return the item and also mention the condition as good or damaged.
class Equipment:
    def __init__(self, eid, ename, brand, total_quantity, aval_quantity):
        self.eid = eid
        self.ename = ename
        self.brand = brand
        self.total_quantity = total_quantity
        self.aval_quantity = aval_quantity

    def add_to_stock(self, quantity):
        self.total_quantity += quantity
        self.aval_quantity += quantity

    def delete_from_stock(self, quantity):
        if quantity <= self.aval_quantity:
            self.aval_quantity -= quantity
        else:
            print("Insufficient quantity available")

    def update_quantity(self, new_quantity):
        self.aval_quantity = new_quantity

    def __str__(self):
        return f"Equipment ID: {self.eid}, Name: {self.ename}, Brand: {self.brand}, Total Quantity: {self.total_quantity}, Available Quantity: {self.aval_quantity}"

rental = {}

def rent_item(student_name, roll_no, equipment):
    if equipment.aval_quantity > 0:
        rental[roll_no] = {
            "name": student_name,
            "roll_no": roll_no,
            "eid": equipment.eid,
            "ename": equipment.ename,
            "status": "rented",
            "return_condition": "good"
        }
        equipment.aval_quantity -= 1
        print(f"{equipment.ename} rented to {student_name}")
    else:
        print(f"Sorry, {equipment.ename} is not available")

def return_item(roll_no, condition):
    if roll_no in rental:
        rental[roll_no]["status"] = "returned"
        rental[roll_no]["return_condition"] = condition
        equipment = next((e for e in equipments if e.eid == rental[roll_no]["eid"]), None)
        if equipment:
            equipment.aval_quantity += 1
        print(f"Equipment returned by {rental[roll_no]['name']}")
    else:
        print("Record not found")

# Example 
equipments = [
    Equipment("E001", "Football", "Nike", 10, 8),
    Equipment("E002", "Basketball", "Adidas", 5, 3)
]

# Add equipment to stock
equipments[0].add_to_stock(2)

# Rent an item
rent_item("Saina Sofi", 117, equipments[0])

# Return an item
return_item(117, "good")

# Print available equipment
for equipment in equipments:
    print(equipment)
