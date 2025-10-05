# 📇 Quick Contact — Instant Contact QR Generator

> _Generate and share your contact details instantly — scan, save, done._

**Quick Contact** is a simple **Flask web app** that instantly generates a **QR code containing your digital contact card (vCard)**.  
Anyone can scan your QR to **save your contact details directly** into their phone — no typing, no hassle.

🔗 **Live Demo:** https://contact-saver-6ipk.onrender.com

---

## 🚀 What It Does

- Turns your name, phone number, and other details into a **vCard QR code**
- When scanned, the QR code automatically saves your contact in the user’s phone
- Clean and modern UI with optional fields like:
  - Email  
  - Organization  
  - Job Title  
  - Birthday  
  - Address  
  - Notes

---

## 💡 Key Features

✅ No apps or accounts needed — just scan and save  
✅ Works seamlessly on both Android and iOS  
✅ Option to **download the QR code** as a PNG image  
✅ Automatically validates Indian phone numbers  
✅ Responsive and mobile-friendly design

---

## 🧠 Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Libraries:**
  - `qrcode` (for generating QR images)
  - `flatpickr` (for date input)
  - `base64`, `io`, `re`, `os` (for processing and encoding)

---

## 📷 How It Works

1. Open the web app.  
2. Enter your contact details (name, phone, etc.).  
3. Click **“Generate QR”**.  
4. Scan the generated QR code with any phone camera.  
5. The phone automatically detects your contact info — just tap **“Save Contact.”**

---
