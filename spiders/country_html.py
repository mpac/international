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


import csv, gzip, ucsv, urllib2, time
from StringIO import StringIO

max = 0

input = open('./country_links.csv', 'r')
reader = ucsv.reader(input, csv.excel_tab)

count = 0

for row in reader:
	count += 1

	url = 'http://en.wikipedia.org' + row[1]
	print url

	request = urllib2.Request(
	 	url, headers = {'User-Agent': 'manytopics/international'}
	)

	response = urllib2.urlopen(request)

	if response.info().get('Content-Encoding') == 'gzip':
    		buffer = StringIO(response.read())
		file = gzip.GzipFile(fileobj=buffer)
		data = file.read()
	else:
		data = response.read()

	file_name = 'countries/' + row[1][6:] + '.html'

	output = open(file_name, 'w')
	output.write(data)

	time.sleep(5)

	if max > 0 and count >= 5:
		break

