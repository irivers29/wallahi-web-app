from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/v1/api/tools', methods=['GET'])
def get_properties():
    response = {
        "itemsReceived": 9,
        "curPage": 1,
        "nextPage": 2,
        "prevPage": None,
        "offset": 0,
        "itemsTotal": 12,
        "pageTotal": 2,
        "items": [
            {
                "id": 25,
                "created_at": 1729684358920,
                "name": "Drill",
                "select_option": "rental",
                "price": 32,
                "type": "tool",
                "region": "Texas",
                "coordinates": {"lat": 31.9686,"lng": -99.9018},
                "image": "https://images.pexels.com/photos/1732414/pexels-photo-1732414.jpeg?auto=compress&cs=tinysrgb&w=600",
            },
            {
                "id": 26,
                "created_at": 1729684358921,
                "name": "Spikeball",
                "select_option": "rental",
                "price": 100,
                "type": "sport_equipment",
                "region": "Munich",
                "coordinates": {"lat": 48.1351,"lng": 11.5820},
                "image": "https://images.pexels.com/photos/209315/pexels-photo-209315.jpeg?auto=compress&cs=tinysrgb&w=600",
            }
        ]
    }
    return jsonify(response)


def run_app():
    # We bind to 0.0.0.0 so Docker containers can expose the port
    app.run(host='0.0.0.0', port=5009)


if __name__ == '__main__':
    run_app()
