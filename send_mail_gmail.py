import smtplib

def send_email(to, subject, body, gmail_user, gmail_password):
    '''
    This function sends an email using a gmail account.
    The password should be an app_password (16 characters, created in profile - security)
    :param to: array of strings
    :param subject: string
    :param body: string
    :param gmail_user: string
    :param gmail_password: string
    :return: prints if success or not
    '''

    sent_from = gmail_user
    email_text = """\
    From: %s
    To: %s
    Subject: %s
    
    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')