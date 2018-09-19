# 此脚本用来快速构建Python爬虫参数header,使用方法：
# 将Chorme浏览器inspect功能下的Request Headers下的项目全选粘贴赋值给字符串变量headerStr，然后运行程序，结果直接输出为最终可以粘贴赋值给header变量的字典类型，比一个一个加上引号要方便多了，当然这个脚本也可以应用到参数data上面

headerStr = '''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: max-age=0
Cookie: __mta=20346247.1537346195910.1537350613375.1537355600245.11; uuid_n_v=v1; uuid=1D2D2EE0BBE711E8A9292B3EF07D935BD00F4DA523C7439EAAAE51C465FB7012; _lxsdk_cuid=165f0f9517ac8-098b7cef681378-8383268-144000-165f0f9517bc8; _lxsdk=1D2D2EE0BBE711E8A9292B3EF07D935BD00F4DA523C7439EAAAE51C465FB7012; _csrf=f6732a03c18bd7859a066e030e3f90bb7879c4e75cdca25ca9d5e7ca507b69c0; _lxsdk_s=165f188d139-116-490-e6%7C%7C2
Host: maoyan.com
Proxy-Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'''

header = headerStr.replace('\n', "',\n'")
header = header.replace(': ', "': '")
header = "{'" + header + "'}"

print(header)

