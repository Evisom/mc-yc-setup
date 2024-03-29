from rcon.source import Client

class RCon:
    def __init__(self, ip, port, password):
        self.port = port
        self.ip = ip
        self.password = password

    def command(self, command):
        with Client(self.ip, self.port, passwd=self.password) as client:
            response = client.run(command)
            return response 