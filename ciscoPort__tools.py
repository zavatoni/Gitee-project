#!/usr/bin/python3
from telnetlib import Telnet
from error_debug import errors_run_log
from error_debug import result_debug_type

def ciscoLogin_loopback_check(Host,User,Passwd):
    tn = Telnet(Host)
    tn.read_until("Username: ")
    tn.write(User + "\n")
    tn.write(Passwd + "\n")

    tn.write("enable\n")
    tn.write("cisco\n")
    tn.write("conf t\n")
    tn.write("hostname saya_tampan\n")

    for x in range(1,10):
        tn.write("interface loopback{}\n".format(x))
        tn.write("description FROM_TELNET_SCRIPT\n")
        tn.write("ip address 1.1.1.{} 255.255.255.255\n".format(x))
    tn.write("exit\n")
    tn.write("end\n")
    tn.write("exit\n")

    return tn.read_all()
from yaml import dump
def userAccount_tool(host,user,passwd):
    userSeq=list()
    if len(host) >0 and len(user)>0 and len(passwd)>0:
        userSeq.append(host)
        userSeq.append(user)
        userSeq.append(passwd)
    userInfo=['host','user','passwd']
    userSum=dict(
        zip(userInfo,userSeq)
    )
    return userSum

def input_tage():
    ua_seq=list()
    while True:
        ua_results=userAccount_tool(
            host=input("请输入一个主机地址："),
            user=input("请输入用户名称:"),
            passwd=input("请输入符合密码格式的有效密码:")
        )
        ua_seq.append(ua_results)
        with open("UA_info.yml","a") as ua_info:
            ua_info.write(dump(ua_seq))
        stops=input("如果完成输入Q一下:")
        if str(stops)=='q':
            break
from yaml import load
import yaml
def main():
    try:
        input_tage()
        with open("UA_info.yml","r",encoding="utf8") as ua_load:
            for context in load(ua_load,Loader=yaml.FullLoader):
                print(context)
    except:
        errors_run_log()
        print(result_debug_type())
if __name__ == "__main__":
    main()