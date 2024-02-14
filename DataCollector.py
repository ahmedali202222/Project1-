import random
import string

class DataCollector:
    def __init__(self):
        self.user_data = []

    def generate_random_username(self):
        return ''.join(random.choices(string.ascii_lowercase, k=8))

    def generate_random_password(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    def generate_random_birthdate(self):
        return '{:02d}-{:02d}-{}'.format(random.randint(1, 12), random.randint(1, 28), random.randint(1950, 2000))

    def generate_random_address(self):
        return '123 Main St, Anytown, USA'

    def generate_random_ssn(self):
        return ''.join(random.choices(string.digits, k=9))

    def generate_random_product_id(self):
        return 'ID-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def generate_random_salesperson(self):
        return 'Salesperson{}'.format(random.randint(1, 10))

    def generate_user_data(self, num_users):
        for _ in range(num_users):
            user = {
                'username': self.generate_random_username(),
                'password': self.generate_random_password(),
                'birthdate': self.generate_random_birthdate(),
                'address': self.generate_random_address(),
                'ssn': self.generate_random_ssn(),
                'product_purchased': self.generate_random_product_id(),
                'salesperson': self.generate_random_salesperson()
            }
            self.user_data.append(user)

class DataWarehouse:
    def __init__(self):
        self.key_value_pairs = {}

    def add_user_data(self, user_id, user_data):
        self.key_value_pairs[user_id] = user_data

    def search_users_by_state(self, state):
        return [user_data for user_data in self.key_value_pairs.values() if state in user_data['address']]

    def search_users_by_salesperson(self, salesperson):
        return [user_data for user_data in self.key_value_pairs.values() if user_data['salesperson'] == salesperson]

    def search_users_by_product_id(self, product_id):
        return [user_data for user_data in self.key_value_pairs.values() if user_data['product_purchased'] == product_id]

# Step One: Data Collection
data_collector = DataCollector()
data_collector.generate_user_data(100)  # Generate sample user data for 100 users

# Step Two: Key/Value Pairs
data_warehouse = DataWarehouse()
for i, user_data in enumerate(data_collector.user_data):
    data_warehouse.add_user_data(i, user_data)

# Step Three: Search Engine
# Search users by state
users_in_state = data_warehouse.search_users_by_state('CA')
print("Users in California:")
for user in users_in_state:
    print(user)

# Search users by salesperson
users_handled_by_salesperson = data_warehouse.search_users_by_salesperson('Salesperson5')
print("\nUsers handled by Salesperson5:")
for user in users_handled_by_salesperson:
    print(user)

# Search users by product ID
users_purchased_product = data_warehouse.search_users_by_product_id('ID-ABC123')
print("\nUsers who purchased product with ID-ABC123:")
for user in users_purchased_product:
    print(user)
