from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.venue.forms import AddForm,DelForm, UpdateForm, QueryForm
from myproject.models import Venue

venue_blueprint = Blueprint('venue',
                              __name__,
                              template_folder='templates/venue')


@venue_blueprint.route('/query', methods=['GET', 'POST'])
def query():
    form = QueryForm()
    if form.validate_on_submit():
        id = form.id.data 
        name = form.name.data
        type = form.type.data 
        location = form.location.data 
        price = form.price.data 
        contact = form.contact.data 

        results = Venue.query.filter()
        if id != '':
            results = results.filter(Venue.id == id)
        if name != '':
            results = results.filter(Venue.name == name)
        if type != '':
            results = results.filter(Venue.type == type)
        if location != '':
            results = results.filter(Venue.location == location)
        if price != '':
            results = results.filter(Venue.price == price)
        if contact != '':
            results = results.filter(Venue.contact == contact)

        return render_template('queryresult_venue.html',venues = results)
    return render_template('query_venue.html',form=form)


@venue_blueprint.route('/update', methods=['GET', 'POST'])
def update():

    
    form = UpdateForm()

    if form.validate_on_submit():
        id = form.id.data 
        name = form.name.data
        type = form.type.data 
        location = form.location.data 
        price = form.price.data 
        contact = form.contact.data 
        

        # Add new Puppy to database
        venue = Venue.query.get(id)
        venue.name = name 
        venue.type = type 
        venue.location = location 
        venue.price = price 
        venue.contact = contact
        
        db.session.add(venue)
        db.session.commit()

        return redirect(url_for('venue.list'))

    return render_template('update_venue.html',form=form)

@venue_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        type = form.type.data 
        location = form.location.data 
        price = form.price.data 
        contact = form.contact.data 
        

        # Add new Puppy to database
        new_venue = Venue(name, type, location, price, contact)
        db.session.add(new_venue)
        db.session.commit()

        return redirect(url_for('venue.list'))

    return render_template('add_venue.html',form=form)

@venue_blueprint.route('/list')
def list():
    # Grab a list of puppies from database.
    venues = Venue.query.all()
    
    return render_template('list_venue.html', venues = venues)


@venue_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        venue = Venue.query.get(id)
        db.session.delete(venue)
        db.session.commit()

        return redirect(url_for('venue.list'))
    return render_template('delete_venue.html',form=form)
