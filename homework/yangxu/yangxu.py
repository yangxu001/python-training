#!/usr/bin/python
#coding:utf-8
import requests
import json
import os

class datacapture:

	def __init__(self):
		pass

	def capture(self):
		global list1
		list1=[]
		url1=requests.get('https://jsonplaceholder.typicode.com/users')
		bbb=url1.json()
		#print bbb
		for i in bbb:
			dict1={}
			#print i
			#print str(i['username'])
			#print str(i['id'])
			dict1['name']=str(i['name'])
			dict1['id']=str(i['id'])
			#print dict1
			list1.append(dict1)
		print list1
	def capture1(self):
		global list2
		list2=[]
		url2=requests.get('https://jsonplaceholder.typicode.com/posts')
		ddd=url2.json()
		#print ddd
		for j in ddd:
			#print j
			dict2={}
			#print str(j['title'])
			#print str(j['id'])
			dict2['title']=str(j['title'])
			dict2['id']=str(j['userId'])
			#print dict2
			list2.append(dict2)
		print list2

class datacleaning:

	def cleaning(self):
		global list3
		list3=[]
		for m in list1:
			
			#print m
			for n in list2:
				dict3={}
				if m['id']==n['id']:
					dict3['name']=m['name']
					dict3['title']=n['title']
					list3.append(dict3)
		print list3
class writefile:
	def __init__(self,title,name):
		self.title=title
		self.name=name

	def show(self):
		print "标题：%s，作者：%s" %(self.title,self.name)
		file_object=open('test.txt','a')
		file_object.write("标题：%s，作者：%s\n" %(self.title,self.name))
		file_object.close()



print hellooo55
aaa=datacapture()
aaa.capture()
aaa.capture1()
aaa1=datacleaning()
aaa1.cleaning()
#os.remove('test.txt')
for p in list3:
	aaa2=writefile(str(p['title']),str(p['name']))
	aaa2.show()


