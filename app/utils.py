import uuid
from flask import jsonify
from .models import URL, db

def url_shortener(data):
    longURL = data.get("url")
    if not longURL:
        return jsonify({"error": "LongURL is required"}), 400

    existing = URL.query.filter_by(longURL=longURL).first()
    if existing:
        return jsonify({
            "url": {
                "shortURL": existing.shortURL,
                "longURL": existing.longURL
            }
        }), 200

    for i in range(5):
        shortURL = "short-"+str(uuid.uuid4())[:8]
        if URL.query.filter_by(shortURL=shortURL).first():
            if i == 4:
                return jsonify({"error": "Could not generate unique short URL"}), 400
            continue
        else:
            new_url = URL(shortURL=shortURL, longURL=longURL)
            db.session.add(new_url)
            db.session.commit()
            return jsonify({
                "url": {
                    "shortURL": new_url.shortURL,
                    "longURL": new_url.longURL
                }
            }), 200
