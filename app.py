from flask import Flask, request
import json

@app.route('/')
def index():
    
    my_html =  '''
    <html>
    <body style='background-image: linear-gradient(to right, #d4d3dd, white);'>
    
        <h1 style='color: violet'; 'font-size:24'; 'text-align:center';>{update}</h1>
        <h2> <p><a href="https://tg-resending-bot.vercel.app/set_webhook">Ткни сюда установить вэбхук!!</a></p> </h2>
  
    </body>
    </html>
    '''
    
    return my_html
