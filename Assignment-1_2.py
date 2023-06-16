import json

indian_states = {
    "Telangana": "Hyderabad",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai"
}
with open(r'C:\Users\rajes\OneDrive\Desktop\Final Project\Json\indian_states.json', 'w') as file:
    json.dump(indian_states, file)

