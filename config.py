import os

from dotenv import load_dotenv
from os import environ

load_dotenv(".env")
DATABASE = os.environ["DATABASE"]
print('asd')