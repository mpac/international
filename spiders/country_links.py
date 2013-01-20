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


import codecs

from elementtree.ElementTree import ElementTree

input = ElementTree(file='./countries.html')
output = codecs.open('./country_links.csv', 'w', 'utf-8')

countries = []
xpath = '//a'

for element in input.findall(xpath):
	country = element.get('title')
	href = element.get('href')

	if not country:
		continue

	if country in countries:
		continue
	else:
		countries.append(country)

	print country, href
	output.write('%s\t%s\n' % (country, href))

