from flask import Flask, render_template, url_for, flash, redirect, request
from climb import app, db
from climb.models import Record 
from climb.forms import Add_record


@app.route("/")
@app.route("/home")
def home():
    records = Record.query.all()
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
    return render_template('new_route.html', form=form, legend='Add route', button_name='Add')

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
        record.date = form.date.data
        db.session.commit()
        flash('Your record has been updated!', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.name.data = record.name
        form.grade.data = record.grade
        form.sector.data = record.sector
        form.location.data = record.location
        form.date.data = record.date
    return render_template('new_route.html', form=form, legend='Update information', button_name='Edit')

@app.route("/sort/location")
def sort_by_location():
    records = Record.query.order_by(Record.location).all()
    return render_template('home.html', records=records)

@app.route("/sort/grade")
def sort_by_grade():
    records = Record.query.order_by(Record.grade).all()
    return render_template('home.html', records=records)

@app.route("/sort/sector")
def sort_by_sector():
    records = Record.query.order_by(Record.sector).all()
    return render_template('home.html', records=records)
    
@app.route("/sort/name")
def sort_by_name():
    records = Record.query.order_by(Record.name).all()
    return render_template('home.html', records=records)

@app.route("/sort/style")
def sort_by_style():
    records = Record.query.order_by(Record.style).all()
    return render_template('home.html', records=records)