# 🚀 AWS S3 Static Website Automation

## 📌 Overview

This project demonstrates how to automate the deployment of a static website on AWS S3 using Python and boto3 (AWS SDK).

Instead of manually creating buckets and uploading files, the entire process is automated using a Python script.

---

## 🎯 Features

* Automated S3 bucket creation
* Static website hosting enabled
* File upload using Python script
* Public access configuration
* MIME type handling for files

---

## 🧰 Tech Stack

* AWS S3
* Python
* boto3

---

## ⚙️ How It Works

1. Creates an S3 bucket programmatically
2. Enables static website hosting
3. Uploads website files automatically
4. Applies public access policy
5. Generates website URL

---

## ▶️ How to Run

```bash
pip install boto3
aws configure
python deploy.py
```

---

## 🌐 Live Website

http://nitisha-static-site-12345.s3-website.ap-south-1.amazonaws.com/

---

## 📸 Screenshots

### 🌐 Website UI

![Website](screenshot1.png)

### 🪣 S3 Bucket

![S3 Bucket](screenshot2.png)

### ⚙️ Static Website Hosting Enabled

![Hosting](screenshot3.png)

---

## 📂 Project Structure

```
aws-s3-static-website-automation/
│── deploy.py
│── website/
│   ├── index.html
│   ├── style.css
│   └── error.html
│── screenshot1.png
│── screenshot2.png
│── screenshot3.png
│── README.md
```

---

## 🧠 Learning Outcomes

* Hands-on experience with AWS S3
* Understanding IAM permissions
* Automating cloud tasks using SDK
* Debugging real-world deployment issues

---

## 🚀 Future Improvements

* Add CloudFront CDN (for HTTPS & caching)
* Add custom domain
* Implement CI/CD using GitHub Actions

---

## 👩‍💻 Author

Nitisha

---
