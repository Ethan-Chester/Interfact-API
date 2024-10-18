from flask import Blueprint, request, jsonify
from firebase_admin import firestore, initialize_app, credentials

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

@intersectionsAPI.route('/intersections/<id>', methods=['GET'])
def get_intersection(id):
    try:
        doc_ref = intersections_ref.document(id)
        doc = doc_ref.get()
        if doc.exists:
            return jsonify(doc.to_dict()), 200
        else:
            return jsonify({"error": "Document not found"}), 404
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500