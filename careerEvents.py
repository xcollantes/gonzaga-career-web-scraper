# author: Xavier Collantes
# date: 09/02/2018
# purpose: Return upcoming events from Gonzaga University's
# Career & Professional Development's website

import requests, bs4

def scrape(target):
	try:
		re = requests.get(target)
		re.raise_for_status()
		print ("Status Code: %s" %re.status_code)
	except IOError as ioe:
		print ("Problem with scraper: %s" %ioe)

	return re

def parseHtml(response):
	extract = bs4.BeautifulSoup(response.text, features='html.parser')
	mon = extract.select('div.event div.month')
	day = extract.select('div.event div.day')
	title = extract.select('div.event div.title')
	deets = extract.select('div.event span.eventDescription')
	time = extract.select('div.event span.eventDate')
	
	print("Gonzaga Career Center's Upcoming Events: ")
	try: 
		i = 0
		for each in title, mon, day, deets, time:
			print (title[i].getText())
			print (deets[i].getText())
			print (mon[i].getText() + ' ' + day[i].getText())
			print (time[i].getText())
			i += 1
			print ()
	except Exception as ex:
		print()



if __name__ == '__main__':
    link = 'https://www.gonzaga.edu/student-life/career-services'
    
    parseHtml(scrape(target))
    
