$(document).ready(function() {		
	$.ajax(
		{
			type: 'GET',
			url: 'http://proxy-rocketu.rhcloud.com/rocketu-api/',
			data: {
			// cat=16&new=n&rss=1&sort=0&srad=85.0&srss=50&st=event&st_select=event&swhat=charity&swhen=&swhere=San+Francisco%2C+CA
				'url': 'http://events.sfgate.com/search',
				'cat': 16, // Charity Events,
				'new': 'n', // new listing or not
				'rss': 1, // RSS
				'sort': 0, // SORT
				'srad': 85, // search radius, e.g. 85 miles
				'srss': 50, // search results number, e.g. 50 results
				'st': 'event', // search type
				'st_select': 'event', // search type selected
				'swhat': 'charity', // search what
				'swhen': '', // search when
				'swhere': 'San Francisco, CA' // search where
			},
			//xml to json
			dataType: 'xml',
			success: function(xml) {
				console.log(xml);
				var items = $(xml).find('item');
				var json = [];
				for(var i=0; i<items.length; i++) {
					var jsonItem = {};
					$(items[i]).children().each(function() {
						jsonItem[this.tagName] = $(this).text();
					});
					json.push(jsonItem);
				}
				console.log(json);
				console.log(json[0].id);
				$('#events').append( Mustache.render( $('#events-template').html(), json) );
/*
				console.log(items);
				console.log($(items[0]).find('title').text());
				for(var i=0; i<items.length; i++)
				{
					$('#events').append('<p>' + $(items[i]).find('title').text() + '</p>');	
}*/
			}
		}
	);

});
