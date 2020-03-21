#!/usr/bin/python3
from telnetlib import Telnet

def ciscoLogin_add_loopBack(host,user,passwd,ip_address,netMask):
    tn=Telnet(host)
    
    tn.read_until("Username: ")
    tn.write(user + "\n")
    
    tn.read_until("Password: ")
    tn.write(password + "\n")

    tn.write("conf t\n")
    tn.write("int lo0\n")
    tn.write("ip address {} {}\n".format(ip_address,netMask))
    tn.write("end\n")
    tn.write("exit\n")

    with open("add_loopback.log","a") as loops:
        loops.write(str(tn.read_all()))

def ciscoLogin_loopBack_loop(host,user,passwd):
    tn=Telnet(host)

    tn.read_until("Username: ")
    tn.write(user + "\n")

    tn.read_until("Password: ")
    tn.write(password + "\n")

    tn.write("conf t\n")
    for x in range (1,11):
        tn.write("int lo{}\n".format(x))
        tn.write("ip address 1.0.0.{} 255.255.255.255\n".format(x))
    tn.write("end\n")
    tn.write("exit\n")

    with open("loopback_loop.log","a") as loops:
        loops.write(str(tn.read_all()))

def mutiple_dev_loopBackup(host_list,user,passwd):
    for host in host_list:
        tn=Telnet(host)

        tn.read_until("Username:")
        tn.write(user+"\n")

        tn.write("conf t\n")
        for x in range(1,11):
            tn.write("int lo{}\n".format(x))
            tn.write("ip address 1.0.0.{} 255.255.255.255\n".format(x))
        tn.write("end\n")
        tn.write("exit\n")

        with open("add_loopback.log","a") as loops:
            loops.write(str(tn.read_all()))

from json import dumps
def exam_test():
    hosts_list=[]
    user_info=['10.10.20.13','tage_user','tage_password']
    hosts_page=['ip_address','user','passwd']
    hosts_stor=dict(zip(hosts_page,user_info))
    hosts_list.append(hosts_stor)
    # print(hosts_list)

    tager=['10.10.10.13','tager_user','tager_passwd']
    tag=['ip_address','user','passwd']
    users=dict(zip(tag,tager))
    hosts_list.append(users)

    pager=['10.10.40.33','avg_user','avg_passwd']
    pag=['ip_address','user','passwd']
    useds=dict(zip(pag,pager))
    hosts_list.append(useds)

    return hosts_list

def multiple_ssh_config(host_list,user,passwd):
    for host in host_list:
        tn = telnetlib.Telnet(host)
    tn.read_until("Username:")
    tn.write(user+'\n')

    tn.read_until("Password:")
    tn.write(passwd+'\n')

    tn.write("conf t\n")
    for x in range(1,4):
        tn.write("ip domain-name mydomain{}.local\n".format(x))
        tn.write("crypto key generate rsa modulus 1024\n")
        tn.write("line vty 0 4\n")
        tn.write("login local\n")
    tn.write("end\n")
    tn.write("write\n")
    tn.write("exit\n")

    with open("multiple_ssh_conf.log","a") as ssh_multip:
        ssh_multip.write(str(tn.read_all()))
def main():
    pass
def main_exam():
    #批量处理部分：
    hostSeq=exam_test()
    for itm in hostSeq:
        ciscoLogin_add_loopBack(
            host=itm['ip_address'],
            user=itm['user'],
            passwd=itm['passwd'],
            ip_address='1.1.1.1',
            netMask='255.255.255.255'
        )
        ciscoLogin_loopBack_loop(
            host=itm['ip_address'],
            user=itm['user'],
            passwd=itm['passwd']
        )

def main_core():
    #org_basic:
    ciscoLogin_add_loopBack(
        host="10.10.10.1",
        user="dhar_user",
        passwd="moPasswd",
        ip_address='1.1.1.1',
        netMask='255.255.255.255'
    )        
    #Alter update V1--------------------------------------
    ciscoLogin_loopBack_loop(
        host="10.10.20.1",
        user="tager_user",
        passwd="moPasswd"
    )
    #multiple function module
    hosts_list=['10.10.10.1','10.10.10.2','10.10.10.3','10.10.30.21','10.10.20.13']
    mutiple_dev_loopBackup(
        host_list=hosts_list,
        user='page_user',
        passwd='page_password'
    )
if __name__ == "__main__":
    main()