import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from os import walk

def get_report_links():
	"""Get a list of links to individual articles from each available page of alerts."""
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
	"""Get article text for each report."""
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

def compileData():
	"""Compile report text files into a single JSON file."""
	# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
	read_path = "reports/"
	_, _, filenames = next(walk(read_path))
	reports = []
	for filename in filenames:
		try:
			with open(read_path + filename) as f:
				report = {
					'metadata': {},
					'incidents': [],
					'resolution': {}
				}
				text = f.read().strip()
				sections = text.split('\n\n')
				for i in range(len(sections)):
					obj = {}
					for line in sections[i].split('\n'):
						split = line.split(': ')
						attribute = split[0]
						value = ': '.join(split[1:])
						if (value == 'True' or value == 'False'):
							value = (value == 'True')
						if attribute in obj:
							obj[attribute] = [obj[attribute]]
							obj[attribute].append(value)
						else:
							obj[attribute] = value
					if i == 0:
						report['metadata'] = obj
					elif i == 1:
						report['incidents'].append(obj)
					else:
						if 'INCIDENT DESCRIPTION' in obj:
							report['incidents'].append(obj)
						else:
							report['resolution'] = obj
				reports.append(report)
		except:
			print(f'Could not read {read_path + filename}.')
	write_path = 'reports.json'
	try:
		with open('reports.json', 'w') as f:
			json.dump(reports, f, indent=2)
			print(f'Successfully wrote to {write_path}.')
	except:
		print(f'Could not write to {write_path}.')

def main():
	# get_report_links()
	# get_report_articles()
	compileData()

if __name__ == '__main__':
	main()