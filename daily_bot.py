import os
import requests
import datetime

# 1. Fetch a live joke/quote from the internet
try:
    response = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=5)
    if response.status_code == 200:
        data = response.json()
        joke = f"{data['setup']} — <strong>{data['punchline']}</strong>"
    else:
        joke = "Why do programmers prefer dark mode? Because light attracts bugs!"
except Exception:
    joke = "Why do programmers prefer dark mode? Because light attracts bugs!"

# 2. Get current time in UTC
now = datetime.datetime.now().strftime("%B %d, %Y - %H:%M:%S UTC")

# 3. Read our Secret Key
secret_key = os.environ.get("MY_SECRET_KEY", "No Secret Found")
secret_status = "ACTIVE & PROTECTED 🛡️" if secret_key != "No Secret Found" else "NOT SET"

# 4. Generate a fresh HTML page
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Live Auto-Updating Bot Webpage</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      background-color: #0d1117;
      color: #c9d1d9;
      text-align: center;
      padding: 40px;
    }}
    h1 {{ color: #58a6ff; }}
    .card {{
      background: #161b22;
      border: 2px solid #30363d;
      border-radius: 12px;
      padding: 25px;
      max-width: 500px;
      margin: 20px auto;
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }}
    .joke-box {{
      background: #21262d;
      border-left: 4px solid #238636;
      padding: 15px;
      margin: 15px 0;
      border-radius: 4px;
      font-size: 16px;
    }}
    .badge {{
      background: #238636;
      color: white;
      padding: 4px 10px;
      border-radius: 12px;
      font-size: 12px;
    }}
  </style>
</head>
<body>
  <h1>🤖 GitHub Actions Live Auto-Updater</h1>
  <div class="card">
    <span class="badge">Robot Active</span>
    <p><strong>Last Auto-Update:</strong> {now}</p>
    <div class="joke-box">
      <p>💡 <em>{joke}</em></p>
    </div>
    <p>🔑 <strong>Secret Security Status:</strong> {secret_status}</p>
  </div>
</body>
</html>
"""

# Write the updated page directly to index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ index.html successfully updated with live internet data!")
