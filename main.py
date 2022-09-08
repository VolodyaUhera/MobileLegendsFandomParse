'''
requests
B4s python
На вхід url сторінка на вихід список url з героями
'''
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


def main():

	url = 'https://mobile-legends.fandom.com/wiki/List_of_heroes'
	res = requests.get(url)

	#status_code = res.status_code
	#print(status_code)

	AllLincks = []

	soup = BeautifulSoup(res.text, "lxml")

	AllLincks = soup.select('table', class_='wikitable sortable jquery-tablesorter')

	AllLincks = soup.select("tr > td > b > a[href]")
	
	AllLincksTITLE = []
	href = []
	
	for link in AllLincks:
		AllLincksTITLE.append(link.get('title'))
		href.append(link.get('href'))

	#href_and_title = {'href': href, 'title': AllLincksTITLE}

	#print (href_and_title)

	"""for link in href_and_title:
					#print(href_and_title)
					df = pd.DataFrame(href_and_title)
					df.to_csv (r'test2.csv', index = False, header=True)   #test2.csv
				"""
	

	#FinalTABLE = df.to_csv ('D:\\WORKASPACE\\WORKSPACEold\\PythonParse\\main')

	'''with open ('test1.csv', 'w') as f:									#test1.csv
					for key in href_and_title.keys():
						f.write("%s, %s\n" % (key, href_and_title[key]))'''


	fieldnames = ['href','title']
	href_and_title = [{'href': href, 'title': AllLincksTITLE}]

	'''with open ('test3.csv', 'w') as f:
		i = csv.DictWriter(f, fieldnames=fieldnames,)
		i.writeheader()
		for link in href_and_title:
			i.writerows(href_and_title)'''

	with open ('test4.csv', 'a') as f:
		w = csv.writer(f)
		w.writerow(
			(
				href,
				AllLincksTITLE
			)
		)









if __name__=='__main__':
		main() 
	
	


	











