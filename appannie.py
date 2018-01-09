import requests
from lxml import etree
import sys
def login():
	pass

def getcsrfmiddlewaretoken():
	url = 'https://www.appannie.com/account/login/?_ref=header'
	headers = {"user-agent":'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}
	html = requests.get(url,headers=headers)
	csrfmiddlewaretoken = etree.HTML(html.text).xpath('//input[@name="csrfmiddlewaretoken"]/@value')
	print(csrfmiddlewaretoken)



if __name__ == '__main__':
	getcsrfmiddlewaretoken()


	# Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0