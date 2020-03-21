#!/usr/bin/python3
from urllib.parse import urlparse
from whois import whois
from datetime import datetime
from urllib.request import urlopen
from socket import getaddrinfo
from error_debug import result_debug_type
from error_debug import errors_run_log

def dns_basicScan():
    with open("urlOrg_addr","r",encoding='utf_8') as orgs:
        text_list=orgs.readlines()
    for url in text_list:
        res=urlparse(url)
        who=whois(res.netloc)
        with open("domain_{}.log".format(datetime.now().strftime('''%Y-%m-%d''')),"a") as tag:
            tag.write(str(datetime.now().strftime('''%Y-%m-%d %H:%M:%S'''))+'\n')
            tag.write(str(who)+'\n')
            tag.write("-----------------------------------result_end-----------------------\n")

def domain_check(dns_list):
    for dns in dns_list:
        results=urlopen('http://panda.www.net.cn/cgi-bin/check.cgi?area_domain={}'.format(dns))
        with open("domainCheck_result.log","a") as tage:
            tage.write(str(datetime.now().strftime('''%Y-%m-%d %H:%M:%S'''))+'\n')
            tage.write(str(results.read().decode()))

def getIP(doMain):
    try:
        myAddr=getaddrinfo(doMain,'http')
        ip_addr=myAddr[0][4][0]
        return ip_addr
    except:
        errors_run_log()
        results=result_debug_type()
        return results

from socket import gethostbyname
def get_ICMP():
    try:
        by_var=gethostbyname("baidu.com")
        return by_var
    except:
        errors_run_log()
        results=result_debug_type()
        return results

def get_ip_list(domain):
    ip_list=[]
    try:
        addrs=getaddrinfo(domain,None)
        for item in addrs:
            if item[4][0] not in ip_list:
                ip_list.append(item[4][0])
    except Exception as e:
        print(str(e))
    return ip_list

def main():
    dns_lists=['baidu.com','sina.com.cn','yahoo.com','naver.com','navers.cn']
    try:
        for itr in get_ip_list(domain='baidu.com'):
            print(itr)
        for iter in dns_lists:
            print(iter)
            for itm in get_ip_list(domain=iter):
                print(itm)
        domain_check(dns_list=dns_lists)
        dns_basicScan()
    except:
        errors_run_log()
        result_err=result_debug_type()
        print(result_err)
if __name__ == "__main__":
    main()