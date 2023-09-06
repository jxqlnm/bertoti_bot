import telebot
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.starcoder import Starcoder
 
API_TOKEN = '6349846228:AAGWDn7CRHdhDQZd39RMgricPPFuv6nXqUY'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def reply_hi(message):
  bot.reply_to(message, 'hallo! wie gehts? ')

bot.polling()

llm = Starcoder(api_token="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")

df = pd.read_csv("https://raw.githubusercontent.com/inteligentni/Class-05-Feature-engineering/master/The%20Beatles%20songs%20dataset%2C%20v1%2C%20no%20NAs.csv")

pandas_ai = PandasAI(llm, conversational=False)
res = pandas_ai.run(df, prompt='what songs belong to abbey road album')
res['Title'].to_string(index=False)


@bot.message_handler(func=lambda message: True)
def response(message):

  response = pandas_ai.run(df, prompt=message.text)


  bot.reply_to(message, response['Title'].to_string(index=False))
     

bot.polling()



