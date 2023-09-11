import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28]}
df = pd.DataFrame(data)

# Selecting data
print(df['Name'])  # Select the 'Name' column
print(df[df['Age'] > 30])  # Select rows where Age > 30

# Data manipulation
df['Salary'] = [50000, 60000, 70000, 55000]  # Add a 'Salary' column
df['Age'] = df['Age'] + 2  # Increase Age by 2 years

# Data analysis
print(df.describe())  # Summary statistics


