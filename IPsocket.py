import socket

website = input("unesi website URL: ")
ip = socket.gethostbyname(website)
print(f"IP adresa website-a {website} je {ip}")

