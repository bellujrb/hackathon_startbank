from flask import Blueprint, request, jsonify
import starkbank

split_bp = Blueprint('split_bp', __name__)

@split_bp.route('/receiver', methods=['POST'])
def create_split_receiver():
    """
    Cria um novo SplitReceiver.
    ---
    tags:
      - SplitReceiver
    parameters:
      - in: body
        name: body
        description: Dados do SplitReceiver
        schema:
          type: object
          required:
            - name
            - tax_id
          properties:
            name:
              type: string
              example: "Daenerys Targaryen Stormborn"
            tax_id:
              type: string
              example: "594.739.480-42"
            bank_code:
              type: string
              example: "341"
            branch_code:
              type: string
              example: "2201"
            account_number:
              type: string
              example: "76543-8"
            account_type:
              type: string
              example: "salary"
    responses:
      200:
        description: SplitReceiver criado com sucesso
        schema:
          type: object
          properties:
            id:
              type: string
              example: "1234567890"
            name:
              type: string
              example: "Daenerys Targaryen Stormborn"
    """
    receiver = starkbank.splitreceiver.create([
        starkbank.SplitReceiver(
            name="Daenerys Targaryen Stormborn",
            tax_id="594.739.480-42",
            bank_code="341",
            branch_code="2201",
            account_number="76543-8",
            account_type="salary"
        )
    ])

    receiver_dict = receiver[0].__dict__
    print("SplitReceiver criado:", receiver_dict)
    return jsonify(receiver_dict), 200
