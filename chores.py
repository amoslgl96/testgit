import random,smtplib


def emailChores(rchore, remail):
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.ehlo()
    smtpObj.login('myemail@address.com', 'mySecretPassword')
    body = 'Subject: Your Chore\n\nYour weekly assigned chore is: %s' % rchore
    print('Sending chore email to ' + remail + '...')
    smtpObj.sendmail('myemail@address.com', remail, body)
    smtpObj.quit()


chores = ['dishes', 'bathroom', 'vaccum', 'trash']
emails = ['someone@emailaddress.com', 'someone@emailaddress.com'\
          'someone@emailaddress.com', 'someone@emailaddress.com']

for i in range(0, len(emails)):
    randomChore = random.choice(chores)
    emailChores(randomChore, emails[i])
    chores.remove(randomChore)
