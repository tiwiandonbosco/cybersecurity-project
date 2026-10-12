\# Python File Integrity Checker



A beginner-friendly cybersecurity project that detects unexpected file-content changes using SHA-256 hashing.



\## Overview



File Integrity Monitoring (FIM) helps security teams identify changes to important files. This project creates a trusted reference hash and compares it with the current hash to detect modifications.



\## Features



\- SHA-256 hash calculation

\- File integrity verification

\- JSON-based reference baseline

\- File path validation

\- Detection of modified files

\- Basic error handling



\## Technologies



\- Python 3

\- hashlib

\- pathlib

\- json

\- Windows PowerShell or Linux terminal



No third-party Python packages are required.



\## Usage



Create a sample file:



```powershell

Set-Content important.txt "Day 1 cybersecurity project"

```



Save its baseline:



```powershell

python integrity\_checker.py baseline important.txt

```



Verify integrity:



```powershell

python integrity\_checker.py check important.txt

```



Modify the file:



```powershell

Add-Content important.txt "This file has been modified"

```



Check again:



```powershell

python integrity\_checker.py check important.txt

```



The program should detect the change and print an alert.



\## Test Results



\- Unchanged file: PASS

\- Modified file: PASS

\- Missing file: To be verified

\- Invalid command: To be verified

\- Missing arguments: To be verified



\## Security Considerations



A matching hash indicates that the file contents match the saved reference. It does not guarantee that the file is safe.



The baseline must be protected from unauthorized modification. This educational tool does not yet provide tamper-proof baseline storage or continuous monitoring.



\## Learning Outcomes



\- Python file handling

\- Cryptographic hashing

\- SHA-256 integrity verification

\- JSON data storage

\- Basic security testing

\- File Integrity Monitoring fundamentals



\## Future Improvements



\- Monitor multiple files and directories

\- Add automated unit tests

\- Generate timestamped alerts

\- Protect baseline storage

\- Add a simple security monitoring dashboard



\## Author



Tiwian Donbosco





