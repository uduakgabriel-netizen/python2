from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "dev-portfolio-secret"  # replace in production

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    errors = {}
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # Validate name
        if not name or len(name) < 3:
            errors["name"] = "Name must be at least 3 characters long."

        # Validate email (basic check)
        if not email or "@" not in email or "." not in email:
            errors["email"] = "Please enter a valid email address."

        # Validate message
        if not message:
            errors["message"] = "Message cannot be empty."

        if not errors:
            flash(f"Thank you {name}, I’ll get back to you at {email} soon!")
            return redirect(url_for("contact"))

    return render_template("contact.html", errors=errors)

if __name__ == "__main__":
    app.run()
 