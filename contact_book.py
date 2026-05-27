contacts = [

    {
        "name": "mansi",
        "phone": "9876543210",
        "email": "mansi@gmail.com"
    },

    {
        "name": "Noopur",
        "phone": "9123456780",
        "email": "noopur@gmail.com"
    },

    {
        "name": "Rahul",
        "phone": "9988776655",
        "email": "rahul@gmail.com"
    },

    {
        "name": "Priya",
        "phone": "9871234560",
        "email": "priya@gmail.com"
    },

    {
        "name": "Aman",
        "phone": "9012345678",
        "email": "aman@gmail.com"
    }
]


def find_contact(name):

    for contact in contacts:

        if contact["name"].lower() == name.lower():
            return contact

    return "Contact not found"


search_name = input("Enter contact name: ")

result = find_contact(search_name)

print(result)