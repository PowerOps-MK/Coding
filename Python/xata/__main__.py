from faker import Faker
from xata import XataClient

# Create faker object
fake = Faker()

# Creata Xata client
client = XataClient(
   api_key="xau_nc9NKeXvgvHuS1AoR5NOwIyWMuPc2XUc7", 
   db_url="https://sifon-lade-0z-s-workspace-h9pso8.eu-west-1.xata.sh/db/powerops-db", 
   branch_name="main"
)

resp = client.query("Posts", page=dict(size=2))
print(resp)
