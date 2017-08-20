# VRblog
A django/wagtail app for a Virtual Reality Blog using A-Frame.
A-Frame is a JavaScript library that lets you embed VR into HTML tags!

In a first phase I followed Wagtail tutorial for setting up a blog app, then I
started implementing the VR part.
The vrblog_base.html holds all the invariant parts of the A-Frame tags.
vrblog_page.html extends the base. By now it's just a room with the title, intro,
date and body template tags associated to the front wall.
