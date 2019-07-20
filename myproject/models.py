from myproject import db

class Client(db.Model):
    __tablename__ = "client"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    bill_info = db.Column(db.Text) 
    event = db.relationship('Event',backref='client',lazy='dynamic', cascade="all, delete-orphan")
    
    def __init__(self, name,  bill_info):
        self.name, self.bill_info = name, bill_info

    def __repr__(self):
        return f'id: {self.id} name: {self.name}, bill_info: {self.bill_info}'


class Venue(db.Model):
    __tablename__ = "venue"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    type = db.Column(db.Text)
    location = db.Column(db.Text)
    #TODO change to Int
    price = db.Column(db.Text)
    contact = db.Column(db.Text)
    event = db.relationship('Event',backref='venue',lazy='dynamic', cascade="all, delete-orphan")
    
    def __init__(self, name, type, location, price, contact):
        self.name = name 
        self.type = type 
        self.location = location 
        self.price = price 
        self.contact = contact

    def __repr__(self):
        return f'id: {self.id} name: {self.name}, type: {self.type} loc: {self.location} price: {self.price} contact: {self.contact}'


class Supply(db.Model):

    __tablename__ = "supply"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    type = db.Column(db.Text)
    # Supply should not have price  Supplier quote price instead 
    #unit_price = db.Column(db.Text) 
    supplier = db.relationship('Supplier',backref='supply',lazy='dynamic', cascade="all, delete-orphan")
    uesd_supply = db.relationship("UsedSupply", backref='supply',lazy='dynamic', cascade="all, delete-orphan" )
    
    def __init__(self, name, type):
        self.name, self.type = name, type

    def __repr__(self):
        return f'id: {self.id} name: {self.name}, type: {self.type} '


class Supplier(db.Model):
    __tablename__ = "supplier"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    type = db.Column(db.Text)
    unit_price = db.Column(db.Text) 
    contact = db.Column(db.Text) 
    supply_id = db.Column(db.Integer,db.ForeignKey('supply.id'))
    
    def __init__(self, name, type, unit_price, contact, supply_id):
        self.name, self.type, self.unit_price, self.contact, self.supply_id = name, type, unit_price, contact, supply_id

    def __repr__(self):
        return f'id: {self.id} name: {self.name}, type: {self.type} unit_price: {self.unit_price} contact: {self.contact} supply_id: {self.supply_id}'

class UsedSupply(db.Model):
    __tablename__ = "used_supply"
    id = db.Column(db.Integer,primary_key = True)
    supply_id = db.Column(db.Integer,db.ForeignKey('supply.id'))
    event_id = db.Column(db.Integer,db.ForeignKey('event.id'))
    quantity = db.Column(db.Text) 

    def __init__(self, supply_id, event_id, quantity):
        
        self.supply_id = supply_id
        self.event_id = event_id 
        self.quantity = quantity 
    def __repr__(self):
        return f'supply_id: {self.supply_id} event_id: {self.event_id} quantity: {self.quantity}'


class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer,primary_key = True)
    # client_id 
    name = db.Column(db.Text) 
    client_id = db.Column(db.Integer,db.ForeignKey('client.id'))
    type = db.Column(db.Text) 
    date = db.Column(db.Text) 
    num_of_invitees = db.Column(db.Text) 
    budget = db.Column(db.Text) 
    # venue_id 
    venue_id = db.Column(db.Integer,db.ForeignKey('venue.id'))
    uesd_supply = db.relationship("UsedSupply", backref='event',lazy='dynamic', cascade="all, delete-orphan" )
    
    def __init__(self, name, client_id, type, date, num_of_invitees, budget, venue_id):
        self.name = name
        self.client_id = client_id 
        self.type = type
        self.date = date  
        self.num_of_invitees = num_of_invitees 
        self.budget = budget  
        self.venue_id = venue_id 
    def __repr__(self):
        return f'id: {self.id} client_id: {self.client_id} type: {self.type} date: {self.date}  # of invitee: {self.num_of_invitees} budget: {self.budget} venue_id {self.venue_id}'


    


