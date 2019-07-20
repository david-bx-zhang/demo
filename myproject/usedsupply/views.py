from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.usedsupply.forms import AddForm,DelForm,UpdateForm
from myproject.models import UsedSupply

usedsupply_blueprint = Blueprint('usedsupply',
                              __name__,
                              template_folder='templates/usedsupply')

@usedsupply_blueprint.route('/update', methods=['GET', 'POST'])
def update():

    form = UpdateForm()

    if form.validate_on_submit():
        id = form.id.data
        supply_id = form.supply_id.data
        event_id = form.event_id.data 
        quantity = form.quantity.data  
        

        # Add new Puppy to database
        used = UsedSupply.query.get(id)
        used.supply_id = supply_id
        used .event_id = event_id  
        used.quantity = quantity 
        db.session.add(used)
        db.session.commit()

        return redirect(url_for('usedsupply.list'))

    return render_template('update_usedsupply.html',form=form)


@usedsupply_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    
    form = AddForm()

    if form.validate_on_submit():
        supply_id = form.supply_id.data
        event_id = form.event_id.data
        quantity = form.quantity.data 

        

        # Add new Puppy to database
        new_used = UsedSupply(supply_id, event_id, quantity)
        db.session.add(new_used)
        db.session.commit()

        return redirect(url_for('usedsupply.list'))

    return render_template('add_usedsupply.html',form=form)

@usedsupply_blueprint.route('/list')
def list():
    # Grab a list of puppies from database.
    usedsupplies = UsedSupply.query.all()
    
    return render_template('list_usedsupply.html', usedsupplies = usedsupplies)


@usedsupply_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data 
        used = UsedSupply.query.get(id)
        db.session.delete(used)
        db.session.commit()

        return redirect(url_for('usedsupply.list'))
    return render_template('delete_usedsupply.html',form=form)
