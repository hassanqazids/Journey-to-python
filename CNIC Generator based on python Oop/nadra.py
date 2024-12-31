import random
class NadraProgram:
    def __init__(self):
        self.users = {}
    def generate_cnic(self):
        while True:
            cnic = f"{random.randint(1000000, 9999999)}-{random.randint(10000000, 99999999)}-{random.randint(1, 9)}"
            if cnic not in self.users: 
                return cnic
    def add_user(self):
      
        print("WELCOME TO NADRA")
        
        name = input("Enter name: ")
        lastname = input("Enter last name: ")
        age = int(input("Enter age: "))
    
        if age < 18:
            print(f"{name} {lastname}, you are not eligible for getting a CNIC.")
            return  
        
        province = input("Enter province name: ")
        gender = input("Enter gender (Male/Female): ")
        father_name = input("Enter Father's name: ")
        mother_name = input("Enter Mother's name: ")
        cnic = self.generate_cnic()
     
        self.users[cnic] = {
            "Name": name,
            "LastName": lastname,
            "Age": age,
            "Gender": gender,
            "FatherName": father_name,
            "MotherName": mother_name,
            "Province": province
        }
        
        print(f"Your CNIC number is: {cnic}")
        print("YOU are successfully added!")
        
   
        print("Current Users:")
        for cnic, user_info in self.users.items():
            print(f"CNIC: {cnic}, Name: {user_info['Name']} {user_info['LastName']}, Age: {user_info['Age']}")

nadra = NadraProgram()
nadra.add_user()
