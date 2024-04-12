import unittest
from io import StringIO
import sys

from fibonacci import fibonacci, process_number, get_input, write_output, main_logic

class TestFibonacciProgram(unittest.TestCase):
    
    def setUp(self):
        # save original stdout and stderr
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr

        # redirect stdout and stderr to StringIO
        sys.stdout = StringIO()
        sys.stderr = StringIO()

    def tearDown(self):
        # restore original stdout and stderr
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr

    def test_fibonacci_positive(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_process_number(self):
        self.assertEqual(process_number("10"), ("Fibonacci(10) = 55", 0))
        self.assertEqual(process_number("1"), ("Fibonacci(1) = 1", 0))
        self.assertEqual(process_number("0"), ("Fibonacci(0) = 0", 0))
        self.assertEqual(process_number("999"), ("Fibonacci(999) = " + str(fibonacci(999)), 0))  

    def test_process_number_error(self):
        self.assertEqual(process_number("a"), ("Error: invalid literal for int() with base 10: 'a'", 1))
        self.assertEqual(process_number("10 10"), ("Error: Please enter only one number.", 1))
        self.assertEqual(process_number("-1"), ("Error: The Fibonacci number cannot be calculated for negative numbers.", 1))

    def test_get_input_multiple_lines(self):
        fake_input = StringIO('test\nanother test\n')
        self.assertEqual(get_input(fake_input), 'test')
        self.assertEqual(get_input(fake_input), 'another test')

    def test_write_output(self):
        fake_output = StringIO()
        write_output("Test message", fake_output)
        self.assertEqual(fake_output.getvalue(), "Test message\n")

        fake_error_output = StringIO()
        sys.stderr = fake_error_output
        write_output("Error message", fake_error_output, error=True)
        self.assertEqual(fake_error_output.getvalue(), "Error message\n")
        sys.stderr = sys.__stderr__

    def test_main_logic_exit_codes(self):
        # test with valid input followed by 'exit'
        input_stream = StringIO("10\nexit\n")
        with self.assertRaises(SystemExit) as cm:
            main_logic(input_stream, sys.stdout)
        self.assertEqual(cm.exception.code, 0)  # No error, exit code should be 0
        output_content = sys.stdout.getvalue() + sys.stderr.getvalue()
        self.assertIn("Fibonacci(10) = 55", output_content)
        self.assertIn("Exiting the program.", output_content)

        # reset streams for next test
        sys.stdout = StringIO()
        sys.stderr = StringIO()

        # test with invalid input followed by 'exit'
        input_stream = StringIO("invalid\nexit\n")
        with self.assertRaises(SystemExit) as cm:
            main_logic(input_stream, sys.stdout)
        self.assertNotEqual(cm.exception.code, 0)  # expect an error, non-zero exit code
        output_content = sys.stdout.getvalue() + sys.stderr.getvalue()
        self.assertIn("Error: invalid literal for int() with base 10: 'invalid'", output_content)
        self.assertIn("Exiting the program.", output_content) 

if __name__ == '__main__':
    unittest.main()
