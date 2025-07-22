"""
Tests for main module
"""
import pytest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import calculate_stats, process_data

def test_calculate_stats():
    """Test statistics calculation"""
    numbers = [1, 2, 3, 4, 5]
    result = calculate_stats(numbers)
    
    assert result['mean'] == 3.0
    assert result['sum'] == 15
    assert isinstance(result['std'], float)

def test_process_data():
    """Test data processing"""
    data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
    result = process_data(data)
    
    assert result is not None
    assert len(result) > 0