import json
import sys

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
def write_json(filename, data):
    with open(filename, 'w',encoding='utf-8' ) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
def fill_report(tests, values):
    value_map = {item['id']: item['value'] for item in values['values']}
    if isinstance(tests, dict):
        for key, value in tests.items():
            if key == 'id' and value in value_map:
                tests['value'] = value_map[value]
            else:
                fill_report(value, values)
    elif isinstance(tests, list):
        
        for item in tests:
            fill_report(item, values)

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <values.json> <tests.json> <report.json>")
        return
    
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]
    
    values = load_json(values_file)
    tests = load_json(tests_file)
    
    fill_report(tests, values)

    write_json(report_file, tests)
    
if __name__ == "__main__":
    main()
