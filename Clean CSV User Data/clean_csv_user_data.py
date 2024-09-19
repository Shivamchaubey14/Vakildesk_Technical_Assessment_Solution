import csv
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def clean_csv(input_file, output_file):
    users = {}
    
    with open(input_file, 'r', newline='') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            if row['user_id'] not in users and is_valid_email(row['email']):
                users[row['user_id']] = row
    
    with open(output_file, 'w', newline='') as outfile:
        fieldnames = ['user_id', 'name', 'email']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for user in users.values():
            writer.writerow(user)

# Example usage
clean_csv('users.csv', 'cleaned_users.csv')
