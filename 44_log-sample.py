# Import the logging module for logging functionality
import logging

# Import the employee module (assuming it exists and is used elsewhere in the application)
import employee

# Create a custom logger with the name of the current module (__name__)
# This helps identify where the log messages are coming from
logger = logging.getLogger(__name__)

# Set the logging level for the logger to DEBUG
# This means all messages with level DEBUG and above will be processed
logger.setLevel(logging.DEBUG)

# Create a formatter to define the structure of the log messages
# The format includes:
# - %(asctime)s: Timestamp
# - %(name)s: Name of the logger
# - %(message)s: The log message
formatter = logging.Formatter('%(asctime)s - %(name)s- %(message)s')

# Create a file handler to write logs to a file named 'sample.log'
file_handler = logging.FileHandler('sample.log')

# Set the formatter for the file handler
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Override the logger's level to ERROR
# This means only messages with level ERROR and above will be processed
logger.setLevel(logging.ERROR)

# Create a stream handler to output logs to the console
stream_handler = logging.StreamHandler()

# Set the formatter for the stream handler
stream_handler.setFormatter(formatter)

# Add the stream handler to the logger
logger.addHandler(stream_handler)

# Uncomment the following block to use basicConfig for logging configuration
# This is an alternative to manually creating handlers and formatters
# logging.basicConfig(filename='sample.log',
#                     level=logging.INFO,
#                     format='%(asctime)s - %(name)s- %(message)s')

# Define a function to add two numbers
def add(x, y):
    """Add function."""
    return x + y

# Define a function to subtract two numbers
def subtract(x, y):
    """Subtract function."""
    return x - y

# Define a function to multiply two numbers
def multiply(x, y):
    """Multiply function."""
    return x * y

# def divide(x, y):
#     """Divide function."""
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         logger.error('Tried to divide by zero')
#     else:
#         return result

# Define a function to divide two numbers
def divide(x, y):
    """Divide function."""
    try:
        # Attempt to divide x by y
        result = x / y
    except ZeroDivisionError:
        # Log an error message with the exception details if division by zero occurs
        logger.exception('Tried to divide by zero')
    else:
        # Return the result if no exception occurs
        return result

# Define two numbers for testing
num1 = 3
num2 = 0

# Log the result of the add function
# Note: Since the logger level is set to ERROR, DEBUG messages will not be logged
logger.debug('Addition of 3 and 4 gives us: {}'.format(add(num1, num2)))

# Log the result of the subtract function
logger.debug('Subtraction of 3 and 4 gives us: {}'.format(subtract(num1, num2)))

# Log the result of the multiply function
logger.debug('Multiplication of 3 and 4 gives us: {}'.format(multiply(num1, num2)))

# Log the result of the divide function
# This will trigger the exception handler if num2 is 0
logger.debug('Division of 3 and 0 gives us: {}'.format(divide(num1, num2)))