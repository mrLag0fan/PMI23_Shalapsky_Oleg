from functools import wraps
import shlex

import jwt

from main import *
from VaccinationRequestShema import VaccinationRequestShema
from Vaccination_RequstModel import VaccinationRequestModel
from  Vaccination_Request import VaccinationRequest
from UserModel import UserModel, UserShema

vr_schema = VaccinationRequestShema()
vrs_schema = VaccinationRequestShema(many=True)
user_schema = UserShema()
users_schema = UserShema(many=True)

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if 'TOKEN' in request.headers:
            token = request.headers['TOKEN']

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = UserModel.query.filter_by(email=data['email']).first()
        except:
            return jsonify({"massage": "Token is invalid"}), 401

        return f(current_user, *args, **kwargs)
    return decorator


@app.route('/vr', methods=["POST"])
@token_required
def post_vaccination_requst(current_user):

    if not current_user.admin:
        return jsonify({"message": "You don't have enough rights"})

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
@token_required
def get_vaccination_requst(current_user, id_):
    results = vr_schema.dump(VaccinationRequestModel.query.get(id_))
    if len(results) == 0:
        return jsonify({'status': 404, 'message': "Vaccination_Requst is not found"}), 404
    return jsonify({'status': 200, 'data': results}), 200


@app.route('/vr', methods=["GET"])
@token_required
def get_vaccination_requsts(current_user):
    all_products = VaccinationRequestModel.query.all()
    limit, offset = request.args.get('limit', type=int), request.args.get('offset', default=0, type=int)
    count = len(all_products)
    if limit:
        all_products = all_products[offset*limit:(offset+1)*limit]
    result = vrs_schema.dump(all_products)
    return jsonify({'status': 200, "data": result, "count": count})


@app.route('/vr/<int:id_>', methods=['DELETE'])
@token_required
def delete_vaccination_requst(current_user, id_):
    if not current_user.admin:
        return jsonify({"message": "You don't have enough rights"})
    try:
        vr = VaccinationRequestModel.query.get_or_404(id_)
        db.session.delete(vr)
        db.session.commit()
        return jsonify({'status': 200, 'message': "Vaccination_Requst has been successfully deleted."}), 200
    except Exception as e:
        return jsonify({'status': 404, 'message': str(e)}), 404


@app.route('/vr/<int:id_>', methods=['PUT'])
@token_required
def update_vaccination_requst(current_user, id_):
    if not current_user.admin:
        return jsonify({"message": "You don't have enough rights"})
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


@app.route("/user", methods=["GET"])
@token_required
def get_users(current_user):
    users = UserModel.query.all()
    result = users_schema.dump(users)
    return jsonify({"status": 200, "data": result})


@app.route("/user/<int:id>", methods=["GET"])
@token_required
def get_user(current_user, id):
    results = user_schema.dump(UserModel.query.get(id))
    if len(results) == 0:
        return jsonify({'status': 404, 'message': "User is not found"}), 404
    return jsonify({'status': 200, 'data': results}), 200


@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    hash_pasword = generate_password_hash(data['password'], method='sha256')

    new_User = UserModel(email=data['email'], hash=hash_pasword, name=data['name'], surname=data['surname'], admin=data['admin'])

    db.session.add(new_User)
    db.session.commit()

    return jsonify({"status": 200, "message": "User created"})

@app.route("/user/<int:id>", methods=["DELETE"])
@token_required
def delete_user(current_user, id):
    if not current_user.admin:
        return jsonify({"message": "You don't have enough rights"})
    try:
        user = UserModel.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'status': 200, 'message': "User has been successfully deleted."}), 200
    except Exception as e:
        return jsonify({'status': 404, 'message': str(e)}), 404

@app.route("/login")
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm ="Login required"'})

    user = UserModel.query.filter_by(email=auth.username).first()
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm ="Login required"'})

    if check_password_hash(user.hash, auth.password):
        token = jwt.encode({"email": user.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config["SECRET_KEY"])
        return jsonify({'token': token.decode('UTF-8')})
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm ="Login required"'})

if __name__ == "__main__":
    db.create_all()
    db.session.commit()
    app.run(debug=True)