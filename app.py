from flask import Flask, render_template, redirect, request
import interface
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('landing.html')

@app.route('/swipe')
def start():
    profile = interface.request_user_profile_from_backend()
    return render_template('index.html', name=profile.name, age=profile.age, location="None", bio=profile.bio, pfimg=profile.profile_picture)

@app.route('/refresh')
def refresh():
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verify', methods=['POST'])
def verify():
    name = request.form['name']
    print(name)
<<<<<<< HEAD
    return redirect('/swipe')
=======
    profile = load_user_profile(name)
    print(profile)
    if profile == None:
>>>>>>> 42d9418c7627549dc0dd69cf6026582c2a9db888

@app.route('/like')
def like():
    #input ML for like
    return redirect('/swipe')

@app.route('/dislike')
def dislike():
    #input ML for dislike
    return redirect('/swipe')

if __name__ == '__main__':
    app.run()


