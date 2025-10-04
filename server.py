from flask import Flask, render_template, request
import qrcode
import io
import base64
from qrcode.constants import ERROR_CORRECT_L
import re

app = Flask(__name__)
app.secret_key = "supersecret"

def create_vcard(name, phone, email="", org="", title="", other={}):
    parts = name.split(" ")
    if len(parts) >= 2:
        lastname, firstname = parts[-1], " ".join(parts[:-1])
    else:
        firstname, lastname = name, ""
    vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{lastname};{firstname};;;
FN:{name}"""
    if org:
        vcard += f"\nORG:{org}"
    if title:
        vcard += f"\nTITLE:{title}"
    vcard += f"\nTEL;TYPE=WORK,VOICE:{phone}"
    if email:
        vcard += f"\nEMAIL;TYPE=PREF,INTERNET:{email}"
    if "birthday" in other and other["birthday"]:
        vcard += f"\nBDAY:{other['birthday']}"
    if "address" in other and other["address"]:
        vcard += f"\nADR:{other['address']}"
    if "note" in other and other["note"]:
        vcard += f"\nNOTE:{other['note']}"
    vcard += "\nEND:VCARD"
    return vcard

@app.route("/", methods=["GET", "POST"])
def index():
    qr_img = None
    values = {}
    error_message = None

    if request.method == "POST":
        # Get form values
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").replace(" ", "")
        email = request.form.get("email", "").strip()
        org = request.form.get("org", "").strip()
        title = request.form.get("title", "").strip()
        birthday = request.form.get("birthday", "").strip()
        address = request.form.get("address", "").strip()
        note = request.form.get("note", "").strip()

        values = {"name": name, "phone": phone, "email": email,
                  "org": org, "title": title, "birthday": birthday,
                  "address": address, "note": note}

        # Validation
        if not name:
            error_message = "Name is required."
        elif not re.fullmatch(r'^[6-9]\d{9}$', phone):
            error_message = "Invalid phone number. Enter a valid 10-digit Indian number starting with 6-9."
        else:
            other_info = {"birthday": birthday, "address": address, "note": note}
            vcard_data = create_vcard(name, phone, email, org, title, other_info)

            qr = qrcode.QRCode(
                version=None,
                error_correction=ERROR_CORRECT_L,
                box_size=8,
                border=4
            )
            qr.add_data(vcard_data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            qr_img = base64.b64encode(buffered.getvalue()).decode()

    return render_template("index.html", qr_img=qr_img, values=values, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
