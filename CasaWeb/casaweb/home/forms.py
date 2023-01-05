from django.forms import CharField, EmailField, Form, Textarea


class ContactForm(Form):
    name = CharField(label="Your name", max_length=200, required=True)
    email = EmailField(label="Email", required=True)
    message = CharField(label="Message", widget=Textarea, required=True)


class IssueForm(Form):
    name = CharField(label="Your Name", max_length=200, required=True)
    email = EmailField(label="Email", required=True)
    subject = CharField(label="Subject", max_length=200, required=True)
    report = CharField(label="Issue Report", widget=Textarea, required=True)
    # TODO: add file upload for screenshots etc.
