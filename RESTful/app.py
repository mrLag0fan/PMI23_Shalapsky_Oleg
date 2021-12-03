import shlex
from main import *
from VaccinationRequestShema import VaccinationRequestShema
from Vaccination_RequstModel import VaccinationRequestModel
from  Vaccination_Request import VaccinationRequest

vr_schema = VaccinationRequestShema()
vrs_schema = VaccinationRequestShema(many=True)

@app.route('/vr', methods=["POST"])
def post_vaccination_requst():
    try:
        dummy = VaccinationRequest.default()
        if len(request.json) != VaccinationRequest.count_of_feilds:
            raise ValueError
        a = [x.split("__")[-1] for x in vars(dummy).keys()]
        for attr in a:
            setattr(dummy, attr, request.json[attr])
        new_vr = VaccinationRequestModel(*vars(dummy).values())
        db.session.add(new_vr)
        db.session.commit()
        return jsonify({'status': 200, 'message': "Vaccination_Requst has been successfully created."}), 200
    except ValueError :
        return jsonify({'status': 400, 'message': "Invalid data"}), 400


@app.route('/vr/<int:id_>', methods=['GET'])
def get_vaccination_requst(id_):
    results = vr_schema.dump(VaccinationRequestModel.query.get(id_))
    if len(results) == 0:
        return jsonify({'status': 404, 'message': "Freelancer is not found"}), 404
    return jsonify({'status': 200, 'data': results}), 200


@app.route('/vr', methods=["GET"])
def get_vaccination_requsts():
    all_products = VaccinationRequestModel.query.all()
    result = vrs_schema.dump(all_products)
    return jsonify(result)


@app.route('/vr/<int:id_>', methods=['DELETE'])
def delete_vaccination_vequst(id_):
    try:
        vr = VaccinationRequestModel.query.get_or_404(id_)
        db.session.delete(vr)
        db.session.commit()
        return jsonify({'status': 200, 'message': "Vaccination_Requst has been successfully deleted."}), 200
    except Exception as e:
        return jsonify({'status': 404, 'message': str(e)}), 404


@app.route('/vr/<int:id_>', methods=['PUT'])
def update_Vaccination_Requst(id_):
    try:
        dummy = VaccinationRequest.default()
        for i, field in enumerate(request.json.keys()):
            setattr(dummy, field, request.json[field])
        vr = VaccinationRequestModel.query.filter_by(id=id_)
        if not vr.all():
            return jsonify({'status': 404, 'message': "Vaccination_Requst is not found"}), 404
        vr.update(request.json)
        db.session.commit()
        return jsonify({'status': 200, 'message': "Vaccination_Requst has been successfully updated."}), 200
    except ValueError:
        return jsonify({'status': 400, 'message': "Invalid data"}), 400

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


if __name__ == "__main__":
    db.create_all()
    db.session.commit()
    app.run(debug=True)