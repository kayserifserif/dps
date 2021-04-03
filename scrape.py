import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

def get_report_links():
	url = 'https://dps.usc.edu/category/alerts/'
	links = []
	page = 1
	while True:
		try:
			r = requests.get(url + 'page/' + str(page))
			r.raise_for_status()
		except requests.exceptions.HTTPError as e:
			break
		soup = BeautifulSoup(r.text, 'html.parser')
		anchors = soup.select('.entry-header .entry-title a')
		for anchor in anchors:
			links.append(anchor['href'])
		print(f'Page {page} ({len(anchors)} links)')
		page += 1
	filename = 'reports.txt'
	try:
		with open(filename, 'w') as f:
			f.writelines('\n'.join(links))
	except:
		print(f'Could not read {filename}.')

def get_report_articles():
	with open('reports.txt') as f:
		links = f.read().split('\n')
	for link in links:
		print(link)
		stub = link.split('/')[-2]
		try:
			r = requests.get(link)
			r.raise_for_status()
		except requests.exceptions.HTTPError as e:
			break
		soup = BeautifulSoup(r.text, 'html.parser')
		article = soup.article
		text = article.h1.string + '\n' + article.time['datetime'] + '\n' + link + '\n\n'
		content = article.select('.entry-content p')
		for p in content:
			text += ' '.join(p.stripped_strings).strip() + '\n'
		filename = 'reports/' + stub + '.txt'
		try:
			with open(filename, 'w') as f:
				f.write(text)
		except:
			print(f'Could not write to {filename}.')

def main():
	# get_report_links()
	get_report_articles()

if __name__ == '__main__':
	main()