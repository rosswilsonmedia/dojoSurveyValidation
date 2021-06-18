from ..config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.location=data['location']
        self.language=data['language']
        self.comment=data['comment']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def save(self, data):
        query="INSERT INTO dojos (name, location, language, comment, created_at, updated_at)"\
            "VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"

        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @staticmethod
    def validate_form(data):
        is_valid=True

        if 'name' not in data or len(data['name'])<2:
            flash("Name must be at least two characters.")
            is_valid=False
        if 'location' not in data or data['location']==None or len(data['location'])<2:
            flash("Location not valid for this form.")
            is_valid=False
        if 'language' not in data or data['language']==None or len(data['language'])<2:
            flash("Language not valid for this form.")
            is_valid=False

        return is_valid