
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


def send_feedback_mail(receivers, context, temlate_name):
    sender = 'contact@redmaxllc.com'
    subject = 'REDMAX LLC'



    #------------------------- admin send (with page_url)

    html_message = render_to_string(temlate_name, context)
    plain_message = strip_tags(html_message)

    emails = []
    for mail_receiver in receivers:
        emails.append(mail_receiver.email)


    send_mail(subject=subject,
              message=plain_message,
              html_message=html_message,
              from_email=sender,
              recipient_list=emails,
              fail_silently=False)
