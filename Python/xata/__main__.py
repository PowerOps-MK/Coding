# Modules
import argparse

from faker import Faker
from xata import XataClient

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--key")
args = parser.parse_args()

# Parameters
api_url = "https://sifon-lade-0z-s-workspace-h9pso8.eu-west-1.xata.sh/db/powerops-db"
branch = "main"
table = "Posts"
labels = ["Python"]
author = "arden"

# Create a faker object
fake = Faker()

# Creata Xata client xau_nc9NKeXvgvHuS1AoR5NOwIyWMuPc2XUc7
client = XataClient(
    api_key=args.key,
    db_url=api_url,
    branch_name=branch,
)

# Creata a record in db
title = f"🙈 {fake.text(max_nb_chars=20)}"
client.create(
    table,
    record={
        "title": title,
        "labels": labels,
        "slug": fake.text(),
        "text": fake.text(),
        "author": author,
        "views": fake.random_int(),
    },
)

# Get one record from db
post = client.get_first(table, filter={"title": title})
print(post)
