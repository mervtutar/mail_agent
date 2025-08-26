from google_auth_oauthlib.flow import InstalledAppFlow
import os
from dotenv import load_dotenv; load_dotenv()

def bootstrap_oauth():
    SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
    client_id = os.environ["GOOGLE_CLIENT_ID"]
    client_secret = os.environ["GOOGLE_CLIENT_SECRET"]
    token_path = os.environ.get("GMAIL_TOKEN_PATH", "./token.json")

    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": client_id,
                "client_secret": client_secret,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": ["http://localhost"]
            }
        },
        SCOPES,
    )
    creds = flow.run_local_server(port=0)  # tarayıcı açılır
    with open(token_path, "w", encoding="utf-8") as f:
        f.write(creds.to_json())
    print(f"Token kaydedildi: {token_path}")

if __name__ == "__main__":
    bootstrap_oauth()
