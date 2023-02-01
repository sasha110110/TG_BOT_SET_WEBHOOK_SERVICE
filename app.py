import telegram
from telegram.ext import Updater , CommandHandler , Filters , MessageHandler
from telegram import ParseMode
from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length


#updater = Updater(token=TOKEN, use_context=True)

app = Flask(__name__)

class SetBotForm(FlaskForm):
    host=StringField("ХОСТ", [validators.DataRequired()])
    bot_token = StringtField("ТОКЕН бота", [validators.DataRequired()])
    submit = SubmitField("Send")


@app.route('/', methods= ["POST", "GET"])
def set_bot():

    form = SetBotForm()
    if form.validate_on_submit():
        HOST=form.host.data
        TOKEN = form.bot_token.data
        global bot
        bot = telegram.Bot(token=TOKEN)
        #updater = Updater(token=TOKEN, use_context=True)
        if reqest.form["set"]:
            bot.deleteWebhook()
            time.sleep(2)
            s = bot.setWebhook(f"{HOST}/{TOKEN}")
            if s:
                return "Вэбхук успешно установлен! \n"+str(bot.getWebhookInfo())
            else:
                return "Не получилось установить вэбхук! Попробуй еще раз."
        if reqest.form["show"]:
            return str(bot.getWebhookInfo())
        if reqest.form["delete"]:
            bot.deleteWebhook()
            return "Вэбхук успешно удален!"
        
        
    return render_template('index.html', form=form)

#app.run(debug=True)
