# Modules
import argparse

from faker import Faker
from xata import XataClient

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--key")
args = parser.parse_args()

# Parameters
table = "Posts"

# Create faker object
fake = Faker()

# Creata Xata client xau_nc9NKeXvgvHuS1AoR5NOwIyWMuPc2XUc7
client = XataClient(
    api_key=args.key,
    db_url="https://sifon-lade-0z-s-workspace-h9pso8.eu-west-1.xata.sh/db/powerops-db",
    branch_name="main",
)

# Get data from db
data = client.query(table, page=dict(size=2))

# Insert data into db
