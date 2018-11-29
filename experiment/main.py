from flask import Flask, render_template, request
app = Flask(__name__)
import os
import random


poll_data = {
   'question' : 'Which trumpet has an onset marked?',
   'fields'   : ['onset', 'onset-50', 'onset-25', 'onset+25', 'onset+50']
}

random.shuffle(poll_data['fields'])

@app.route('/')
def root():
    return render_template('main.html')

@app.route('/train')
def train():
    return render_template('train.html')

@app.route('/trumpet')
def trumpet():
    random.shuffle(poll_data['fields'])
    return render_template('trumpet.html', data=poll_data)

@app.route('/votetrumpet')
def votetrumpet():
    vote = request.args.get('chosed')
    answer = poll_data['fields'][int(vote[0])]

    out = open('Trumpet.txt', 'a')
    out.write( answer + '\n' )
    out.close()

    return render_template('trumpet-labels.html', data=poll_data, label=answer)

@app.route('/clarinet')
def clarinet():
    random.shuffle(poll_data['fields'])
    return render_template('clarinet.html', data=poll_data)

@app.route('/voteclarinet')
def voteclarinet():
    vote = request.args.get('chosed')
    answer = poll_data['fields'][int(vote[0])]

    out = open('Clarinet.txt', 'a')
    out.write( answer + '\n' )
    out.close()

    return render_template('clarinet-labels.html', data=poll_data, label=answer)

@app.route('/violin')
def violin():
    random.shuffle(poll_data['fields'])
    return render_template('violin.html', data=poll_data)

@app.route('/voteviolin')
def voteviolin():
    vote = request.args.get('chosed')
    answer = poll_data['fields'][int(vote[0])]

    out = open('Violin.txt', 'a')
    out.write( answer + '\n' )
    out.close()

    return render_template('violin-labels.html', data=poll_data, label=answer)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
