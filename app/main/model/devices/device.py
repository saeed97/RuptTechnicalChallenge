
from ... import db

from sqlalchemy import ForeignKey


class Devices(db.Model):
    """Devices of user that has been used """
    __tablename__ = "devices"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    device_id = db.Column(db.String(255))
    client_id = db.Column(db.Integer, ForeignKey(
        "client.client_id"), name="fk_devices_client_id")
    user_id = db.Column(db.Integer, ForeignKey(
        "user.user_id"), name="fk_devices_user_id")
    device_type = db.Column(db.String(255), nullable=False)
    access_count = db.Column(db.Integer, default=0, index=True)
    created_at = db.Column(db.DateTime, nullable=False)
