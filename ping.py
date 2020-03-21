import socket
import argparse
from icmp import ICMPSocket


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='send ICMP ECHO_REQUEST to network hosts')
    parser.add_argument('-c', metavar='count', dest='count', default=5, type=int, help='Stop after sending count ECHO_REQUEST packets.')
    parser.add_argument('-s', metavar='packetsize', dest='packetsize', default=56, type=int, help='Specifies the number of data bytes to be sent.')
    parser.add_argument('target')
    args = parser.parse_args()

    ipaddr = socket.gethostbyname(args.target)
    sock = ICMPSocket(ipaddr, args.packetsize)
    print('PING {}({}) {} bytes of data.'.format(args.target, ipaddr, args.packetsize))
    for i in range(args.count):
        sock.request()
