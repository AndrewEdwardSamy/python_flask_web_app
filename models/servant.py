from flask import Flask, request
from bson.objectid import ObjectId
from common.database import Database
import datetime


class Servant:
    def pp(self):
        print('test print')
    
    def intelligence_type_list(self):
        return [ x['intelligence_type'] for x in Database.find(collection='intelligence_type', query='')]
    
    def skill_list(self):
        return [ x['skill'] for x in Database.find(collection='skill', query='')]

    def add_servant(self):
        servant_disc = []
        servant_intelligence = []
        servant_skill = []

        if request.method == "POST":
            for i in 'DISC':
                if request.form.get(i) != None:
                    servant_disc.append(request.form.get(i))
            
            for x in self.intelligence_type_list():
                if request.form.get(x) != None:
                    servant_intelligence.append(request.form.get(x))
            
            for s in self.skill_list():
                if request.form.get(s) != None:
                    servant_skill.append(request.form.get(s))

            servant_data = {
                'date' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'fname' : request.form.get("fname"),
                'lname' : request.form.get("lname"),
                'identity' : request.form.get("identity"),
                'address' : request.form.get("address"),
                'block' : request.form.get("block"),
                'phone' : request.form.get("phone"),
                'whats' : request.form.get("whats"),
                'father_of_confession' : request.form.get("father_of_confession"),
                'pre_graduation_year' : request.form.get("pre_graduation_year"),
                'pre_grade' : request.form.get("pre_grade"),
                'pre_church' : request.form.get("pre_church"),
                'membership' : request.form.get("membership"),
                'disc' : servant_disc,
                'intelligence_type' : servant_intelligence,
                'skill' : servant_skill,
                'course' : request.form.get("course"),
                'note' : request.form.get("note")
            }
            print(servant_data)
            Database.insert(collection='servant', data=servant_data)


    def all_servants(self):
        all_servants = Database.find(collection='servant', query='')
        return [servant for servant in all_servants]

    def findby_id(self, id):
        servant = Database.find_one(collection='servant', query={'_id':ObjectId(id)})
        return servant
