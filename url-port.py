import urllib.request
import urllib.error
import socket  
from threading import Thread  
import time  

f = open("url.txt")    #带http:// 的未经筛选url
start_time = time.time()
url = []              
for line in f.readlines():       
    tmp = line.replace('\n','')    #数据处理
    url.append(tmp)              
f.close()                       
print("————默认端口请求-开始遍历url————")
for tmpurl in url:               
    try:                         
        req = urllib.request.Request(tmpurl)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
        resp = urllib.request.urlopen(req,timeout=2)    
        code = resp.getcode()                          
        print(tmpurl,":",code)
        if code == 200:    
            ab = tmpurl.replace('http://','')
            bc = ab.replace('https://','')   
            m = open('200ok.txt', 'a')      
            m.write(bc)
            m.write("\n")
            m.close()  
    except urllib.error.URLError as e:
        continue                     
    except urllib.error.HTTPError as e:
        continue            
print("————<<以上为200ok存活结果>>————")
s = open("200ok.txt")
def main():
    print("[*]——————开始对各个有效目标进行端口扫描 ： %s ——————————" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    for line in s.readlines(): 
        target = line.replace('\n','')
        for port in range(1, 10000):  
            t = Thread(target=portscan, args=(target, port))  
            t.start()  
    s.close()
def portscan(target, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        client.connect((target, port))  
        print("[*] %s =>%d  端口开放" % (target, port))
        with open(target+"-port.txt", "a") as f:
            f.write("%s:%d\n" % (target, port))
        client.close()
    except:
        pass
if __name__ == "__main__":
    main()
    end_time = time.time()
    print("[*] ——————扫描完成共耗时： %.2f 秒" % (end_time - start_time),",扫描结束——————")
    print("各存活目标端口探测结果已自动生成文档")

