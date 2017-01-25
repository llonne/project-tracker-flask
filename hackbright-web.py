from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    #print github
    first, last, github = hackbright.get_student_by_github(github)
    projects = hackbright.get_grades_by_github(github)
    #print projects
    html = render_template("student_info.html",
                            first = first,
                            last = last,
                            github = github,
                            projects=projects
                            )

    return html
    # github = "jhacks"
    # first, last, github = hackbright.get_student_by_github(github)
    # return "%s is the GitHub account for %s %s" % (github, first, last)
@app.route("/project")
def get_student():
    """Show information about a student."""

    title = request.args.get('title', 'Markov')
    #print github
    title, description, max_grade = hackbright.get_project_by_title(github)
    #projects = hackbright.get_grades_by_github(github)
    #print projects
    html = render_template("project_info.html",
                            title=title,
                            description=description,
                            max_grade=max_grade
                            # first = first,
                            # last = last,
                            # github = github,
                            # projects=projects
                            )

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add-form")
def student_form_add():
    return render_template("student_add.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    github = request.form.get('github')
    first = request.form.get('first')
    last = request.form.get('last')

    hackbright.make_new_student(first, last, github)

    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)
    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
