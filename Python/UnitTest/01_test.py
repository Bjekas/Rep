import unittest
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 3000
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

class TestTIM(unittest.TestCase):
    socket = None

    def setUpClass():
        global socket
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.connect(('127.0.0.1', 3000))

    def test_upper(self):
        global socket
        socket.send(b'teste')
        self.assertEqual('foo'.upper(), 'FOO')

    def test_upper1(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def tearDownClass():
        global socket
        input('')
        socket.close()

  
if __name__ == '__main__':
    unittest.main()

