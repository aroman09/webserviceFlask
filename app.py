from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {
        'cedula': 1982462,
        'nombre':'marco martinez',
        'edad': 25
    },
    {
        'cedula': 1029304,
        'nombre':'carlos',
        'apellido':'abad',
        'direccion':'Av. 12 de Abril y Av. Loja', 
    },
    {
        'cedula': 18964346,
        'nombre':'dario gonza',
        'sueldo': 600
    },

]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_task(user_id):
    user = [user for user in users if user['cedula'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

if __name__ == '__main__':
    app.run(debug=True)