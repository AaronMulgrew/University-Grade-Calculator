
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, FieldList, FormField
 
# App config.
#DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    module = TextField('Module Grade:', validators=[validators.required()])
    weight = TextField('Weighting:', validators=[validators.required()])
 
class BusinessForm(Form):
    #name = StringField('Business Name')
    grades = FieldList(FormField(ReusableForm), min_entries=8, max_entries=10)

def CalcOverall(Weightings, Grades):
    gradewithWeight = []
    overallWeighting = 0
    gradeWeightInt = 0
    # iterate over the Weightings list using integer rather than elements
    for i in xrange(len(Weightings)):
        # skip element if cannot convert to float
        try:
            float(Grades[i])
        except:
            continue
        print Weightings[i]
        print Grades[i]
        gradeFloat = float(Grades[i])/100
        overallWeighting += float(Weightings[i])
        gradewithWeight.append(gradeFloat * float(Weightings[i]))
    for element in gradewithWeight:
        gradeWeightInt += element
    print "Overall Weighting" + str(overallWeighting)
    print "Weight: " + str(gradeWeightInt)
    print "List: " + str(gradewithWeight)
    print "Percentage Overall: " + str(gradeWeightInt * 100 / overallWeighting)
    OverallPercentage = str(gradeWeightInt * 100 / overallWeighting)
    return OverallPercentage

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = BusinessForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        moduledict = dict(request.form)
        print moduledict

        weightings = moduledict['weight']
        grades = moduledict['module']
        OverallGrade = CalcOverall(weightings, grades)
        return render_template('results.html', results=OverallGrade)
    return render_template('grades.html', form=form)
 
if __name__ == "__main__":
    app.run()