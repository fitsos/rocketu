var fbAccessToken;
window.fbAsyncInit = function() {
	FB.init({
		appId      : '547589258628474', // App ID
		channelUrl : '//bootcamp.rocketu.com/channel.html', // Channel File
		status     : true, // check login status
		cookie     : true, // enable cookies to allow the server to access the session
		xfbml      : true  // parse XFBML
	});
	FB.Event.subscribe('auth.authResponseChange', function(response) {
		console.log(response); 
		if (response.status === 'connected') {
			alreadyConnected = true;				
			fbAccessToken = response.authResponse.accessToken;
			login();
		} else if (response.status === 'not_authorized') {
			FB.login(function(response) {
			},{ scope: 'email,user_likes,friend_likes' });
		} else {
			FB.login(function(response) {			
			},{ scope: 'email,user_likes,friend_likes,user_education_history' });
		}
	});
};
// Load the SDK asynchronously
(function(d){
	var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
	if (d.getElementById(id)) {return;}
	js = d.createElement('script'); js.id = id; js.async = true;
	js.src = "//connect.facebook.net/en_US/all.js";
	ref.parentNode.insertBefore(js, ref);
}(document));
/* HARDER WAY TO CALL GRAPH API
	$.ajax({
		url: 'https://graph.facebook.com/me',
		dataType: 'json',
		data: {
			access_token: fbAccessToken
		},
		success: function(json) {
			console.log('Doing it the hard way');
			console.log(json);
		}
	});
*/
function login() {
    console.log('Welcome!  Fetching your information.... ' + response.name);
    if(localStorage['response']) {
        console.log('user is in local storage')
        console.log(JSON.parse(localStorage['response']));
    } else {
        console.log('getting user info from api')
        getFriendsInfo();
    }
    if(localStorage['m']) {
        console.log('localStorage has music_data');
        console.log(localStorage['music_data']);
        console.log('****************************');
    } else {
        getMe();
    }
    if(localStorage.location) {
        console.log('localStorage has location data');
        console.log(localStorage.location);
        console.log('****************************');
    } else {
        navigator.geolocation.getCurrentPosition(saveUserLoc);
    }
}
function getMe() {
    FB.api('/me', function(response) {
        // console.log(response);
        myName = response.name;
        // var imgSrc = 'https://graph.facebook.com/' +response.username+'/picture?type=normal';
        // $('#picture').append($('<h3/>').html(name));
        // $('#picture').append($('<img/>').attr('src', imgSrc));
        getMyMusic();
    });
}
// function getMyMusic() {
//     FB.api('/me/music', function(response) {

//         var bands = [];
//         for(var k in response.data) {
//             if(response.data[k].category === 'Musician/band') {

//                 // band object as it will be defined in local storage

//                 var band = {
//                     'name': response.data[k].name,
//                     'img': '',
//                     'id': '',
//                     'terms': [],
//                 }
//                 bands.push(band);
//             }
//         }

//         var user = {
//             'username': myName,
//             'bands': bands
//         };

//         // TODO: put this into a seperate func later
//         localStorage['music_data'] = JSON.stringify(user);
//         console.log('we just hit the facebook api')
//     });
// }

// function getMusicInfo(user) {

//     console.log('--- Getting Music');
//     if (!user) {
//         user = 'me';
//     }

//     friend_bands = {
//         name: user,
//     }

//     FB.api('/'+user+'/music',function(response) {
//         var result = [];
//         var objs = response.data;
//         for(var k in objs) {
//             if(objs[k].category==='Musician/band') {
//                 var band = objs[k].name;
//                 result.push(band);
//             }
//         }
//         friend_bands[user] = result;
//         friendsApiCalls[user] = true;
//         console.log(user + ' DONE');
//     });
// }
function getFriendsInfo() {
    /*
        Goal: get music interests from user's friends
        Logic:
            1. get user's friends
            2. for each of the friends get their music interests - bands/artists names
            3. return a mapping of friends and their list of bands/artists names
    */
    console.log('*** Getting Friends');
    FB.api('me/friends', function(response) {
        // console.log(response);

        for(var k in response.data) {

            var id_friend = response.data[k].id;
            var name_friend = response.data[k].name;
            // var friend_img_url = '<img src="https://graph.facebook.com/'+id_friend+'/picture?type=normal"/>';
            friendsApiCalls[id_friend] = false;
            getMusicInfo(id_friend);
        }
        printMusicInfo();
    });
}
function saveUserLoc(position) {
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
    var latlng = {
        lat: lat,
        lng: lng
    }
    localStorage['location'] = JSON.stringify(latlng);
    console.log(localStorage['location'])
}
$(document).ready(function() {
    $('#logout').on('click', function() {
      FB.logout(function(response) {
        // log out
      });
    });
});