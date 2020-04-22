from selenium import webdriver
import sys
import os, json

"""
Rahat Hossain
Date: 23-4-2020

I find This code hard to comment 
"""

def start(email, password):
	browser = webdriver.Chrome()
	browser.get("http://lightoj.com/index.php")
	browser.find_element_by_css_selector('#myuserid').send_keys(email)
	browser.find_element_by_css_selector('#mypassword').send_keys(password)
	browser.find_element_by_css_selector('body > div:nth-child(3) > form > input[type=submit]').click()
	browser.get("http://lightoj.com/volume_usersubmissions.php")
	browser.find_element_by_css_selector('#mytable2 > tbody > tr:nth-child(3) > td > input[type=password]').send_keys(password)
	browser.find_element_by_css_selector('#content > form > input[type=submit]').click()	
	haha = browser.find_element_by_css_selector("#mytable3").find_elements_by_tag_name('tr')
	submission = []
	for row in haha:
		cols = row.find_elements_by_tag_name('td')
		if(len(cols) == 0):
			continue
		if(cols[-1].text == 'Accepted'):
			submission.append(row.find_elements_by_tag_name('th')[0].text)
	solutios = {}
	for each in submission:
		browser.get("http://lightoj.com/volume_showcode.php?sub_id=" + each)
		name = browser.find_element_by_css_selector('#mytable3 > tbody > tr:nth-child(2) > td:nth-child(4)').text.strip()
		code = browser.find_element_by_css_selector('ol').text.strip()
		if solutios.get(name) == None:
			solutios[name] = []
		solutios[name].append(code)
	return solutios

def save(result):
	if not os.path.exists('Solution'):
		os.mkdir('Solution')
	for name in result:
		solutios = result[name]
		if not os.path.exists('Solution/' + name):
			os.mkdir('Solution/' + name)
		count = 0
		for solution in solutios:
			filename = 'Solution/' + name + '/' + name
			if count == 0:
				filename += ".cpp"
			else:
				filename += "({0}).cpp".format(count)
			count += 1
			with open(filename, 'w') as file:
				file.write(solution)


if __name__ == "__main__":
	try:
		save(start(sys.argv[1], sys.argv[2]))
	except:
		print("Process halted")