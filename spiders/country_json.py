# Copyright 2013, Michael Pacchioli.
#
# This file is part of manytopics/international (MT/I).
#
# MT/I is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 3,
# as published by the Free Software Foundation.
#
# MT/I is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MT/I.  If not, see <http://www.gnu.org/licenses/>.

# Please only use these spiders and their derivatives in accordance
# with the terms of service and acceptable use policies of the data
# providers.


import csv, json, ucsv
import lxml.etree

countries = []

links = open('./country_links.csv', 'r')
output = open('./countries.json', 'w')

reader = ucsv.reader(links, csv.excel_tab)

for row in reader:
	error = False

	country = {}
	country['name'] = row[0]

	file_name = 'countries/' + row[1][6:] + '.html'
	data = open(file_name).read()

	tree = lxml.etree.XML(data)

	xpath = "//table/tr/th/a[@title='Demonym']/../../td/a"

	try:
		element = tree.xpath(xpath)[0]
		demonym = element.text
	except:
		print 'DEMONYM EXCEPTION: ' + row[0]
		demonym = 'N/A'

	country['demonym'] = demonym

	xpath = "//span[@class='geo']"

	try:
		element = tree.xpath(xpath)[0]
	except:
		print 'COORDINATE EXCEPTION: ' + row[0]
		error = True

	if error:
		continue

	coordinates = element.text.split(';')

	country['latitude'] = float(coordinates[0])
	country['longitude'] = float(coordinates[1])

	countries.append(country)

output.write(json.dumps(countries, indent = 4))

