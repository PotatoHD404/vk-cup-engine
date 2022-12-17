import json
import time
import pathlib


def main():
    base_path = pathlib.Path(__file__).parent
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
    for name, tests in tasks.items():
        # Create a directory for each task
        task_path = base_path / name
        task_path.mkdir(exist_ok=True)
        tests_path = task_path / 'tests'
        tests_path.mkdir(exist_ok=True)
        answers_path = task_path / 'answers'
        answers_path.mkdir(exist_ok=True)
        # Create a file for each test
        for i, test in enumerate(tests):
            test_path = tests_path / f'{i}.txt'
            with open(test_path, 'w') as f:
                f.write(test['input'])
            answer_path = answers_path / f'{i}.txt'
            with open(answer_path, 'w') as f:
                f.write(test['output'])

        # create c++ file for each task
        cpp_path = task_path / f'main.cpp'
        # read template
        with open('template.cpp', 'r') as f:
            template = f.read()

        with open(cpp_path, 'w') as f:
            f.write(template)
        # create test_template.py for each task
        test_path = task_path / f'test.py'
        # read template
        with open('test_template.py', 'r') as f:
            template = f.read()
        with open(test_path, 'w') as f:
            f.write(template)
        # create run.py for each task
        run_path = task_path / f'run.py'
        # read template
        with open('run_template.py', 'r') as f:
            template = f.read()
        with open(run_path, 'w') as f:
            f.write(template)


if __name__ == '__main__':
    main()
