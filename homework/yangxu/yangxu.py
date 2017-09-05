#!/usr/bin/python
#coding:utf-8
import requests
import json

allgroups_id_name = []
allgroups_userid_title = []
allgroups_name_title = []

class DataCapture:
	def capture_userinfo(self):
		global allgroups_id_name
		allgroups_id_name = []
		url = requests.get('https://jsonplaceholder.typicode.com/users')
		userinfo = url.json()
		for i in userinfo:
			eachgroup_id_name = {}
			eachgroup_id_name['name'] = str(i['name'])
			eachgroup_id_name['id'] = str(i['id'])
			allgroups_id_name.append(eachgroup_id_name)

	def capture_articleinfo(self):
		global allgroups_userid_title
		allgroups_userid_title = []
		url = requests.get('https://jsonplaceholder.typicode.com/posts')
		articleinfo = url.json()
		for i in articleinfo:
			eachgroup_userid_title = {}
			eachgroup_userid_title['title'] = str(i['title'])
			eachgroup_userid_title['id'] = str(i['userId'])
			allgroups_userid_title.append(eachgroup_userid_title)

class DataCleaning:
	def cleaning_name_title(self):
		global allgroups_name_title
		allgroups_name_title = []
		for i in allgroups_id_name:
			for j in allgroups_userid_title:
				eachgroup_name_title = {}
				if i['id'] == j['id']:
					eachgroup_name_title['name'] = i['name']
					eachgroup_name_title['title'] = j['title']
					allgroups_name_title.append(eachgroup_name_title)

class WriteFile:
	def __init__(self,title,name):
		self.title = title
		self.name = name

	def show_title_name(self):
		document.write("标题：%s，作者：%s\n" %(self.title,self.name))

def main():
	info = DataCapture()
	info.capture_userinfo()
	info.capture_articleinfo()
	cleaning = DataCleaning()
	cleaning.cleaning_name_title()
	global document
	document = open('title_name.txt','w')
	for i in allgroups_name_title:
		info_title_name = WriteFile(str(i['title']),str(i['name']))
		info_title_name.show_title_name()
	document.close()

main()

