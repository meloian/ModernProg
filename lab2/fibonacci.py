import sys

def fibonacci(n):
    if n < 0:
        raise ValueError("The Fibonacci number cannot be calculated for negative numbers.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def process_number(number):
    try:
        if ' ' in number:
            raise ValueError("Please enter only one number.")
        n = int(number)
        fib_number = fibonacci(n)
        return f"Fibonacci({n}) = {fib_number}", 0
    except ValueError as e:
        return f"Error: {e}", 1

def get_input(input_stream):
    return input_stream.readline().strip()

def write_output(message, output_stream, error=False):
    if error:
        print(message, file=sys.stderr)
    else:
        output_stream.write(message + "\n")

def main_logic(input_stream=sys.stdin, output_stream=sys.stdout):
    exit_code = 0  # start with success exit code
    output_stream.write("Enter a number to calculate the Fibonacci number or 'exit' to exit:\n")
    while True:
        line = get_input(input_stream)
        if line.lower() == 'exit':
            write_output("Exiting the program.", output_stream)
            break
        message, code = process_number(line)
        if code != 0:
            exit_code = code  # set to error code if any error occurs
        write_output(message, output_stream, error=code != 0)
        output_stream.write("Enter the next number or 'exit' to finish:\n")
    
    sys.exit(exit_code)  

if __name__ == "__main__":
    main_logic() 
  
