from flask import Flask, render_template, redirect
from flask_migrate import Migrate

from .forms import ShippingForm
from .config import Configuration
from .models import db, Package

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    packages = Package.query.all()
    return render_template("package_status.html", packages=packages)


@app.route("/new_package", methods=["GET", "POST"])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():

        data = form.data
        package = Package(
            sender=data["sender_name"],
            recipient=data["recipient_name"],
            origin=data["origin"],
            destination=data["destination"],
            location=data["origin"],
        )

        # Add package to db
        db.session.add(package)
        db.session.commit()

        package.advance_all_locations()
        return redirect("/")

    return render_template("shipping_request.html", form=form)
