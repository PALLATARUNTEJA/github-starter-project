import os
import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Read the secret key from the environment variables safely!
secret_key = os.environ.get("MY_SECRET_KEY", "No Secret Found (Local Mode)")

print("🤖 Hello from your GitHub Actions Robot!")
print(f"⏰ Execution Time: {current_time} UTC")
print(f"🔑 Secret Key Received from GitHub: {secret_key}")
