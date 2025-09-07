from pyrogram import Client
import os

# Ask user for credentials
API_ID = int(input("Enter your API_ID from my.telegram.org: "))
API_HASH = input("Enter your API_HASH from my.telegram.org: ")
SESSION_NAME = input("Enter a short session name (e.g., anime_userbot): ")

# Create the client
app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

print("\n⚡ Starting login process...")
app.run()  # Interactive login: phone + code + 2FA if required

# Success message
print(f"\n✅ Session generated successfully: {SESSION_NAME}.session")

# Optional: show download path in Replit
print(f"Your session file is in the Replit project folder. Download it to use on Heroku.")
