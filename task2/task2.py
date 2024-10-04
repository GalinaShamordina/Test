import sys
import math

def read_circle(file_path):
    with open(file_path, 'r') as file:
        x_c, y_c = map(float, file.readline().strip().split())
        radius = float(file.readline().strip())
    return (x_c, y_c), radius

def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points

def calculate_position(point, center, radius):
    x, y = point
    x_c, y_c = center
    distance_squared = (x - x_c) ** 2 + (y - y_c) ** 2
    radius_squared = radius ** 2
    
    if distance_squared < radius_squared:
        return 1 
    elif distance_squared == radius_squared:
        return 0  
    else:
        return 2  

def main(circle_file, points_file):
    center, radius = read_circle(circle_file)
    points = read_points(points_file)
    results = []
    for point in points:
        position = calculate_position(point, center, radius)
        results.append(position)
    for result in results:
        print(result)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <circle_file> <points_file>")
        sys.exit(1)
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    main(circle_file, points_file)
