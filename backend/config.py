import starkbank

with open('privateKey.pem', 'r') as file:
    private_key = file.read()

project = starkbank.Project(
    environment="sandbox",
    id="4651416945688576",
    private_key=private_key
)
