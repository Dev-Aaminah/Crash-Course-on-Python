# Logging is a fundamental concept in software development. It is essential for debugging, monitoring, and maintaining applications, especially as they grow in complexity. By using Python's logging module effectively, you can build more reliable, maintainable, and scalable applications. If you're serious about software development, mastering logging is a must!

# Logging is the process of recording events, messages, and errors that occur during the execution of a program. It helps developers:
# Debug issues.
# Monitor application behavior.
# Track errors and exceptions.
# Analyze performance

import logging
# log message
logging.warning('This is a warning message')

# Log Levels
# Logging supports different levels of severity. Here are the standard levels (from lowest to highest severity):
# DEBUG: Detailed information for debugging.
# INFO: General runtime events.
# WARNING: Indicates a potential issue.
# ERROR: Indicates a serious problem.
# CRITICAL: Indicates a critical failure.

logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
# Observations:
# The basicConfig() method configures the logging level.
# Setting level=logging.DEBUG ensures all messages (DEBUG and above) are logged.

# Configuring Log Format
# You can customize the log format to include additional information like timestamps, module names, and line numbers.

# Example: Custom Log Format
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.info('This is an info message')

# Logging to a File
# Instead of printing logs to the console, you can write them to a file.
# Example: Logging to a File

logging.basicConfig(
    filename='app.log',  # Log file name
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info('This message will be written to the log file')