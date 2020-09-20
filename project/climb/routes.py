from flask import Flask, render_template, url_for, flash, redirect, request
from climb import app, db
from climb.models import Record 
from climb.forms import Add_record


@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page',1,type=int)
    records = Record.query.paginate(page=page, per_page=12)
    return render_template("home.html", records=records)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/routes/new", methods=['GET', 'POST'])
def new_route():
    form = Add_record()
    if form.validate_on_submit():
        record = Record(name=form.name.data, grade=form.grade.data, sector=form.sector.data, location=form.location.data, date=form.date.data)
        db.session.add(record)
        db.session.commit()
        flash('New route has been added!', 'success')
        return redirect(url_for('home'))
    return render_template('new_route.html', form=form, legend='Add new route', button_name='Add')

@app.route("/routes/<int:record_id>/delete", methods=['POST'])
def delete(record_id):
    record = Record.query.get_or_404(record_id)
    db.session.delete(record)
    db.session.commit()
    flash('Your record has been deleted!', 'success')
    return redirect(url_for('home'))

@app.route("/routes/<int:record_id>/update", methods=['GET', 'POST'])
def update(record_id):
    record = Record.query.get_or_404(record_id)
    form = Add_record()
    if form.validate_on_submit():
        record.name = form.name.data
        record.grade = form.grade.data
        record.sector = form.sector.data
        record.location = form.location.data
        record.style = form.style.data
        record.date = form.date.data
        db.session.commit()
        flash('Your record has been updated!', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.name.data = record.name
        form.grade.data = record.grade
        form.sector.data = record.sector
        form.location.data = record.location
        form.style.data = record.style
        form.date.data = record.date
    return render_template('new_route.html', form=form, legend='Update information', button_name='Edit')

@app.route("/sort/location")
def sort_by_location():
    page = request.args.get('page',1,type=int)
    records = Record.query.order_by(Record.location).paginate(page=page, per_page=12)
    return render_template("home.html", records=records)

@app.route("/sort/grade")
def sort_by_grade():
    page = request.args.get('page',1,type=int)
    records = Record.query.order_by(Record.grade.desc()).paginate(page=page, per_page=12)
    return render_template('home.html', records=records)

@app.route("/sort/sector")
def sort_by_sector():
    page = request.args.get('page',1,type=int)
    records = Record.query.order_by(Record.sector).paginate(page=page, per_page=12)
    return render_template('home.html', records=records)
    
@app.route("/sort/name")
def sort_by_name():
    page = request.args.get('page',1,type=int)
    records = Record.query.order_by(Record.name).paginate(page=page, per_page=12)
    return render_template('home.html', records=records)

@app.route("/sort/date")
def sort_by_date():
    page = request.args.get('page',1,type=int)
    records = Record.query.order_by(Record.date.desc()).paginate(page=page, per_page=12)
    return render_template('home.html', records=records)
