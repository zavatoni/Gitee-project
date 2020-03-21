#!/usr/bin/python3
from telnetlib import Telnet
from error_debug import result_debug_type
# tel_result=Telnet('127.0.0.53',53)
# print(tel_result,type(tel_result))
# 127.0.0.1:631
def telnet_port_check(ip,ports):
    try:
        telTcp=Telnet(ip,ports)
        if len(str(telTcp))==43:
            return "True:端口正常"
    except:
        return result_debug_type()