# Email Sender
Send email with python script.
Can include attachment file and/or image file in the body content.

## Usage example
```
# Recipients - List with comma delimited addresses
recipients = ['recipient1@gmail.com', 'recipient2@gmail.com']

# Email Sender
email_from = 'Python email sender'

# Email subject
email_subject = 'Test from python email sender'

# Email header
header = 'Test report'

# Provide content - Can be a string or database result
content = 'Contrary to popular belief, Lorem Ipsum is not'

# Image in the content
content_image = 'some_image.jpg'

# Attache file to email
attachment_file = 'some_image.extension'

# SMTP Login
smtp_login = 'some_login'

# SMTP Password
smtp_password = 'some_passowrd'

send_email(recipients, email_from, email_subject, header, content, content_image, attachment_file, smtp_login, smtp_password)
```

## Meta

Evgeni Altshul - jenyaalt@gmail.com

https://github.com/Jenyaalt/python
