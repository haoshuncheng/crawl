"""

抓取妹子图 



"""

import requests
from lxml import etree
import sys
import os
import urllib.request
import re

#获取 页面 html内容
def getTypeHtml(url):
	return requests.get(url).text

def parseZhuanti(html) :
	r = etree.HTML(html)
	murl =r.xpath('//dl/dd/a/@href')
	mtype = r.xpath('//dl/dd/a/text()')
	# mpic = r.xpath('//dl/dd/a/img/@src')
	# print(murl)
	# sys.exit()
	for index, url in enumerate(murl):
		if index == 0 or index ==1:
			continue
		typeName = '../meizitu/'+mtype[index]
		# print(typeName)
		# continue
		# os.makedirs()
		getname(url,typeName)

def getname(url,typeName):
	# print(url)
	# sys.exit()
	html = etree.HTML(getTypeHtml(url))
	page_numbers = html.xpath('//div[@class="nav-links"]/a[last()-1]/text()')
	if not len(page_numbers):
		pass
	else:
		for x in range(1,int(page_numbers[0])+1):
			url2 = url+'page/'+str(x)+'/'
			url3 = etree.HTML(getTypeHtml(url2)).xpath('//ul[@id="pins"]/li/a/@href')
			# title3 = etree.HTML(getTypeHtml(url2)).xpath('//ul[@id="pins"]/li/a/img/@alt')
			getPic(url3,typeName)

def getPic(url,typeName):
	# print(url)

	# print(title)

	# return
	for i, u in enumerate(url):
		# print(i,u)
		# sys.exit()
		# continue
		# if len(title) <= i:
			# continue

		paths =typeName+'/'+u.split('/')[-1]

		if os.path.exists(paths):
			print(paths)
			continue
		# if title[i] == '怎一个”大”字了得 性感尤物赵伊彤情趣写真露妖艳大奶':
		# paths = re.sub(r'”|“| ',"",paths)
		# print(paths)
		# sys.exit()
		# continue
		# continue;

		# path = path
		# path = re.sub('')
		# path = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"),path) 
		# print(path)
		# return

		try:
			os.makedirs(paths)
		except Exception as e:
			print(e)
		# print(u)
		# return
		html = etree.HTML(getTypeHtml(u))
		page_numbers = html.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()')
		# print(page_numbers)
		# continue
		if not len(page_numbers):
			pass
		else:
			zz = 0;
			for x in range(1, int(page_numbers[0])+1):
				# print(x)
				# print(u)
				# continue
				upic = u+'/'+str(x)
				pic = etree.HTML(getTypeHtml(upic)).xpath('//div[@class="main-image"]/p/a/img/@src')
				print(paths+pic[0])
				# print(pic)

				if os.path.exists(paths+"/"+str(zz)+".jpg"):
					zz+= 1
					continue


				opener = urllib.request.build_opener()
				headers = ('Referer',u)#防盗链，修改访问来源   
				opener.addheaders = [headers]
				data = opener.open(pic[0]).read()
				with open(paths+"/"+str(zz)+".jpg", "wb") as code:       
					code.write(data)    
				zz += 1
				# sys.exit()
				# urllib.request.urlretrieve(pic[0],path+"/"+str(zz)+".jpg")
				# sys.exit()

		# print()

	







if __name__ == '__main__':
	# parseTypeHtml()
	html = getTypeHtml('http://www.mzitu.com/zhuanti/')
	parseZhuanti(html)
	# path = '怎一个”大”字了得性感 尤物赵伊彤情趣写真露妖艳大奶';
	# print(path)
	# print("\n")
	# print("aaaa")
	# print(re.sub(r'”|“| ',"",path))