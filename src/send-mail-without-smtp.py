import smtplib
import dns.resolver

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


send_from = "E-mail example <email@example.com>"

def sendMail(to):
    msg = MIMEMultipart()
    msg["From"] = send_from
    msg["To"] = to
    msg["X-Priority"] = "1"
    msg["Date"] = formatdate(localtime=True)
    msg["Subject"] = "A test e-mail"

    text_html = """
    <html>
        <body>
            <h1>E-mail without SMTP.</h1>
        </body>
    </html>
    """

    msg.attach(MIMEText(text_html, "html"))

    domain = to.split('@')[1]
    mx = str(dns.resolver.query(domain, 'MX')[0].exchange)
    server = smtplib.SMTP(mx)
    # server.starttls()
    server.sendmail(send_from, to, msg.as_string())
    server.quit()

sendMail("example@mailinator.com")