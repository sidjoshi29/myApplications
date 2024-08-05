from app import app, db
from flask import request, jsonify
from models import Application

# Get all applications
@app.route("/api/applications", methods=["GET"])
def get_applications():
    applications = Application.query.all()
    result = [application.to_json() for application in applications]
    return jsonify(result)

# Create an application
@app.route("/api/applications", methods=["POST"])
def create_application():
    try:
        data = request.json
        required_fields = ["status", "company", "role"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        application = Application(
            status=data.get("status"),
            role=data.get("role"),
            company=data.get("company"),
            notes=data.get("notes", ""),
            timeline=data.get("timeline", "")
        )
        db.session.add(application) #like git add .
        db.session.commit() #like git commit
        return jsonify(application.to_json()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Delete an application
@app.route("/api/applications/<int:id>", methods=["DELETE"])
def delete_application(id):
    try:
        application = Application.query.get(id)
        if application is None:
            return jsonify({"error": "Application not found"}), 404

        db.session.delete(application)
        db.session.commit()
        return jsonify({"msg": "Application deleted"}), 200
    except Exception as e:
        db.session.rollback() #go back to previous state
        return jsonify({"error": str(e)}), 500

# Update an application
@app.route("/api/applications/<int:id>", methods=["PATCH"])
def update_application(id):
    try:
        application = Application.query.get(id)
        if application is None:
            return jsonify({"error": "Application not found"}), 404

        data = request.json
        application.status = data.get("status", application.status)
        application.company = data.get("company", application.company)
        application.notes = data.get("notes", application.notes)
        application.timeline = data.get("timeline", application.timeline)

        db.session.commit()
        return jsonify(application.to_json()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
