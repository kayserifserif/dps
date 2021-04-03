from os import walk
from pprint import pprint
import json

def compileData():
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
	compileData()

if __name__ == '__main__':
	main()