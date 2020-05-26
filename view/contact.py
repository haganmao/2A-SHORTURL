
import smtplib
from email.mime.text import MIMEText

from view.core import coreHandler
from werkzeug.datastructures import MultiDict


class contactHandler(coreHandler):
    def get(self):
        data = dict(
            cardTitle='Contact Us'
        )
        self.render('contact.html', data=data)

    def post(self):
        result = dict(statuscode=500)
        contact_form = MultiDict(self.getFormData)
        # print("#######################")
        # print(contact_form)
        # print(contact_form['fullname'])
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = '2aurlshortner@gmail.com'
        EMAIL_HOST_PASSWORD = '123456mmc..'
        EMAIL_PORT = 465

        mail_sender = '2aurlshortner@gmail.com'
        mail_receiver = ['2aurlshortner@gmail.com']

        # print(m)
        if contact_form:
            m = 'message: ' + contact_form['message'] + '\n\n'  + 'email: ' + contact_form['email'] 
            message = MIMEText(
                m, 'plain', 'utf-8')

            message['From'] = mail_sender
            message['To'] = ','.join(mail_receiver)
            message['subject'] = contact_form['fullname'] + \
                ' contact form information received'
            print("#######################1")
            s = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
            print("#######################2")
            s.connect(EMAIL_HOST, EMAIL_PORT)
            s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

            print("#######################3")
            print(message)
            s.sendmail(
                mail_sender, mail_receiver, message.as_string()
            )
            s.quit()
            try:
                print('send success')
            except Exception as expection:
                print("#######################")
                return 'send error'
            result['statuscode'] = 200
        else:
            result['statuscode'] = 500          
        self.write(result)
