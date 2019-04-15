import requests
import re

f = open('C:/Users/FLY/Desktop/doupo2.txt', 'a+', encoding='utf-8') #在桌面创建并以读写方式打开文件，若存在文件，将会以追加的形式，并且定义编码


urls = ['https://m.doupocangqiong1.com/1/{}.html'.format(str(i)) for i in range(1921, 1922)] #构建url

#进行迭代，获取文本
for url in urls:
    res = requests.get(url) #发送请求
    title = re.findall('<h1 class="title">(.*)</h1>', res.content.decode('utf-8'), re.S)[0] #用正则匹配每一章的标题
    contents = re.findall('<div id="articlecon" class="articlecon"><p>(.*)</p></div>', res.content.decode('utf-8'), #用正则匹配每一章的内容
                          re.S)
    contentsss = re.compile(r'<[^>]+>', re.S)
    result = contentsss.sub('', ';'.join(contents)) #借助sub（）修改文本
    f.write(title + '\n\n') #写入标题
    f.write(result + '\n\n') #写入内容



