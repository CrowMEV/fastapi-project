import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import Environment, PackageLoader, select_autoescape

from app.core.settings import settings


def render_email_template(*args, **kwargs) -> str:
    env = Environment(
        loader=PackageLoader("app"), autoescape=select_autoescape()
    )
    template = env.get_template("email.html")
    return template.render(*args, **kwargs)


def send_email(to: str, *args, **kwargs) -> None:
    sender_email = settings.EMAIL_USERNAME

    msg = MIMEMultipart()
    msg["From"] = settings.EMAIL_FROM
    msg["To"] = to
    msg["Subject"] = settings.EMAIL_SUBJECT
    msg.attach(MIMEText(render_email_template(*args, **kwargs), "html"))

    with smtplib.SMTP_SSL(
        settings.EMAIL_HOST,
        settings.EMAIL_PORT,
        context=ssl.create_default_context(),
    ) as server:
        server.login(sender_email, settings.EMAIL_PASSWORD)
        server.sendmail(to, sender_email, msg.as_string())
