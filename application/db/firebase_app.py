import pyrebase
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"), # API key for Firebase
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"), # Firebase authentication domain
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),  # URL of the Firebase Realtime Database
    "projectId": os.getenv("FIREBASE_PROJECT_ID"), # Firebase project ID
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"), # Firebase storage bucket
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"), # Messaging sender ID
    "appId": os.getenv("FIREBASE_APP_ID"), # Firebase app ID
}

# Initialize the Firebase app
firebase = pyrebase.initialize_app(config)
# Get the Firebase authentication instance
auth = firebase.auth()


def register(email, password):
    try:
        # Create a new user with the provided email and password
        auth.create_user_with_email_and_password(email, password)
        return "success"
    except Exception as e:
        print(f"Error: {e}")
        return "failure"

def login(email, password):
    try:
        # Sign in the user with the provided email and password
        auth.sign_in_with_email_and_password(email, password)
        return "success"
    except Exception as e:
        print(f"Error: {e}")
        return "failure"
