0x03. Log Parsing
Project Overview
This project involves parsing and processing log data in real-time using Python. The primary goal is to read log entries from standard input (stdin), extract relevant information, and compute metrics such as the total file size and the number of occurrences of specific HTTP status codes. The script is designed to handle large streams of data efficiently, and it must be able to handle interruptions (e.g., via CTRL + C) gracefully.

Requirements
Python Version: The script will be interpreted using Python 3.4.3 on Ubuntu 20.04 LTS.
Text Editors: vi, vim, emacs
Style Guidelines: The code must follow PEP 8 style (version 1.7.x).
Execution: All Python files must be executable and end with a new line.
First Line of Files: #!/usr/bin/python3
Repository: GitHub repository alx-interview, directory 0x03-log_parsing, file 0-stats.py
Concepts and Resources
File I/O in Python
Reading from sys.stdin line by line.
Python Input and Output documentation.
Signal Handling in Python
Handling keyboard interruptions using signal handling.
Python Signal Handling documentation.
Data Processing
Parsing strings to extract specific data points.
Aggregating data to compute summaries.
Regular Expressions
Using regular expressions to validate and extract data from log lines.
Python Regular Expressions documentation.
Dictionaries in Python
Counting occurrences of status codes using dictionaries.
Python Dictionaries documentation.
Exception Handling
Handling potential exceptions during file reading and data processing.
Python Exceptions documentation.
