from django.forms import CharField, EmailField, Form, Textarea


class ContactForm(Form):
    name = CharField(label="Your name", max_length=200, required=True)
    email = EmailField(label="Email", required=True)
    message = CharField(label="Message", widget=Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self:
            field.field.widget.attrs["class"] = "input"


class IssueForm(Form):
    name = CharField(label="Your Name", max_length=200, required=True)
    email = EmailField(label="Email", required=True)
    subject = CharField(label="Subject", max_length=200, required=True)
    report = CharField(label="Issue Report", widget=Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "input"
