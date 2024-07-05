import json
import sys

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def update_values(tests, values):
    if isinstance(tests, list):
        for test in tests:
            update_values(test, values)
    elif isinstance(tests, dict):
        test_id = tests.get('id')
        if test_id is not None and test_id in values:
            tests['value'] = values[test_id]
        if 'values' in tests:
            update_values(tests['values'], values)

def main(values_path, tests_path, report_path):
    values_data = load_json(values_path)
    tests_data = load_json(tests_path)
    values_dict = {item['id']: item['value'] for item in values_data['values']}
    update_values(tests_data['tests'], values_dict)
    save_json(tests_data, report_path)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Используй команду: python task3.py values.json tests.json report.json")
    else:
        values_path = sys.argv[1]
        tests_path = sys.argv[2]
        report_path = sys.argv[3]
        main(values_path, tests_path, report_path)
