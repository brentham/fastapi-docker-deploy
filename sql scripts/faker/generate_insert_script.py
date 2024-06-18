import bcrypt
from faker import Faker

faker = Faker()

# Function to hash the password 'admin' using bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# Hash the password 'admin'
admin_password_hashed = hash_password('admin')

# Generate SQL insert statements for 100 users
insert_statements = []
for i in range(1, 101):
    email = faker.email()
    username = f'user{i}'
    first_name = faker.first_name()
    last_name = faker.last_name()
    hashed_password = admin_password_hashed
    is_active = 1
    insert_statements.append(f"('{email}', '{username}', '{first_name}', '{last_name}', '{hashed_password}', {is_active})")

# Create the final SQL script
sql_script = f"USE your_database_name;\n\n"  # Make sure to replace 'your_database_name' with the actual database name
sql_script += "INSERT INTO users (email, username, first_name, last_name, hashed_password, is_active)\nVALUES\n"
sql_script += ",\n".join(insert_statements) + ";\n"

# Write the script to a file
with open('insert_users.sql', 'w') as file:
    file.write(sql_script)

print("SQL script to insert 100 users with bcrypt hashed password 'admin' has been generated and saved to 'insert_users.sql'")
