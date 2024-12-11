import sys 
import os 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mypackage import add, subtract 
def test_add(): 
    assert add(1, 2) == 3 
def test_subtract(): 
    assert subtract(1, 2) == -1