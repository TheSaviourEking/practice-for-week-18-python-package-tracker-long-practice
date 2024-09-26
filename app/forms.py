from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from map.map import map as mymap


class ShippingForm(FlaskForm):
    locations = sorted(list(mymap.keys()))

    sender_name = StringField("Name", validators=[DataRequired()])
    recipient_name = StringField("Recipient's name", validators=[DataRequired()])
    origin = SelectField(
        "Origin",
        # choices=[(key, value) for key, value in mymap.items()]
        choices=locations,
        validators=[DataRequired()],
    )
    destination = SelectField(
        "Destination",
        choices=locations,  # choices requires a list
        validators=[DataRequired()],
    )
    express_shipping = BooleanField("Express Shipping ?")
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")
