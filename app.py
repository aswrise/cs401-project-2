# !pip install mlxtend

import pickle
from flask import Flask, jsonify, request
app = Flask(__name__)


def load_model():
    while True:
        try:
            app.model = pickle.load(open("/data/rules", "rb"))
            print('model loaded')
            break
        except:
            print('model loading failed')

load_model()

@app.route('/api/recommend', methods=['POST'])
def json_example():
    request_data = request.get_json(force=True)

    songs = None
    # dataset=pd.read_csv("test.csv")
    recommend = []
    if request_data:
        if 'songs' in request_data:
            songs = request_data['songs']
            # songs is a list
    # with open('rules', 'rb') as f:
    #     recovered_data = pickle.load(f)

    rules = app.model[0]
    time = app.model[1]
    n =len(rules["antecedents"])
    for i in range(n):
        # print(type(rules["antecedents"][i]))
        rules["antecedents"][i]=list(rules ["antecedents"][i])
        rules["consequents"][i]=list(rules ["consequents"][i])
    for i in range(n):
        a = False
        for j in rules["antecedents"][i]:
            if j not in songs:
                a = True
                break
        if a == False:
            for j in rules["consequents"][i]:
                if j not in songs:
                    recommend.append(j)
    # tracklist = list(set(recommend))
    # version = "version: 0.0.1"
    # model_date = time
    return jsonify(
        tracklist=list(set(recommend)),
        version="0.0.1",
        model_date= time

        # version=g.user.email,
        # model_date=g.user.id,
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='30505', debug=True)