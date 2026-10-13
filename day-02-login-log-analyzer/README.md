\# Python Login Log Analyzer



A beginner-friendly cybersecurity tool that analyzes simulated authentication logs to identify repeated failed login attempts and generate basic security alerts.



\## Overview



Security Operations Center (SOC) analysts investigate authentication logs to identify suspicious activity. This project demonstrates a simple Python-based approach to parsing login events, counting failures, and flagging IP addresses that exceed a configurable threshold.



\## Features



\- Parses comma-separated authentication logs.

\- Counts successful and failed login events.

\- Groups failed attempts by IP address and username.

\- Flags IP addresses with repeated failed login attempts.

\- Skips malformed records and invalid login statuses.

\- Supports a custom log file path.

\- Uses Python's built-in libraries.



\## Requirements



\- Python 3.10 or later

\- Windows, Linux, or macOS



No third-party packages are required.



\## Usage



Run the analyzer using the default sample log:



powershell

python login\_log\_analyzer.py





Analyze a different log file:



powershell

python login\_log\_analyzer.py test\_bad.log





The default alert threshold is three failed attempts per IP address. You can change `FAILURE\_THRESHOLD` in the Python script.



\## Sample Results



For the included simulated authentication events:



\- Total valid events: 12

\- Successful logins: 4

\- Failed logins: 8

\- Alert: `203.0.113.25` recorded six failed login attempts.



\## How It Works



1\. Reads the authentication log line by line.

2\. Splits each valid line into timestamp, username, IP address, and status.

3\. Counts successful and failed login events.

4\. Groups failures by IP address and username.

5\. Compares each IP's failure count with the configured threshold.

6\. Prints a summary and any resulting alerts.



\## Security Considerations



A repeated-failure alert is an indicator for investigation, not proof of a brute-force attack. Analysts should consider event timing, account activity, and other evidence.



The current implementation uses a total failure count per IP, not a time-based detection window. It is an educational demonstration, not a production SIEM or continuous monitoring system.



\## Learning Outcomes



\- Python log parsing and file handling

\- Dictionaries and `Counter`

\- Basic authentication event analysis

\- Threshold-based detection

\- Input validation and error handling

\- SOC investigation fundamentals



\## Future Improvements



\- Detect failures within a configurable time window.

\- Add automated unit tests.

\- Export alerts to JSON or CSV.

\- Generate timestamped reports.

\- Add more robust file and data validation.



\## Disclaimer



This project uses simulated log data for educational purposes. The sample IP addresses are reserved for documentation and examples.



\## Author



Tiwian Donbosco





