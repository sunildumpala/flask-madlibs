from flask import Flask, render_template
from stories import story

app = Flask(__name__)

@app.route('/home')
def show_home():
  
  return render_template('home.html', fillers=story.prompts)

@app.route('/story')
def show_story():
  print(f"Prompts: {story.prompts}")
  print(f"Template: {story.template}")
  ans = {"place":"condo", "noun":"dragon", "verb":"eat", "adjective":"frozen", "plural_noun":"popsicles"}
  # return story.generate(ans)
  return render_template('story.html', story_gen = story.generate(ans))