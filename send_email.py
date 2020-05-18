import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_email(recipients, sender, email_subject, content_header, content_body, content_image, attachment_file, login, password):
    """
    Send email with attachment and/or image in contect.

    Parameters:
        recipients: The recipient.
        sender: From who the email.
        email_subject: The subject of the email.
        content_header: The header of the content.
        content_body: The content of the email. usually text.                
        content_image: The image that appears in the email body.
        attachment_file: File attached to the email.
    """

    if login is None or password is None:
        print('login and password required and connot be empty or None')
        return

    if recipients is None:
        print('recipients required and connot be empty or None')
        return        

    message = MIMEMultipart("alternative")
    message['Subject'] = email_subject
    message['From'] = sender
    message['To'] = ", ".join(recipients)

    # write the HTML part
    html = """\
        <html>
            <body>
                <h1>{0}</h1>
                <h4>Content</h4>
                <p>{1}</p>                
                <img src="cid:Mailtrapimage">                
            </body>
        </html>
    """.format(content_header, content_body)

    part = MIMEText(html, "html")
    message.attach(part)

    if content_image is not None:
        fp = open(content_image, 'rb')
        image = MIMEImage(fp.read())
        fp.close()

        image.add_header('Content-ID', '<Mailtrapimage>')
        message.attach(image)

    if attachment_file is not None:
        filename = attachment_file
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {filename}",)
        message.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        print(f'Sending email to {recipients}...')
        try:
            smtp.login(login, password)
            smtp.sendmail(sender, recipients, message.as_string())
            print('Email sent Successfully')
        except Exception as error:
            print(error)
        finally:
            smtp.quit()
