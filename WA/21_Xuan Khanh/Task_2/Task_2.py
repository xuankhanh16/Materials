from flask import Flask, render_template

import csv

def task_1(filename):
    with open(filename) as f:
        pointer = csv.reader(f)
        data = [i for i in pointer]
        sorted_data = data.sort(key = lambda x : x[4], reverse=True)
        # data is not sorted in descending order, you should return sorted_data
    return data



records = task_1("2003_2017_waste.csv")

records = [i for i in records if i[0] in ("Plastics", "Glass", "Paper/Cardboard")]

#print (records)

app = Flask (__name__)

app.route("/") # should be prepended with @
def show_data():
    return render_template("Task2.html", records = records) #name of html file need to be consistent, the name indicated here is different from the name of actual html file
    
    # return "Hello"

app.run()