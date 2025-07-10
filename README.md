This project is a simple TCP port scanner built using Python’s socket and threading modules.
It scans a given IP address or domain name over a range of ports and checks which ports are open.

I focused on understanding and implementing:

1) IP and domain resolution

2) TCP port scanning

3) Multi-threading for faster performance



**Tools Used**

Python 3
Socket programming
Threading module
Terminal (CLI)
Target: scanme.nmap.org for ethical scanning


**Workflow**


User Input
Enter the hostname or IP, and a start & end port range.

Threaded Scanning
Uses multiple threads to scan ports simultaneously.

Checks for Open Ports
If a port responds with a successful connection, it’s considered open.

Result Output
Displays open ports on the screen and writes them to a .txt file.



<img width="1853" height="992" alt="Screenshot (1558)" src="https://github.com/user-attachments/assets/88c94a77-a7cf-47c4-b1ae-a7e66665c6c8" />


**What I Learned!**


1)How to use Python’s socket and threading modules

2)What open ports mean and how they respond to TCP requests

3)Why multi-threading speeds up port scans significantly

4)Basics of network recon and ethical scanning practices




Credits

Inspired by basic Nmap behavior and real-world TCP/IP concepts. :))
