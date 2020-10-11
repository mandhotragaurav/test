from django.test import TestCase
from django.conf import settings
from django.core.mail import EmailMessage
# Create your tests here.
def send_mailer(useremail):

    msg = EmailMessage('This is subject ', 'message', 'You got a email of contact form' + '<' + settings.EMAIL_HOST_USER + '>', ['gauravmandhotra5@gmail.com',useremail])
    msg.content_subtype = "html"
    return msg.send()