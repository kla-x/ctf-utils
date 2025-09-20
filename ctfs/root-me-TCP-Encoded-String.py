import socket
with socket.create_connection(("challenge01.root-me.org",52023),timeout=10) as s:
    data = s.recv(1000)
    print(data.decode(errors="replace"))
    d = data.decode(errors="replace")
    print(d.find("my string is"))

    for j in d.splitlines():
        print(f"> {j}")
    d.splitlines().

    0702917307