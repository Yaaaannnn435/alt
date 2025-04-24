import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import json
import os

# 🔧 Paramètres
KEYWORDS = [
    "alternance BTS CIEL",
    "alternance technicien réseaux",
    "alternance technicien support",
    "alternance cybersécurité"
]
SEARCH_URL = "https://www.hellowork.com/fr-fr/emploi/recherche.html?k=alternance&l=&mode=offres"
SENT_OFFERS_FILE = "sent_offers.json"

# 📬 Configuration e-mail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_FROM = "tonmail@gmail.com"
EMAIL_TO = "tonmail@gmail.com"
EMAIL_PASSWORD = "motdepasse-application"  # Utilise un mot de passe d'application si Gmail

def load_sent_offers():
