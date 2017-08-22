# VRblog
A django/wagtail app for a Virtual Reality Blog using A-Frame.
A-Frame is a JavaScript library that lets you embed VR into HTML tags!

In a first phase I followed Wagtail tutorial for setting up a blog app, then I
started implementing the VR part.
The vrblog_base.html holds all the invariant parts of the A-Frame tags.
vrblog_page.html extends the base. Blog page is transformed in a 3x3x3 room
where you can walk around. On the front wall you find the title, date, intro,
and category template tags. On the right an image gallery alternated with text.
On the left the main image in random colors. On the back wall is a link target 
to navigate to the parent page.
