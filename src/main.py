"""
Main application module
"""
import requests
import pandas as pd
import numpy as np

def fetch_data(url):
    """Fetch data from API"""
    response = requests.get(url)
    return response.json()

def process_data(data):
    """Process data using pandas"""
    df = pd.DataFrame(data)
    return df.describe()

def calculate_stats(numbers):
    """Calculate statistics"""
    arr = np.array(numbers)
    return {
        'mean': np.mean(arr),
        'std': np.std(arr),
        'sum': np.sum(arr)
    }

if __name__ == "__main__":
    print("Application started")
    sample_data = [1, 2, 3, 4, 5]
    stats = calculate_stats(sample_data)
    print(f"Statistics: {stats}")