from flask import Flask, request, render_template
import subprocess
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("final.html")

@app.route('/redirect')
def redirect():
    return render_template('first.html')

@app.route("/tech")
def mytech():
    mycmd = request.args.get("cmd")
    return "<pre>" + subprocess.getoutput(mycmd) + "</pre>"

@app.route('/automate', methods=['GET', 'POST'])
def automate():
    if request.method == 'POST':
        choice = request.form.get('choice')
        dirname = request.form.get('dirname')
        filename = request.form.get('filename')
        containername = request.form.get('containername')

        output = None

        if choice == '1':
            output = subprocess.getoutput('date')
        elif choice == '2':
            output = subprocess.getoutput('pwd')
        elif choice == '3':
            output = subprocess.getoutput('ls')
        elif choice == '4':
            if dirname:
                subprocess.getoutput('mkdir ' + dirname)
                output = 'Directory created successfully.'
            else:
                output = 'Please enter a directory name.'
        elif choice == '5':
            if dirname:
                subprocess.getoutput('rmdir ' + dirname)
                output = 'Directory removed successfully.'
            else:
                output = 'Please enter a directory name.'
        elif choice == '6':
            if filename:
                subprocess.getoutput('touch ' + filename)
                output = 'File created successfully.'
            else:
                output = 'Please enter a file name.'
        elif choice == '7':
            if filename:
                subprocess.getoutput('nano ' + filename)
                output = 'File edited successfully.'
            else:
                output = 'Please enter a file name.'
        elif choice == '8':
            if filename:
                output = subprocess.getoutput('cat ' + filename)
            else:
                output = 'Please enter a file name.'
        elif choice == '9':
            if filename:
                subprocess.getoutput('rm ' + filename)
                output = 'File removed successfully.'
            else:
                output = 'Please enter a file name.'
        elif choice == '10':
            output = subprocess.getoutput('docker')
        elif choice == '11':
            output = subprocess.getoutput('docker ps')
        elif choice == '12':
            if containername:
                subprocess.getoutput('docker run -itd --name ' + containername + ' ubuntu')
                output = 'Container created successfully.'
            else:
                output = 'Please enter a container name.'
        elif choice == '13':
            if containername:
                subprocess.getoutput('docker stop ' + containername)
                output = 'Container stopped successfully.'
            else:
                output = 'Please enter a container name.'
        elif choice == '14':
            if containername:
                subprocess.getoutput('docker rm ' + containername)
                output = 'Container removed successfully.'
            else:
                output = 'Please enter a container name.'
        elif choice == '15':
            output = subprocess.getoutput('docker images')
        elif choice == '16':
            image_id = request.form.get('imageid')
            if image_id:
                subprocess.getoutput('docker rmi ' + image_id)
                output = 'Image removed successfully.'
            else:
                output = 'Please enter an image ID.'
        elif choice == '17':
            exit()

        return render_template("automation.html", output=output)

    # Handle GET request method
    return render_template("automation.html")

@app.route("/sign", methods=['GET'])
def mysign():
    name = request.args.get("nm")
    email = request.args.get("em")
    mob = request.args.get("pmo")
    password = request.args.get("pm")
    First = request.args.get("fm")
    last = request.args.get("lm")
    le = request.args.get("le")
    lmess = request.args.get("lmess")

    with sql.connect("database.db") as con, sql.connect("Contact_us.db") as conu:
        cur = con.cursor()
        curt = conu.cursor()
        cur.execute("INSERT INTO students (name, Email, Mobile, Password) VALUES (?,?,?,?)", (name, email, mob, password))
        curt.execute("INSERT INTO contacts (First, last, le, Message) VALUES (?,?,?,?)", (First, last, le, lmess))
        con.commit()
        conu.commit()
        print("Record successfully added")

    return render_template("fl_check.html")

if __name__ == '__main__':
    app.run()