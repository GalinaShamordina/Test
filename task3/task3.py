import json
import sys

def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def write_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def fill_report(tests, values):
    if isinstance(tests, list):
        for test in tests:
            if isinstance(test, dict):
                test_id = test.get('id')
                if test_id in values:
                    test['value'] = values[test_id]
                else:
                    test['value'] = None  
            if 'tests' in test:
                fill_report(test['tests'], values)

def main():
    if len(sys.argv) != 4:
        print("Использование: python script.py <path_to_values.json> <path_to_tests.json> <path_to_report.json>")
        return

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    values = read_json(values_file)
    tests = read_json(tests_file)

    fill_report(tests, values)

    write_json(report_file, tests)

if __name__ == "__main__":
    main()
