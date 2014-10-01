UDP:

User Datagram Protocol
Un-reliable connection-less based protocol
Low Overhead

Used fro VOIP, online games, streaming

We use recvfrom() and sendto() with UDP because it is connectionless.  We need to tell the data where to go when we send it.





TCP:
Transmission Control Protocol
Reliable Connection based protocol
Ordered & error checked (simple checksum)

Used by Web Broswers, Email, SSH, FTP, Etc





.pyw
The pyw extenison will run the script without invoking the console window - this is especially useful if your progam is GUI based. It can still be run if you rename it to .py later.


How to connect to URL:
    server_ip = socket.gethostbyname(URL)

    You can also just find the IP using:
        In console, type "ping URL" which will return the domain's IP address.
