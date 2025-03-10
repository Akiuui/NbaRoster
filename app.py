from flask import Flask, jsonify
from nba_api.stats.endpoints import CommonTeamRoster
import os
import logging
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


@app.route('/')
def home():
    roster = CommonTeamRoster(1).get_dict()

    # roster_data =  roster.to_disc(orient="records")

    return jsonify({"roster":roster})
    # return roster


if __name__ == '__main__':
    from waitress import serve
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 8008))
    serve(app, host="0.0.0.0", port=port)