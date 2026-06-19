from sys import exit
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/validar_cnpj/<string:cnpj>", methods=["GET"])
def validar_cnpj(cnpj: str):
    cnpj = ''.join(filter(str.isdigit, cnpj))

    if len(cnpj) != 14:
        return {
            "status": "fail",
            "motivo": "CNPJ deve possuir 14 dígitos"
        }, 400

    if cnpj == cnpj[0] * 14:
        return {
            "status": "fail",
            "motivo": "CNPJ inválido"
        }, 400

    # Primeiro Digito
    pesos_1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    soma = sum(int(n) * p for n, p in zip(cnpj[:12], pesos_1))
    resto = soma % 11
    digito_1 = 0 if resto < 2 else 11 - resto

    # Primeiro Digito
    pesos_2 = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    soma = sum(int(n) * p for n, p in zip(cnpj[:12] + str(digito_1), pesos_2))
    resto = soma % 11
    digito_2 = 0 if resto < 2 else 11 - resto

    valido = cnpj[-2:] == f"{digito_1}{digito_2}"

    if not valido:
        return {
            "status": "fail",
            "message": "Dígitos verificadores inválidos",
            # "digitos_calculados": f"{digito_1}{digito_2}",
            # "digitos_informados": cnpj[-2:]
        }, 400

    return {
        "status": "success",
        "cnpj": cnpj,
        # "digitos_calculados": f"{digito_1}{digito_2}",
        # "digitos_informados": cnpj[-2:]
    }, 200

    return cnpj[-2:] == f"{digito_1}{digito_2}"

# if __name__ == "__main__":
#     app.run("0.0.0.0", port = 8002, debug = True)

# cnpj = "60877480000103"

# print()

# if not validar_cnpj(cnpj):
#     exit()

# print(f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}")

# response = requests.get(
#     f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
# )

# if response.status_code == 200:
#     empresa = response.json()

#     print("Razão Social:", empresa["razao_social"])
#     print("Nome Fantasia:", empresa["nome_fantasia"])
#     print("Situação:", empresa["descricao_situacao_cadastral"])
# else:
#     print("CNPJ não encontrado")