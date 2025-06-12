from flask import Flask, render_template, request, jsonify

# Inicializamos la aplicación Flask
app = Flask(__name__)


@app.route('/')
def login_page():
    """
    Muestra la página de login.
    """
    return render_template('login.html')


@app.route('/auth', methods=['POST'])
def authenticate():
    """
    Procesa los datos del formulario de login.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    # Lógica de validación MUY simple (en un proyecto real, esto sería complejo y seguro)
    if email and password:
        # Aquí iría la validación contra una base de datos, comprobando que la clave es correcta.
        # Por ejemplo, si el email contiene '@' y la clave tiene más de 8 caracteres.
        if "@" in email and len(password) > 8:
            return jsonify({
                "status": "success",
                "message": f"Bienvenido, {email}!"
            }), 200
        else:
            return jsonify({
                "status": "error",
                "message": "Credenciales con formato inválido."
            }), 400

    return jsonify({
        "status": "error",
        "message": "Faltan correo o contraseña."
    }), 400


# Permite ejecutar la app directamente con 'python app.py'
if __name__ == '__main__':
    app.run(debug=True, port=5001)
