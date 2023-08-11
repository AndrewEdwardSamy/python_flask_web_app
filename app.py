from flask import Flask, render_template, request
from common.database import Database
from models.servant import Servant

# def create_app():
app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html", title='Archangel Michael',)


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route("/add_servant/", methods=['GET','POST'])
def add_servant():
    intelligence_type_list = Servant().intelligence_type_list()
    skill_list = Servant().skill_list()
    Servant().add_servant()
    return render_template("add_servant.html", title='Add Servant',intelligence_type_list=intelligence_type_list, skill_list=skill_list)

@app.route('/all_servants/')
def all_servants():
    all_servants = Servant().all_servants()
    return render_template("all_servants.html", title='All Servants', all_servants=all_servants)

@app.route('/all_servants/profile/<id>')
def profile(id):
    servant = Servant().findby_id(id)
    return render_template("profile.html", title='Profile',servant=servant)


@app.route('/test/',methods=['GET','POST'])
def test():
    return render_template("test.html", title='test')


#     return app



# app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
