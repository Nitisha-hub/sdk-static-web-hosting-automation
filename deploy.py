import boto3
import os
import json
import mimetypes

# Create S3 client
s3 = boto3.client('s3')

# Unique bucket name
bucket_name = "nitisha-static-site-12345"  # change if needed
region = "ap-south-1"

# 1️⃣ Create Bucket
try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    print("✅ Bucket created")
except Exception as e:
    print("⚠️ Bucket may already exist:", e)

# 2️⃣ Disable Block Public Access
s3.put_public_access_block(
    Bucket=bucket_name,
    PublicAccessBlockConfiguration={
        "BlockPublicAcls": False,
        "IgnorePublicAcls": False,
        "BlockPublicPolicy": False,
        "RestrictPublicBuckets": False
    }
)

print("✅ Public access settings updated")

# 3️⃣ Add Bucket Policy
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicRead",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": f"arn:aws:s3:::{bucket_name}/*"
        }
    ]
}

s3.put_bucket_policy(
    Bucket=bucket_name,
    Policy=json.dumps(bucket_policy)
)

print("✅ Bucket policy added")

# 4️⃣ Enable Static Website Hosting
s3.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration={
        'IndexDocument': {'Suffix': 'index.html'},
        'ErrorDocument': {'Key': 'error.html'}
    }
)

print("✅ Website hosting enabled")

# 5️⃣ Upload Files
folder_path = "website"

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        s3_path = os.path.relpath(file_path, folder_path)

        content_type, _ = mimetypes.guess_type(file_path)
        if content_type is None:
            content_type = 'binary/octet-stream'

        s3.upload_file(
            file_path,
            bucket_name,
            s3_path,
            ExtraArgs={'ContentType': content_type}
        )

        print(f"📤 Uploaded: {s3_path}")

# 6️⃣ Website URL
website_url = f"http://{bucket_name}.s3-website-{region}.amazonaws.com"

print("\n🎉 Deployment Complete!")
print("🌍 Website URL:", website_url)