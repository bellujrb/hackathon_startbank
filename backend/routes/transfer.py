from flask import Blueprint, request, jsonify
import starkbank

transfer_bp = Blueprint('transfer_bp', __name__)

@transfer_bp.route('/', methods=['POST'])
def create_transfer():
    """
    Cria uma nova transferência.
    ---
    tags:
      - Transfer
    parameters:
      - in: body
        name: body
        description: Dados da transferência
        schema:
          type: object
          required:
            - amount
            - tax_id
          properties:
            amount:
              type: integer
              example: 1000000
            tax_id:
              type: string
              example: "123.456.789-10"
            name:
              type: string
              example: "Daenerys Targaryen Stormborn"
            bank_code:
              type: string
              example: "20018183"
            branch_code:
              type: string
              example: "2201"
            account_number:
              type: string
              example: "76543-8"
            external_id:
              type: string
              example: "my-external-id"
            scheduled:
              type: string
              format: date
              example: "2020-08-14"
            tags:
              type: array
              items:
                type: string
              example: ["daenerys", "invoice/1234"]
            rules:
              type: array
              items:
                type: object
                properties:
                  key:
                    type: string
                    example: "resendingLimit"
                  value:
                    type: integer
                    example: 5
    responses:
      200:
        description: Transferência criada com sucesso
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                example: "1234567890"
              status:
                type: string
                example: "success"
    """
    transfers = starkbank.transfer.create([
        starkbank.Transfer(
            amount=1000000,
            tax_id="123.456.789-10",
            name="Daenerys Targaryen Stormborn",
            bank_code="20018183",
            branch_code="2201",
            account_number="76543-8",
            external_id="my-external-id",
            scheduled="2020-08-14",
            tags=["daenerys", "invoice/1234"],
            rules=[
                starkbank.transfer.Rule(
                    key="resendingLimit",
                    value=5
                )
            ]
        )
    ])

    transfer_dict = [transfer.__dict__ for transfer in transfers]
    return jsonify(transfer_dict), 200
