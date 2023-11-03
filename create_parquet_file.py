import pandas as pd

# Generate the same larger dataset with random data
n = 4  # Number of records
data = {
    'employee_id': range(1, 5),  # Generate IDs from 1 to 1000
    'first_name': [f'Employee-{i}' for i in range(1, 5)],  # Generate unique first names
    'last_name': [f'Last-{i}' for i in range(1, 5)],  # Generate unique last names
    'department': ['HR'] * 1 + ['IT'] * 1 + ['Finance'] * 2,  # Distribute departments evenly
    'salary': [55000.00] * 4,  # Same salary for all
}

df = pd.DataFrame(data)

# Save the dataset as a Parquet file
df.to_parquet('sample.parquet', index=False)

df_read = pd.read_parquet('sample.parquet')
print(df_read)

