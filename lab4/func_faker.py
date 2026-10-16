from faker import Faker
fake = Faker("uk_UA")
def generate_person():
    return {
        "name": fake.name(),
        "city": fake.city(),
        "email": fake.email(),
    }