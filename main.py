from flask import Flask, request, jsonify, abort

app = Flask(__name__)

APP_HOST = '127.0.0.1'
APP_PORT = 5000


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route('/test', methods=["POST"])
def get_third_element():
    """Get the input string from the user.
        Return every third letter from the original string"""

    try:
        input_json = request.get_json(force=True)
        string_to_cut = input_json['string_to_cut']
        ans = {'return_string': ""}

        if len(input_json.keys()) != 1:
            abort(404,
                  description="Only 1 Key 'string_to_cut' should be present.")
        elif len(string_to_cut) < 3:
            abort(404, description='The value has Insufficient Length')

        for index in range(2, len(string_to_cut), 3):
            ans['return_string'] += string_to_cut[index]

        return jsonify(ans)
    except Exception as e:
        abort(404,
              description=f"{e}: Make sure the key is 'string_to_cut'")


if __name__ == '__main__':
    app.run(host=APP_HOST, debug=True, port=APP_PORT)
