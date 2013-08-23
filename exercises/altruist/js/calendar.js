# Create a WebContent object
url = 'http://google.com/ig/modules/datetime.xml'
web_content = gdata.calendar.data.WebContent(url=url, width='300', height='136')
web_content.web_content_gadget_pref.append(
    gdata.calendar.data.WebContentGadgetPref(name='color', value='green'))

# Create a WebContentLink object that contains the WebContent object
title = 'Date and Time Gadget'
href = 'http://www.google.com/calendar/images/google-holiday.gif'
type = 'application/x-google-gadgets+xml'
web_content_link = gdata.calendar.data.WebContentLink(title=title, href=href,
    link_type=type, web_content=web_content)