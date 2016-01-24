# ResumeBuilder
A resume building, storing, and searching application

Developed in Python 2.7 using the Django 1.7 framework
Database configuration is for PostgreSQL

Current Status:

The application is fully functional now in terms of resume creation, storage, and searching.

Brief Overview:

We have two public views at /resume/id and /search, and one admin view at /admin.  Currently our resume creation exists within the admin space since we'd like the ability to create and edit to be protected by authentication.  The resume view shows the resume with the given Id and the search view allows us to search by applicant name or skillset.

Current and Ongoing development:

Resume:

Functionally this is done, it displays everything we want to display on the resume page in a readable format.  It takes no input, so nothing fancy happens on the backend here, the work occurs elsewhere.  Future dev on this page will be focused on HTML/CSS and making things pretty.

Search:

The core of this page is done, we can display 0, 1, or more resumes based off our search query, and we can take a variable number of arguments without issues.  However there is more to be done.
1.  Our search query is currently vulnerable to SQL injection.  The current query needs to be replaced with a more secure version, but Django doesn't support prepared statements by default, so we'll have to find an alternative or write our own.
2.  CSS/HTML, because right now it is just ugly
3.  Additional search fields would be nice, like salary range, school, etc.  These are all easily achievable, but I'd like to resolve issue 1 before changing the query any more (the current query is there mostly to prove that it can be done, not that it should be done this way.)

Creation:
I used one of the built in admin templates for the resume creation, but I'd like to eventually create my own given enough time.  This will likely have to wait on some database schema changes as well, since I haven't decided how/where to handle authentication.  Once I do add authentication, we'll also want to look at a login page.

Database:
This is done for now and completely functional.  The only current additions I might make are changes to the applicant model to add a username and password.  Aside from that all the information is where and how I want it, with the correct many-one and one-many relationships (1 user, multi resumes, 1 resume, multi edhistory jobhistory, etc.)
