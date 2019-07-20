from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.supply.forms import AddForm,DelForm, UpdateForm, QueryForm
from myproject.models import Supply

supply_blueprint = Blueprint('supply',
                              __name__,
                              template_folder='templates/supply')

# my_filters = {'name_last':'Duncan', 'name_first':'Iain'}
# query = session.query(User)
# for attr,value in my_filters.iteritems():
#     query = query.filter( getattr(User,attr)==value )
# # now we can run the query
# results = query.all()
@supply_blueprint.route('/query', methods=['GET', 'POST'])
def query():
    applied_filter = {}
    form = QueryForm()
    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        type = form.type.data
        results = Supply.query.filter()
        if id != '':
            results = results.filter(Supply.id == id)
        if name != '':
            results = results.filter(Supply.name == name)
        if type != '':
            results = results.filter(Supply.type == type)

        
        return render_template('queryresult_supply.html',supplies = results)
    return render_template('query_supply.html',form=form)


@supply_blueprint.route('/update', methods=['GET', 'POST'])
def update():
    form = UpdateForm()
    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        type = form.type.data 

        supply = Supply.query.get(id)
        supply.name = name 
        supply.type = type 
        db.session.add(supply)
        db.session.commit()
        return redirect(url_for('supply.list'))
    return render_template('update_supply.html',form=form)

@supply_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        type = form.type.data 

        # Add new Puppy to database
        new_supply = Supply(name, type)
        db.session.add(new_supply)
        db.session.commit()

        return redirect(url_for('supply.list'))

    return render_template('add_supply.html',form=form)

@supply_blueprint.route('/list')
def list():
    # Grab a list of puppies from database.
    supplies = Supply.query.all()
    return render_template('list_supply.html', supplies=supplies)


@supply_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        supply = Supply.query.get(id)
        db.session.delete(supply)
        db.session.commit()

        return redirect(url_for('supply.list'))
    return render_template('delete_supply.html',form=form)
