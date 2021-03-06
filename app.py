import pickle as p
import os

from flask import Flask, request, jsonify

app = Flask(__name__)

model = p.load(open('knnpickle_file4', 'rb'))

@app.route('/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = model.predict(data)
    sort = ['тюльпан', 'роза', 'ромашка', 'орхидея']
    prediction = sort[int(prediction)]
    return jsonify(prediction)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    # port = int(os.environ.get("PORT", 5000))
    # app.run(debug=True, host='0.0.0.0')

# import os
#
# from flask import Flask, request, jsonify
# import pickle as p
#
# app = Flask(__name__)
#
# model = p.load(open('knnpickle_file', 'rb'))
#
#
# @app.route('/', methods=['POST'])
# def makecalc() :
#     data = request.get_json()
#     prediction = model.predict(data)
#     flower = ['Setosa', 'Versicolor', 'Virginica']
#     prediction = flower[int(prediction)]
#     return jsonify(prediction)
#
#
# if __name__ == '__main__' :
#     app.run(port=8080, host='127.0.0.1')
    # port = int(os.environ.get("PORT", 5000))
    # app.run(debug=True, host='0.0.0.0')
