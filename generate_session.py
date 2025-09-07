from pyrogram import Client

print("🔑 Pyrogram Session Generator\n")

API_ID = int(input("👉 Enter your API_ID (from https://my.telegram.org/apps): "))
API_HASH = input("👉 Enter your API_HASH: ")
SESSION_NAME = input("👉 Enter a short session name (e.g., anime_userbot): ")

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

print("\n⚡ Starting login process...")
app.run()  # Will ask phone, code, and 2FA if enabled

print(f"\n✅ Session generated successfully! File saved as {SESSION_NAME}.session")
print("➡️ Download this .session file and upload it to Heroku/GitHub with your bot.")
