from flask import Flask, make_response


APP = Flask(__name__)


def sumar(n, m):
    return n + m


def restar(n, m):
    return n - m


def multiplicar(n, m):
    return n * m


def dividir(n, m):
    return n / m


@APP.route('/', methods=['GET'])
@APP.route('/<operador>/<op1>/<op2>', methods=['GET', 'POST'])
def matematicas(**datos):
    """ Esto es un endpoint de prueba para pytest """
    data = {}
    headers = {}

    try:
        if not datos:
            data = {'operador': 'ninguno, no hay operacion que realizar'}

        else:
            if datos['operador'] == 'sumar':
                res = sumar(int(datos['op1']), int(datos['op2']))
                data = {'operador': 'sumar', 'resultado': res}

            elif datos['operador'] == 'restar':
                res = restar(int(datos['op1']), int(datos['op2']))
                data = {'operador': 'restar', 'resultado': res}

            elif datos['operador'] == 'multiplicar':
                res = multiplicar(int(datos['op1']), int(datos['op2']))
                data = {'operador': 'multiplicar', 'resultado': res}

            elif datos['operador'] == 'dividir':
                res = dividir(int(datos['op1']), int(datos['op2']))
                data = {'operador': 'dividir', 'resultado': res}

    except Exception as e:
        print(f'Excepcion: {e}')

    return make_response(data, 200, headers)


def main():
    """ Programa principal """
    APP.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
