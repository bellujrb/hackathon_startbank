from flask import Blueprint, request, jsonify
import starkbank

brcode_payment_bp = Blueprint('brcode_payment_bp', __name__)

@brcode_payment_bp.route('/', methods=['POST'])
def create_brcode_payment():
    """
    Cria um novo pagamento BRCode.
    ---
    tags:
      - BRCodePayment
    parameters:
      - in: body
        name: body
        description: Dados do pagamento via BRCode
        schema:
          type: object
          required:
            - brcode
            - tax_id
          properties:
            brcode:
              type: string
              example: "00020101021226890014br.gov.bcb.pix2567brcode-h.sandbox.starkinfra.com/v2/ace289aac1ce453b9ca64fb12ec525855204000053039865802BR5925Stark Bank S.A. - Institu6009Sao Paulo62070503***63044DDF"
            tax_id:
              type: string
              example: "012.345.678-90"
            scheduled:
              type: string
              format: date
              example: "2021-01-13"
            description:
              type: string
              example: "this will be fast"
            tags:
              type: array
              items:
                type: string
              example: ["pix", "qrcode"]
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
        description: Pagamento BRCode criado com sucesso
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
    payments = starkbank.brcodepayment.create([
        starkbank.BrcodePayment(
            brcode="00020101021226890014br.gov.bcb.pix2567brcode-h.sandbox.starkinfra.com/v2/ace289aac1ce453b9ca64fb12ec525855204000053039865802BR5925Stark Bank S.A. - Institu6009Sao Paulo62070503***63044DDF",
            tax_id="012.345.678-90",
            scheduled="2021-01-13",
            description="this will be fast",
            tags=["pix", "qrcode"],
            rules=[
                starkbank.brcodepayment.Rule(key="resendingLimit", value=5)
            ]
        )
    ])

    payment_dict = [payment.__dict__ for payment in payments]
    return jsonify(payment_dict), 200
