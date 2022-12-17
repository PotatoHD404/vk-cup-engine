import subprocess
import pathlib
import os


def test_all():
    base_path = pathlib.Path(__file__).parent
    tests_path = base_path / 'tests'
    answers_path = base_path / 'answers'
    for i in range(len(os.listdir(tests_path))):
        test_path = tests_path / f'{i}.txt'
        answer_path = answers_path / f'{i}.txt'
        with open(test_path, 'r') as f:
            test = f.read()
        with open(answer_path, 'r') as f:
            answer = f.read()
        p = subprocess.Popen(['wsl', './main'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd=base_path)
        out, err = p.communicate(test.encode())
        if out.decode() == answer:
            print(f'Test {i} passed')
        else:
            print(f'Test {i} failed')
            print(f'Expected: {answer}')
            print(f'Got: {out.decode()}')
