generate random test file
import random
import string
def generate_random_test_file(filename, num_lines=100, line_length=50):
    with open(filename, '
w') as f:
        for _ in range(num_lines):
            line = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=line_length))
            f.write(line + '\n')    
generate_random_test_file('test_file.py')   
# This will create a file named 'test_file.py' with 100 lines of random text, each line being 50 characters long.
# You can adjust num_lines and line_length as needed.
# -*- coding: utf-8 -*-
# This is a sample test file generated for testing purposes.
def sample_function():
    return "Hello, World!"
# You can add more functions or classes here for testing.
# -*- coding: utf-8 -*-
# This is another line in the test file.
# You can add more lines as needed for testing.
# This is a sample test file generated for testing purposes.
def sample_function():
    return "Hello, World!"