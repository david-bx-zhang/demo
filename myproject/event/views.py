from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.event.forms import AddForm,DelForm,UpdateForm, QueryForm
from myproject.models import Event, Venue, Client, UsedSupply, Supply, Supplier

event_blueprint = Blueprint('event',
                              __name__,
                              template_folder='templates/event')

@event_blueprint.route('/query', methods=['GET', 'POST'])
def query():
    form = QueryForm()
    if form.validate_on_submit():
        id = form.id.data
        event = Event.query.get(id)
        venue_id = event.venue_id 
        client_id = event.client_id 
        venue = Venue.query.get(venue_id)
        client = Client.query.get(client_id)
        usedsupplies = UsedSupply.query.filter(UsedSupply.event_id == id).all()


        return render_template('queryresult_event.html', event = event, venue = venue, client = client, usedsupplies = usedsupplies,  )
    return render_template('query_event.html',form=form)


@event_blueprint.route('/update', methods=['GET', 'POST'])
def update():

    
    form = UpdateForm()

    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        client_id = form.client_id.data 
        type = form.type.data 
        date = form.date.data 
        num_of_invitees = form.num_of_invitees.data 
        budget =  form.budget.data 
        venue_id =  form.venue_id.data 
        

        # Add new Puppy to database
        event = Event.query.get(id)
        event.name = name 
        event.client_id = client_id 
        event.type = type 
        event.date = date  
        event.num_of_invitees = num_of_invitees  
        event.budget = budget 
        event.venue_id = venue_id  

        db.session.add(event)
        db.session.commit()

        return redirect(url_for('event.list'))

    return render_template('update_event.html',form=form)


@event_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        client_id = form.client_id.data 
        type = form.type.data 
        date = form.date.data 
        num_of_invitees = form.num_of_invitees.data 
        budget =  form.budget.data 
        venue_id =  form.venue_id.data 
        

        # Add new Puppy to database
        new_event = Event(name, client_id, type, date, num_of_invitees, budget, venue_id)
        db.session.add(new_event)
        db.session.commit()

        return redirect(url_for('event.list'))

    return render_template('add_event.html',form=form)

@event_blueprint.route('/list')
def list():
    # Grab a list of puppies from database.
    events = Event.query.all()
    
    return render_template('list_event.html', events =  events)


@event_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        event = Event.query.get(id)
        db.session.delete(event)
        db.session.commit()

        return redirect(url_for('event.list'))
    return render_template('delete_event.html',form=form)
