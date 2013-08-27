$(document).ready(function() {
	console.log('document ready');
	$('#here').html('*through the DOM!');
	$.ajax(
		{
			type:"GET",
			url:"http://bootcamp-rocketu.rhcloud.com/exercises/ajax/data/places-restaurant.json",
			data: {},

			dataType: "json",
			success: function(json) {
						console.log(json);
						console.log('ajax success');
						$('#here').append(Mustache.render( $('#bar-template').html(), json) );
			// 			for (i = 0; i < json.length; i++) {
			// 				$('#here').append("<img src=" + json[i].icon + "> " + "<br/>" +
			// 								"<li/>" + json[i].name + "<br/>" +
			// 								" " + json[i].vicinity + "<br/>" + 
			// 								"rating: " + json[i].rating + ", " +
			// 								"price level: " + json[i].price_level + " , "  );
			// 			}
			// 				console.log(json[0].types[0]);
			// 			for (i = 0; i < json.length; i++) {
			// 				for (k = 0; k < json[i].types[k].length; k++)
			// 					$('#here').append(json[i].types[k] + ", " );
			// 			}

			}, 
		}
	);
	return false;
});





















































// $(document).ready(function() {

// 	$('form').('submit',function() {
// 		var firstname = $(this).find('input#firstname').val();
// 		var lastname = $(this).find('input#lastname').val();
// 		console.log(firstname + ' ' + lastname);
		
// 		$.ajax(
// 			{
// 				url: 'http://bootcamp-rocketu.rhcloud.com/exercises/ajax/data/places-restaurant.json',
// 				type: 'POST',
// 				dataType: 'json',
// 				data: {
// 					fname: firstname,
// 					lname: lastname,
// 					date: (new Date())
// 				},
// 				success: function(json) {
// 					console.log(json);
// 					// DO SOMETHING HERE
	
// 				}
// 			}
// 		);
		
// 		return false;
// 	});