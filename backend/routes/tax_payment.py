from flask import Blueprint, request, jsonify
import starkbank

tax_payment_bp = Blueprint('tax_payment_bp', __name__)

@tax_payment_bp.route('/', methods=['POST'])
def create_tax_payment():
    """
    Cria um novo pagamento de imposto.
    ---
    tags:
      - TaxPayment
    parameters:
      - in: body
        name: body
        description: Dados do pagamento de imposto
        schema:
          type: object
          required:
            - bar_code
          properties:
            bar_code:
              type: string
              example: "83660000001084301380074119002551100010601813"
            scheduled:
              type: string
              format: date
              example: "2023-08-02"
            description:
              type: string
              example: "fix the road"
            tags:
              type: array
              items:
                type: string
              example: ["take", "my", "money"]
    responses:
      200:
        description: Pagamento de imposto criado com sucesso
        schema:
          type: object
          properties:
            id:
              type: string
              example: "1234567890"
            status:
              type: string
              example: "success"
    """
    data = request.json

    bar_code = data.get('bar_code')
    scheduled = data.get('scheduled')
    description = data.get('description')
    tags = data.get('tags')

    payments = starkbank.taxpayment.create([
        starkbank.TaxPayment(
            bar_code=bar_code,
            scheduled=scheduled,
            description=description,
            tags=tags,
        )
    ])

    payment_dict = [payment.__dict__ for payment in payments]

    return jsonify(payment_dict), 200
