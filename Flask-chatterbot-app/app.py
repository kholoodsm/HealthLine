# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 06:27:49 2019

@author: anshu
"""

from flask import Flask,render_template, request
app = Flask(__name__)
import chatterbot
from chatterbot.trainers import ListTrainer
bot = chatterbot.ChatBot('smartbot')
trainer = ListTrainer(bot)
trainer.train("Medicina.ai")

import os
folder = "Medicina"
files = os.listdir(folder)
for file in files:
    if "txt" in file:
        data = open(folder+"//"+file).readlines()
        trainer.train(data)

@app.route('/',methods=['POST','GET'])
def main():
    return render_template("index.html")

@app.route('/get')
def get_response():
    userqus = request.args.get('msg')
    return str(bot.get_response(userqus))
if __name__=='__main__':
    app.run(debug=True)