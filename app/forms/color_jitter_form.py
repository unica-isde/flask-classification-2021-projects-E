from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange, InputRequired

from app.utils.list_images import list_images
from app.custom_fields.custom_decimal_field import CustomDecimalField


class JitterImageForm(FlaskForm):
    """Form to select parameters and image for a Color Jitter transformation"""

    brightness = CustomDecimalField('brightness', validators=[NumberRange(min=0),
                                                              InputRequired('Set a value for brightness')], default=1)
    saturation = CustomDecimalField('saturation', validators=[NumberRange(min=0),
                                                              InputRequired('Set a value for saturation')], default=1)
    contrast = CustomDecimalField('contrast', validators=[NumberRange(min=0),
                                                          InputRequired('Set a value for contrast')], default=1)
    hue = CustomDecimalField('hue', validators=[NumberRange(min=0, max=0.5),
                                                InputRequired('Set a value for hue')], default=0.5)

    image = SelectField('image', choices=list_images(), validators=[DataRequired()])
    submit = SubmitField('Submit')
