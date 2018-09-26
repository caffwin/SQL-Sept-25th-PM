"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add-form")
def student_form():    
    return render_template("new_student.html")



@app.route("/student-add", methods=['POST'])
def student_add():
    # one form for display and another for processing results

    first_name= request.form.get("first_name")
    last_name= request.form.get("last_name")
    github= request.form.get("github")

    hackbright.make_new_student(first_name, last_name, github)
    # var = request.forms.get("")
    return render_template("welcome_new.html", first_name=first_name, last_name=last_name, github=github)

    # print("".format(first_name, last_name))


@app.route("/student")
def get_student():
    """Show information about a student."""

    # github = "jhacks"
    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    # make one more query for projects and grade for project
    project_title, grade = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)

    # return "{} is the GitHub account for {} {}".format(github, first, last)
    return html 

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
