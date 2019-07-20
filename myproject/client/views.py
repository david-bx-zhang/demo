from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.client.forms import AddForm,DelForm,UpdateForm,QueryForm
from myproject.models import Client

client_blueprint = Blueprint('client',
                              __name__,
                              template_folder='templates/client')


@client_blueprint.route('/query', methods=['GET', 'POST'])
def query():
    form = QueryForm()
    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        bill_info = form.bill_info.data
        

        results = Client.query.filter()
        if id != '':
            results = results.filter(Client.id == id)
        if name != '':
            results = results.filter(Client.name == name)
        if bill_info != '':
            results = results.filter(Client.bill_info == bill_info)
        

        return render_template('queryresult_client.html',clients = results)
    return render_template('query_client.html',form=form)


@client_blueprint.route('/update', methods=['GET', 'POST'])
def update():

    
    form = UpdateForm()

    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        bill_info = form.bill_info.data
        

        # Add new Puppy to database
        client = Client.query.get(id)
        client.name = name 
        client.bill_info = bill_info 
        db.session.add(client)
        db.session.commit()

        return redirect(url_for('client.list'))

    return render_template('update_client.html',form=form)


@client_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        bill_info = form.bill_info.data
        

        # Add new Puppy to database
        new_client = Client(name, bill_info)
        db.session.add(new_client)
        db.session.commit()

        return redirect(url_for('client.list'))

    return render_template('add_client.html',form=form)

@client_blueprint.route('/list')
def list():
    # Grab a list of puppies from database.
    clients = Client.query.all()
    
    return render_template('list_client.html', clients = clients)


@client_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        client = Client.query.get(id)
        db.session.delete(client)
        db.session.commit()

        return redirect(url_for('client.list'))
    return render_template('delete_client.html',form=form)
