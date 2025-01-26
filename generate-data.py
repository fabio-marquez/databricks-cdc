# This notebook is used to generate the data for the project

import uuid
import random
import pandas as pd
from typing import Tuple

def generate_name() -> str:
    """Generate a random full name from predefined lists."""
    list_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hank']
    list_last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
    return f"{random.choice(list_names)} {random.choice(list_last_names)}"

def generate_email(name: str) -> str:
    """Generate an email address from a name.
    
    Args:
        name: Full name to convert into email
    Returns:
        Email address string
    """
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    return f"{name.lower().replace(' ', '.')}@{random.choice(domains)}"

def generate_record() -> Tuple[uuid.UUID, str, str]:
    """Generate a single record with ID, name, and email."""
    id = uuid.uuid4()
    name = generate_name()
    email = generate_email(name)
    return str(id), name, email

def main(num_records: int = 100, output_file: str = 'fake_data.json') -> None:
    """Generate fake data and save to JSON file.
    
    Args:
        num_records: Number of records to generate
        output_file: Path to output JSON file
    """
    all_records = [generate_record() for _ in range(num_records)]
    print(f"{num_records} names generated")
    
    df = pd.DataFrame(all_records, columns=['id', 'name', 'email'])
    try:
        df.to_json(output_file, index=False)
        print(f"Data successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving data to {output_file}: {str(e)}")

if __name__ == "__main__":
    main()

