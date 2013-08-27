// # Create a WebContent object
// url = 'http://google.com/ig/modules/datetime.xml'
// web_content = gdata.calendar.data.WebContent(url=url, width='300', height='136')
// web_content.web_content_gadget_pref.append(
//     gdata.calendar.data.WebContentGadgetPref(name='color', value='green'))

// # Create a WebContentLink object that contains the WebContent object
// title = 'Date and Time Gadget'
// href = 'http://www.google.com/calendar/images/google-holiday.gif'
// type = 'application/x-google-gadgets+xml'
// web_content_link = gdata.calendar.data.WebContentLink(title=title, href=href,
//     link_type=type, web_content=web_content)

//load a stable version and wait till the page loads to call it
google.load("gdata", "1");
google.setOnLoadCallback(getMyFeed);
var myService;
var feedUrl = "https://www.google.com/calendar/feeds/fitsos21@gmail.com/private/full";
function setupMyService() {
  myService = new google.gdata.calendar.CalendarService('exampleCo-exampleApp-1');
}
function getMyFeed() {
  setupMyService();
  myService.getEventsFeed(feedUrl, handleMyFeed, handleError);
}
function handleMyFeed(myResultsFeedRoot) {
  alert("This feed's title is: " + myResultsFeedRoot.feed.getTitle().getText());
}
function handleError(e) {
  alert("There was an error!");
  alert(e.cause ? e.cause.statusText : e.message);
}

google.gdata.client.init()
google.gdata.client.init(handleInitError)