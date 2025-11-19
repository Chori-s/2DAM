def build_profile(location, field, email, pet_name, first_name, last_name):
    profile = {
        'location': location,
        'field': field,
        'email': email,
        'pet_name': pet_name,
        'first_name': first_name,
        'last_name': last_name
    }
    return profile

user_profile = build_profile('Benalmádena', 'Informatica', 'ivan@gmail.com', 'Onix', 'Iván', 'Liñán')

print(user_profile)

