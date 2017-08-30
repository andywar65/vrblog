# VRblog
A django/wagtail app for a Virtual Reality Blog using A-Frame.
A-Frame is a JavaScript library that lets you embed VR into HTML tags!

In a first phase I followed Wagtail tutorial for setting up a blog app, then I
started implementing the VR part.

The vrblog_base.html holds all the invariant parts of the A-Frame tags.

Vrblog_index_page.html extends the base. Index page is transformed in a 4x4x3 
room where you can walk around. On the front wall you find the title and intro
template tags. On the right links to indexed posts.
On the left there is no wall, but a window to an equirectangular image. 
On the back wall are three link targets to navigate to the parent, previous and 
next pages.

Vrblog_page.html extends the base. Blog page is transformed in a 4x4x3 room
where you can walk around. On the front wall you find the title, date, intro,
category and tag template tags. On the right an image gallery alternated with text.
On the left there is no wall, but a window to an equirectangular image. 
On the back wall are three link targets to navigate to the parent, previous and 
next pages.
