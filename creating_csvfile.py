import csv
import re

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def clean_csv(input_file, output_file):
    seen = set()
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            if row['user_id'] not in seen and is_valid_email(row['email']):
                writer.writerow(row)
                seen.add(row['user_id'])

# Example usage
clean_csv('users.csv', 'cleaned_users.csv')
