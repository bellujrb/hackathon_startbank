from flask import Flask, request, jsonify
import starkbank
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

with open('privateKey.pem', 'r') as file:
    private_key = file.read()

project = starkbank.Project(
    environment="sandbox",  
    id="4651416945688576",  
    private_key=private_key  
)

starkbank.user = project

@app.route('/v2/split-receiver', methods=['POST'])
def create_split_receiver():
        receiver = starkbank.splitreceiver.create([
            starkbank.SplitReceiver(
                name="Daenerys Targaryen Stormborn",
                tax_id="594.739.480-42",
                bank_code="341",
                branch_code="2201",
                account_number="76543-8",
                account_type="salary"
        )])

        receiver_dict = receiver[0].__dict__

        print("SplitReceiver criado:", receiver_dict)

        return jsonify(receiver_dict), 200

if __name__ == '__main__':
    app.run(port=8080)
