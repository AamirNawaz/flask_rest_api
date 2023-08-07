from flask import Flask, request, jsonify

app = Flask(__name__)


list_of_dec = [
    {"id": 1, "name": "Aamir", "country": "Pakistan",
     "status": "active", "country_code": +92},
    {"id": 2, "name": "Tahir", "country": "Bossnia",
        "status": "block", "country_code": +550}
]


@app.route('/')
def index():
    # calling the list function
    return get_data()


@app.route('/api/record/list', methods=["GET"])
def get_data():
    return jsonify(list_of_dec)


@app.route('/api/record/<int:id>', methods=['GET'])
def get_single_record(id):

    # First Method
    # item = next((item for item in list_of_dec if item['id'] == id), None)
    # if (item):
    #     return jsonify(item)
    # else:
    #     return "item not found", 404

    # Second Method
    for singleDec in list_of_dec:
        if singleDec['id'] == id:
            return jsonify(singleDec)
        else:
            return "item not found", 404


@app.route('/api/record/update/<int:id>', methods=["PUT"])
def update_record(id):
    updated_item = request.get_json()

    for singleDec in list_of_dec:
        if (singleDec['id'] == id):
            singleDec.update(updated_item)
            return jsonify(singleDec)
        else:
            return "item faild to update", 404
    return "No record found", 404


@app.route('/api/record/delete/<int:id>', methods=['delete'])
def delete_record(id):
    for record in list_of_dec:
        if (record['id'] == id):
            list_of_dec.remove(record)
            return jsonify({"data": record, "message": "Record deleted successfully!", "status": 200})
        else:
            return "item not found", 404
    return "No record found", 404
