from mcstatus import JavaServer

# Use your ZeroTier IP
server = JavaServer.lookup("10.243.179.32:43391")

try:
    status = server.status()
    print(f"Server is online with {status.players.online} player(s) connected.")
    # print(f"Server is online with {status.players} player(s) connected.")
except Exception as e:
    print("Failed to connect. Server might be offline or unreachable.")
    print("Error:", e)
