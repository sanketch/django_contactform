Django Contact Form
==================

Contact form application that can be used in with any Django Project!

Currently not a package so in order to add this to your project:   

1. Download the zip file and put the contact folder into your Django project directory.   
 
2. Add ``'contact',`` to your settings.py   
 
3. You will need to set an email host. For debug you can print out the email on the console in order to test. For production you will need a service like Mandrill, which has a good basic free plan!  
 
```
#if DEBUG:
#    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#    EMAIL_FILE_PATH = '/messages'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_HOST_USER = 'hostusername'
EMAIL_HOST_PASSWORD = 'password'
DEFAULT_FROM_EMAIL = 'from@example.com'
EMAIL_PORT = 587
```
The repo is a sample project so you can run it in order to give it a try. 
