$(document).ready(function() {		
	$.ajax(
		{

			type: 'GET',
			url: 'https://www.thegivinglab.org/api/charities/',
			data: {
				apikey: '3ef2ea81-93fb-431b-b8c3-92b0604da5eb'	
			},

			dataType: 'json',
			success: function(json) {
				console.log(json);
				// DO SOMETHING HERE

			}
		}
	);
});

$(document).ready(function() {
	console.log('document ready!');
	$('#events').html('Content through the DOM');
	// GET https://www.thegivinglab.org/api/charities/[3ef2ea81-93fb-431b-b8c3-92b0604da5eb]
});
