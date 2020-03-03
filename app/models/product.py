from sqlalchemy import Column, Integer, String, Float, Boolean
from app.models.base import Base

def to_timestamp(time_stamp, digits = 13):
    if time_stamp is None:
        return None
    digits = 10 ** (digits -10)
    return int(round(time_stamp*digits))

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement= True)
    productId = Column(String(50), nullable=False)
    supplier = Column(String(20), nullable=True)
    category = Column(String(60), nullable=False)
    name = Column(String(500), nullable=True)
    img = Column(String(150), nullable=True)
    prefix = Column(String(50), nullable=True)
    price = Column(String(20))
    unit = Column(String(50), nullable=False)
    compare = Column(Float(20), default=1.00)
    latest = Column(Boolean, default=False)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'productId': self.productId,
            'create_time': to_timestamp(self.create_time),
            'supplier': self.supplier,
            'category': self.category,
            'name': self.name,
            'img': self.img,
            'prefix': self.prefix,
            'price': self.price,
            'unit': self.unit,
            'compare': self.compare,
            'latest': self.latest
        }

    @property
    def serialize_many2many(self):
        """
        Return object's relations in easily serializable format.
        NB! Calls many2many's serialize property.
        """
        return [item.serialize for item in self.many2many]