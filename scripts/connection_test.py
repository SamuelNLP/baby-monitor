import os

from dotenv import load_dotenv
from pytapo import Tapo


load_dotenv()

user = os.getenv("ACCOUNT")
password = os.getenv("PASSWORD")
cloud_password=os.getenv("CLOUD_PASSWORD")
host = "192.168.8.113"

tapo = Tapo(host, user, password)

print(tapo.getBasicInfo())