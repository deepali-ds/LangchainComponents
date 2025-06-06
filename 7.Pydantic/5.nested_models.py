from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address: Address

address_dict = {'city': 'Princeton' , 'state': 'New Jersey', 'pin': '08543'}

address1= Address(**address_dict)

patient_dict = {'name': 'Kathy', 'gender': 'female', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.age)
print(patient1.address.city)
print(patient1.address.state)