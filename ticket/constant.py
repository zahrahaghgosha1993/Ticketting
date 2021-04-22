from django.utils.translation import ugettext_lazy as _


SENT = 'sent'
OPEN = 'open'
ANSWERED = 'answered'

STATUS_CHOOSE = (
    (SENT, _('sent')),
    (OPEN, _('open')),
    (ANSWERED, _('answered'))
)
