from db import db


class BaseMixin:
    def json(self):
        raise NotImplementedError("Subclasses must implement this method")

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_to_db(self):
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def paginate(cls,start_index, per_page, error_out=True):
        return cls.query.paginate(start_index, per_page, error_out)
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
