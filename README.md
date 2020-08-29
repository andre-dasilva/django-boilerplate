# Django Boilerplate

This project contains a django app with boilerplate code, that could be used in real world application.

The goal is, that anyone could grab a feature like logging, rest framework, settings management, etc. and paste it into their project.

The **inspiration** for this project is the Python Zen Code: 
> There should be one-- and preferably only one --obvious way to do it.

There are a lot of boilerplate projects already, but this one should cover a lot of common needs in a project, especially for newcomers to django.

## Dependencies

This project contains the following django packages:
* [Django](https://www.djangoproject.com/)
* [REST Framework](https://www.django-rest-framework.org/)
* [Debug Toolbar](https://github.com/jazzband/django-debug-toolbar) 
* [Environ](https://github.com/joke2k/django-environ)

## Content

So far this project contains the following features:

- [x] Dependency management with [https://python-poetry.org/](https://www.djangoproject.com/) 
- [x] Settings management for multiple environments (e.q development, production etc.)
- [x] logging to console and to file example
- [x] Custom user model with e-mail address
- [x] Two small apps (Task and User) with models and One-To-Many relationship
- [x] Basic REST framework example
- [x] Basic MVC example with template
- [ ] Basic settings needed (e.q ADMINS, CSRF, SESSION, EMAIL, etc.)
- [ ] Handling forms with Django and normal forms
- [ ] All model relationships
- [ ] Classed based views and function based views example
- [ ] Static File handling
- [ ] Media File handling
- [ ] File upload
- [ ] REST different responses (xml, json)
- [ ] E-Mail support (register, 500 error mail to admins, etc.)
- [ ] User management
- [ ] Authentication REST (OAuth, JWT)
- [ ] Authentication Session Based (MVC)
- [ ] Database (MySQL, PostgreSQL)
- [ ] NoSQL (MongoDB, CouchDB)
- [ ] Other security (CSRF, XSS, etc.)
- [ ] Documentation
- [ ] Pagination
- [ ] Sorting
- [ ] Filtering
- [ ] Testing and code coverage
- [ ] Web Sockets (with Signals e.q Chat application)
- [ ] multiple languages with translations
- [ ] Task Queue (e.q with Celery and Redis)
- [ ] Caching (e.q with Redis or Memcache) 
- [ ] Async in django
- [ ] django system checks
- [ ] Docker support
- [ ] REST HATEOAS
- [ ] SSL
- [ ] and more ...

