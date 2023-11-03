import pandas as pd
from sqlalchemy import create_engine

# Define the PostgreSQL connection URL
db_url = "postgresql://postgres:Arrow#0610@localhost:5434/Example"

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Load data from the Parquet file
parquet_data = pd.read_parquet('sample.parquet')


sql_query = "SELECT * FROM employees"
# sql_query_2 = "select * from Employees where department='HR'"

db_data = pd.read_sql_query(sql_query, engine)


# comparing specific data :

# parquet_data_filtered = parquet_data[parquet_data['department'] == "HR"]
# print(parquet_data_filtered)

# Compare data

# Data Consistency Checks:
if parquet_data.equals(db_data):
    print("Data is same.")
else:
    print("Data is different.")

if len(parquet_data) == len(db_data):
    print("Record counts match.")
else:
    print("Record counts do not match.")

if parquet_data['salary'].sum() == db_data['salary'].sum():
    print("Salary sums match.")
else:
    print("Salary sums do not match.")

# Data Type Validation:

if set(parquet_data.columns) == set(db_data.columns):
    print("Columns are Same")
else:
    print("Columns are different")

if parquet_data.dtypes.equals(db_data.dtypes):
    print("Data types match.")
else:
    print("Data types do not match.")

# Data Completeness checks:
if parquet_data.isnull().sum().equals(db_data.isnull().sum()):
    print("Null values match.")
else:
    print("Null values do not match.")

# Dispose of the SQLAlchemy engine
engine.dispose()
