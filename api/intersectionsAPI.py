from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
intersections_ref = db.collection('intersections')

intersectionsAPI = Blueprint('intersectionsAPI', __name__)



@intersectionsAPI.route('/intersections', methods=['GET'])
def get_all_intersections():
    try:
        all_docs = intersections_ref.stream()
        intersections = {}
        for doc in all_docs:
            intersections[doc.id] = doc.to_dict()
        return jsonify(intersections), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

@intersectionsAPI.route('/intersections/geo-json', methods=['GET'])
def get_intersection():
    try:
        all_docs = intersections_ref.stream()
        intersections = {
        }
        geoJson = {
                    "type":"FeatureCollection",
                    "features":[],
                    "image_url": []
                }

        for doc in all_docs:
            intersections[doc.id] = doc.to_dict()

        for key in intersections:
            new_feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        intersections[key]["longitude"], 
                        intersections[key]["latitude"]
                    ]
                },
                "properties": {
                    "id": intersections[key]["id"],
                    "name": intersections[key]["name"],
                    "status": intersections[key]["status"],
                    "timestamp": intersections[key]["timestamp"]
                }
            }
        geoJson["features"].append(new_feature)
        geoJson["image_url"].append(intersections[key]["imagepath"])
        return jsonify(geoJson), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500


@intersectionsAPI.route('/intersections/geo-json2', methods=['GET'])
def get_intersection():
    try:
        # all_docs = intersections_ref.stream()
        # intersections = {
        # }
        geoJson = {
                    "type":"Feature",
                    "geometry":{
                        "type": "Polygon",
                        "coordinates": [
                            [
                            [-100.0, 40.0],
                            [-100.0, 40.0],
                            [-100.0, 35.0],
                            [-100.0, 35.0],
                            [-100.0, 40.0]
                            ]
                        ],
                        "properties": {
                            "name": "ELL1"
                        }
                    },
                    "image_url": ["https://cdn.discordapp.com/attachments/1290699389160919185/1298408517501325322/isolated-white-chicken-shot-studio-316731815.png?ex=671974a9&is=67182329&hm=d6409fdf777dbabf6e23d58a7103f43eeacf41921eae2a565bb43cb1de417ec0&"]
                }

        # for doc in all_docs:
        #     intersections[doc.id] = doc.to_dict()

        # for key in intersections:
        #     new_feature = {
        #         "type": "Feature",
        #         "geometry": {
        #             "type": "Point",
        #             "coordinates": [
        #                 intersections[key]["longitude"], 
        #                 intersections[key]["latitude"]
        #             ]
        #         },
        #         "properties": {
        #             "id": intersections[key]["id"],
        #             "name": intersections[key]["name"],
        #             "status": intersections[key]["status"],
        #             "timestamp": intersections[key]["timestamp"]
        #         }
        #     }
        # geoJson["features"].append(new_feature)
        # geoJson["image_url"].append(intersections[key]["imagepath"])
        return jsonify(geoJson), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500
    