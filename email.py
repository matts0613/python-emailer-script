import webbrowser

fromEmail = "example@example.com"
passwrd = "password"
subject = "email subject"
emailBody = "email body"

webbrowser.open('mailto:?to=' + fromEmail + '&subject=' + subject + '&body=' + emailBody, new=1)