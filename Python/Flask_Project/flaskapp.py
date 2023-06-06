from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'


class NewStudentForm(FlaskForm):
    name = StringField('Όνομα', validators=[DataRequired()])
    surname = StringField('Επώνυμο', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    age = IntegerField('Ηλικία', validators=[DataRequired()])
    submit = SubmitField('Υποβολή')

app.config['SECRET_KEY'] = '0c9e249f30815b0341df0179a9927089'
app.config['WTF_CSRF_SECRET_KEY'] = '87152d3840f6c1bceb491e70ac9083fc'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'st_admin'
app.config['MYSQL_PASSWORD'] = 'myadmin'
app.config['MYSQL_DB'] = 'students_db'
 
mysql = MySQL(app)




@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template('home.html')


@app.route('/students')
def students():

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM STUDENTS ORDER BY SURNAME ASC")
    data=cursor.fetchall() 
    print(data)
    cursor.close() 

    return render_template('students.html', data=data)

@app.route('/new_student', methods=['GET', 'POST'])
def new_student():

    form = NewStudentForm()

    
    if request.method == 'POST' and form.validate_on_submit():

        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        age = form.age.data

        cur = mysql.connection.cursor()
        insert_stmt = ("INSERT INTO students (name, surname, email, age) "
                    "VALUES (%s, %s, %s, %s)"
                    )
        
        data = (name, surname, email, age)
        cur.execute(insert_stmt, data)
        mysql.connection.commit()
        cur.close()

        flash("Η καταχώριση ολοκληρώθηκε επιτυχώς", "success")

    

        # if form submitted correctly redirect to students pages
        return redirect(url_for('students'))

    # if form is not submitted (page called by GET method) show the form
    return render_template('newstudent.html', form=form)

@app.route('/update_student', methods=['GET', 'POST'])
def update_student():

    
    if request.method == 'POST':
            id = request.form['id']
            name = request.form['name']
            surname = request.form['surname']
            email = request.form['email']
            age = request.form['age']
            
            cur = mysql.connection.cursor()
            update_stmt = ("UPDATE students SET name=%s, surname=%s, email=%s, age=%s WHERE id=%s "
                            )
            data = (name, surname, email, age, id)
            cur.execute(update_stmt, data)
    

            mysql.connection.commit()

            flash("Η ενημέρωση ολοκληρώθηκε επιτυχώς", "success")


            return redirect(url_for('students'))


@app.route('/delete_student/<int:id>')
def delete_student(id):

    cursor = mysql.connection.cursor()
    cursor.execute(f"DELETE FROM students WHERE id='{id}'")
    mysql.connection.commit()
    cursor.close() 

    flash("Η διαγραφή ολοκληρώθηκε επιτυχώς", "success")


    return redirect(url_for('students'))


@app.route('/about')
def about():
    
   

    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
