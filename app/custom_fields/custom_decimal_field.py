from wtforms.fields import DecimalField
from wtforms.utils import unset_value

from config import Configuration

conf = Configuration()


class CustomDecimalField(DecimalField):
    """
    Custom decimal field class that allows to
    set a custom step for the number widget.
    """

    def __init__(self, label=None, validators=None, places=unset_value, rounding=None, step=0.1, **kwargs):
        self.widget.step = step
        super().__init__(label=label, validators=validators, places=places, rounding=rounding, **kwargs)

