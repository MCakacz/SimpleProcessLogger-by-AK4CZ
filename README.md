# Session Monitoring Script

This Python script is designed to monitor and log session activity on a computer. It tracks the opening and closing of processes and creates a log file with essential information about the sessions.

## Prerequisites

Before using this script, make sure you have the following prerequisites installed:

- [Python](https://www.python.org/) (version 3.6 or higher)
- [psutil](https://pypi.org/project/psutil/) library

## Usage

1. Clone this repository to your local machine or download the script.

```
git clone https://github.com/your-username/your-repo.git
```
2. Navigate to the repository's directory:
```
cd your-repo
```
3. Run the script:
```
python session_monitor.py
```
The script will create a sessions folder if it doesn't exist and log session activity in .log files within that folder.
## Output
The script records the following information in the log file:

- Computer name
- IP address
- Total session count for the computer
- Session start and end times for each process
The log files are named with a timestamp and the computer name for easy reference.

## Example log entry
```
2023-09-18_15-30-45 - Opening: chrome.exe (PID: 1234) (Action 1)
2023-09-18_15-45-12 - Closing: notepad.exe (PID: 5678)
```
## Author
Arkadiusz Adamowski/AK4CZ

## License
This project is licensed under the MIT License - see the [LICENSE](https://www.mediafire.com/file/1237ejkpwz6ro53/LICENSE/file) file for details.
