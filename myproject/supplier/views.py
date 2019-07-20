from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.supplier.forms import AddForm,DelForm, UpdateForm, QueryForm
from myproject.models import Supplier

supplier_blueprint = Blueprint('supplier',
                              __name__,
                              template_folder='templates/supplier')
@supplier_blueprint.route('/query', methods=['GET', 'POST'])
def query():
    form = QueryForm()
    if form.validate_on_submit():
        id = form.id.data 
        name = form.name.data
        type = form.type.data 
        unit_price = form.unit_price.data 
        contact = form.contact.data 
        supply_id = form.supply_id.data

        results = Supplier.query.filter()
        if id != '':
            results = results.filter(Supplier.id == id)
        if name != '':
            results = results.filter(Supplier.name == name)
        if type != '':
            results = results.filter(Supplier.type == type)
        if unit_price != '':
            results = results.filter(Supplier.unit_price == unit_price)
        if contact != '':
            results = results.filter(Supplier.contact == contact)
        if supply_id != '':
            results = results.filter(Supplier.supply_id == supply_id)

        return render_template('queryresult_supplier.html',suppliers = results)
    return render_template('query_supplier.html',form=form)


@supplier_blueprint.route('update', methods=['GET', 'POST'])
def update():

    
    form = UpdateForm()

    if form.validate_on_submit():
        id = form.id.data 
        name = form.name.data
        type = form.type.data 
        unit_price = form.unit_price.data 
        contact = form.contact.data 
        supply_id = form.supply_id.data

        supplier = Supplier.query.get(id)
        supplier.name = name 
        supplier.type = type 
        supplier.unit_price = unit_price
        supplier.contact = contact 
        supplier.supply_id = supply_id 

        # Add new Puppy to database
        db.session.add(supplier)
        db.session.commit()

        return redirect(url_for('supplier.list'))

    return render_template('update_supplier.html',form=form)

@supplier_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        type = form.type.data 
        unit_price = form.unit_price.data 
        contact = form.contact.data 
        supply_id = form.supply_id.data

        # Add new Puppy to database
        new_supplier = Supplier(name, type,unit_price, contact, supply_id)
        db.session.add(new_supplier)
        db.session.commit()

        return redirect(url_for('supplier.list'))

    return render_template('add_supplier.html',form=form)

@supplier_blueprint.route('/list')
def list():
    # Grab a list of puppies from database.
    suppliers = Supplier.query.all()
    print("supplier list called ######")
    return render_template('list_supplier.html', suppliers=suppliers)


@supplier_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        supplier = Supplier.query.get(id)
        db.session.delete(supplier)
        db.session.commit()

        return redirect(url_for('supplier.list'))
    return render_template('delete_supplier.html',form=form)
