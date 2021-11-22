from faker import Faker

fake = Faker()

def get_user():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "address": fake.address(),
        "created_at": fake.year()
    }