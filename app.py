from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route('/home')
def show_home():
  
  return render_template('home.html', fillers=story.prompts)

@app.route('/story')
def show_story():
  return render_template('story.html', story_gen = story.generate(request.args))