from ... import db
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    client_id = db.Column(db.Integer, ForeignKey(
        'client.client_id'), name='fk_users_client_id')
    username = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    __table_args__ = (UniqueConstraint(
        "fk_users_client_id", "user_id", name="unique_client_user"),)

    def __repr__(self):
        return f"<User '{self.username}'>"
