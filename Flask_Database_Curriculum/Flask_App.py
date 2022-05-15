from flask_mysqldb import MySQL
from markupsafe import Markup
from flask import Flask, redirect, render_template, request, url_for, session
 
app = Flask(__name__)
app.secret_key = "Its a secret duh"

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "password"
app.config['MYSQL_DB'] = "blog_db"
mysql = MySQL(app)

@app.route("/", methods=['GET','POST'])
def index():
    if 'username' in session:
        if request.method == "POST":
            print(request.form)
            if 'delete' in request.form:
                PID = request.form['delete']
                posts = Delete(PID)
                return render_template("index.html", posts=posts) 

            tittle = request.form["post_title"]
            message = request.form["post_body"]
            poster = session["username"]
            USID = session["USID"]

            cursor = mysql.connection.cursor()
            cursor.execute(''' INSERT INTO posts VALUES(null,%s,%s,%s,%s,CURRENT_TIMESTAMP) ''', [USID,tittle,message,poster])
            mysql.connection.commit()
            cursor.close()

            posts = PopulatePosts()
            return render_template("index.html", posts=posts)
        else:
            posts = PopulatePosts()
            return render_template("index.html", posts=posts)
    else:
        return render_template("log_in.html")


@app.route("/log_in", methods=['GET','POST'])
def log_in():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if CreateSession(username, password):
            return redirect(url_for('index'))
        else:
            return render_template("log_in.html")    
    else:
        return render_template("log_in.html")


@app.route("/sign_up", methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM users WHERE username = %s ''',[username])
        username_Check = cursor.fetchall()
        cursor.close()


        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO users VALUES(null,%s,%s) ''', [username, password])
        mysql.connection.commit()
        cursor.close()

        CreateSession(username,password)

        return redirect(url_for('index'))
    else:
        return render_template('sign_up.html')


@app.route('/sign_out')
def sign_out():
    if "username" in session:
        session.pop("USID", None)
        session.pop("username", None)
        return redirect(url_for("log_in"))
    else:
        return redirect(url_for("log_in"))



"""
    Functions that are used multiple times to cut down on code length
"""
def CreateSession(username,password):
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM users WHERE username LIKE '{0}' '''.format(username))
    user = cursor.fetchall()
    cursor.close()

    if password == user[0][2]:
        session["username"] = user[0][1]
        session["USID"] = user[0][0]
        return True
    else:
        return False


def Delete(PID):
    cursor = mysql.connection.cursor()
    cursor.execute(''' DELETE FROM posts WHERE PID = %s  ''', [PID])
    mysql.connection.commit()
    cursor.close()

    posts = PopulatePosts()
    return posts
    

def PopulatePosts():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM posts ''')
    data = cursor.fetchall()
    cursor.close()

    posts = ""
    for post in data:
        PID = f"{post[0]}"
        post_tittle = post[2]
        post_body = post[3]
        poster = post[4]
        date = f"{post[5]}"

        posts += Markup("""  
                            <div class="card text-white bg-dark mb-3">
                                <div class="card-header" name="post_tittle">"""+ post_tittle +"""</div>
                                <div class="card-body" name="post_body">
                                    <blockquote class="blockquote mb-0">
                                        <p>"""+ post_body +"""</p>
                                        <footer class="blockquote-footer">Posted by 
                                        <cite title="Source Title" name="username">"""+ poster +"""</cite>
                                            on """ + date
                        )

        if session["username"] == poster:        
            posts += Markup("""                          
                                            <form class="delete" method="POST" href="delete"><button type="submit" name="delete" value=" """+ PID +"""  " class="btn btn-danger">DELETE</button></form>
                                            </footer>
                                        </blockquote>
                                    </div>
                                </div>
                            """)
        else:
            posts += Markup("""                           
                                            </footer>
                                        </blockquote>
                                    </div>
                                </div>
                            """)
    return posts


if __name__ == ("__main__"):
    app.run(debug=True)
