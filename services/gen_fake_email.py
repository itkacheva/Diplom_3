from faker import Faker
fake = Faker()


def gen_fake_email():
    return fake.email()
