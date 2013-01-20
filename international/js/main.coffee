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


$ ->
	numCountries = 50

	form1 = $('#form1')
	search = $('#search')

	map = L.map('map').setView [23.5, 0], 2

	L.tileLayer('http://{s}.tile.cloudmade.com/fa6abac8684e4cbf9557c995b6644f0f/997/256/{z}/{x}/{y}.png', {
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
		maxZoom: 18
	}).addTo(map)

	markPlaces = (search) ->
		for country in countries[0...numCountries]
			if country['demonym'] == 'N/A'
				demonym = country['name']
			else
				demonym = country['demonym']
				
			text = "#{demonym} #{search}"
			href = 'http://www.google.com/search?q=' + escape(text)
			link = "Search: <a target=\"_blank\" href=\"#{href}\">#{text}</a>"
		
			L.marker([country['latitude'], country['longitude']])
				.addTo(map)
				.bindPopup(link)
				
	form1.submit ->
		markPlaces search.val()
		return false

