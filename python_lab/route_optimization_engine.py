"""
Project: Route Optimization Engine (TSP Solver)
Description: 
Implements a Brute-Force solution for the Traveling Salesman Problem (TSP).
Features data sanitization, Euclidean distance calculation, and path optimization
using combinatorial permutations.

Technical Highlights:
- Data Integrity: Filters non-integer coordinates.
- Computational Complexity: O(n!) search space analysis.
- Modular Design: Separated distance logic from route optimization.
"""

import math
import itertools

def calculate_distance(point_a: dict, point_b: dict) -> float:
    """Calculates Euclidean distance between two coordinate dictionaries."""
    diff_x = point_b["x"] - point_a["x"]
    diff_y = point_b["y"] - point_a["y"]
    
    sum_squares = (diff_x ** 2) + (diff_y ** 2)
    return math.sqrt(sum_squares)

def bus_stops(raw_data: list) -> dict:
    """
    Sanitizes coordinate data and identifies the path with the minimum total distance.
    """
    print(f"--- Processing {len(raw_data)} initial data points ---")
    
    # 1. Data Cleaning
    clean_list = []
    for point in raw_data:
        # Check if both coordinates are integers (Data Integrity check)
        if isinstance(point.get("x"), int) and isinstance(point.get("y"), int):
            clean_list.append(point)
        else:
            print(f"Removed invalid data point: {point}")

    # 2. Optimization Logic (Brute Force Approach)
    permutations = list(itertools.permutations(clean_list))
    print(f"Analyzing {len(permutations)} possible route combinations...")

    min_distance = float('inf')
    best_route = []

    for route in permutations:
        current_total_distance = 0

        # Calculate sum of all segments in the current route
        for i in range(len(route) - 1):
            current_point = route[i]
            next_point = route[i+1]
            
            segment_dist = calculate_distance(current_point, next_point)
            current_total_distance += segment_dist

        # Update best route if a shorter path is found
        if current_total_distance < min_distance:
            min_distance = current_total_distance
            best_route = list(route)

    # 3. Results Formatting
    rounded_dist = round(min_distance, 2)
    print(f"Optimization Complete. Minimum distance: {rounded_dist} units")

    return {
        "optimized_path": best_route,
        "total_distance": rounded_dist
    }

# Dataset for testing (Includes dirty data: strings, floats, etc.)
bs_data = [
    {"x": 1, "y": 1},
    {"x": "some", "y": 12},
    {"x": 3, "y": 9},
    {"x": 9, "y": 4},
    {"x": 1, "y": 1},
    {"x": 1, "y": 5},
    {"x": 5, "y": 2},
    {"x": 4, "y": 10},
    {"x": 8, "y": 8},
    {"x": -3, "y": 2.3}
]

if __name__ == "__main__":
    final_result = bus_stops(bs_data)
    
    print("\n" + "="*50)
    print("FINAL OPTIMIZED OUTPUT")
    print("="*50)
    print(f"Route Order: {final_result['optimized_path']}")
    print(f"Total Distance: {final_result['total_distance']}")
    print("="*50)
