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
        self.assertEqual(process_number("10"), ("55", 0))
        self.assertEqual(process_number("1"), ("1", 0))
        self.assertEqual(process_number("0"), ("0", 0))
        self.assertEqual(process_number("999"), (str(fibonacci(999)), 0))

    def test_process_number_error(self):
        self.assertEqual(process_number("a"), ("Error: invalid literal for int() with base 10: 'a'", 1))
        self.assertEqual(process_number("10 10"), ("Error: Please enter only one number.", 1))
        self.assertEqual(process_number("-1"), ("Error: The Fibonacci number cannot be calculated for negative numbers.", 1))

    def test_write_output(self):
        fake_output = StringIO()
        write_output("Test message", fake_output)
        self.assertEqual(fake_output.getvalue(), "Test message\n")

        fake_error_output = StringIO()
        write_output("Error message", fake_error_output)
        self.assertEqual(fake_error_output.getvalue(), "Error message\n")

    def test_main_logic_exit_codes(self):
        input_stream = StringIO("10\n")
        with self.assertRaises(SystemExit) as cm:
            main_logic(input_stream, sys.stdout)
        self.assertEqual(cm.exception.code, 0)  
        output_content = sys.stdout.getvalue()
        self.assertEqual(output_content.strip(), "55")  

        input_stream = StringIO("invalid\n")
        with self.assertRaises(SystemExit) as cm:
            main_logic(input_stream, sys.stdout)
        self.assertNotEqual(cm.exception.code, 0)  # expect an error, non-zero exit code
        error_output = sys.stderr.getvalue()
        self.assertTrue("invalid" in error_output and "Error:" in error_output)  

if __name__ == '__main__':
    unittest.main() 
