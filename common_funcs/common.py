from typing import Dict, List, Tuple
import numpy as np
import re

def is_number(s) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_integer(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


def calculate_regression(data, key) -> Dict[str, Tuple[float, float]]:
    regression_results = {}
    
    for key, values in data.items():
        x = np.arange(len(values))
        y = np.array(values)
        
        A = np.vstack([x, np.ones(len(x))]).T
        m, c = np.linalg.lstsq(A, y, rcond=None)[0]
        
        regression_results[key] = (m, c)
    
    return regression_results


def remove_html_tags(value: str) -> str:
    clean = re.compile('<.*?>')
    return re.sub(clean, '', value)