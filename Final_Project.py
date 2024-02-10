from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup
import datetime
import random
listName = []
listDes = []
listHref = []
def parser():
    global listName
    global listDes
    global listHref
    url = "https://uaserials.pro/films/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    for a in soup.find_all('a', href=True):
        u = a['href']
        if u.startswith("http"):
            listHref.append(u)
            requst = requests.get(u)
            soup1 = BeautifulSoup(requst.text, features="html.parser")
            soup_list_name = soup1.find_all('span', {'class': 'oname_ua'})
            if len(soup_list_name) > 0:
                listName.append(soup_list_name[0].text)
            soup_list_ul = soup1.find_all('ul', {'class': 'short-list fx-1'})
            for i in soup_list_ul:
                listDes.append(i.text)
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    comands = "hello, film, searchFilm, filmInfo, filmByNumber, now"
    await update.message.reply_text(f'це команди бота {comands}')

async def randomiser(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    random = randint(1, 100)
    await update.message.reply_text(f'ваше рандомне число {random}')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.full_name}')
    
async def now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = datetime.datetime.now()
    await update.message.reply_text(f'{now}')

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    parser()
    for film in range(len(listName)):
        await update.message.reply_text(f'{listName[film]} \n{listDes[film]}\n{listHref[film]}')
        
async def filmByNumber(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    number = int(update.message.text.split(" ")[1]) - 1
    parser()
    if 0 <= number < len(listName):
        await update.message.reply_text(f'{listName[number]} \n{listDes[number]}\n{listHref[number]}')
    else:
        await update.message.reply_text(f'Фільм з номером {number + 1} не знайдено.')

async def searchFilm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    parser()
    search_query = update.message.text.split(" ")[1]
    for film in range(len(listName)):
        if search_query.lower() in listName[film].lower():
            await update.message.reply_text(f'{listName[film]} \n{listDes[film]}\n{listHref[film]}')
            break
    else:
        await update.message.reply_text(f'Фільм з назвою "{search_query}" не знайдено.')

async def filmInfo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = update.message.text.split(" ")[1]
    requst = requests.get(url)
    soup = BeautifulSoup(requst.text, features="html.parser")
    soup_list_name = soup.find_all('span', {'class': 'oname_ua'})
    if len(soup_list_name) > 0:
        film_name = soup_list_name[0].text
    soup_list_ul = soup.find_all('ul', {'class': 'short-list fx-1'})
    for i in soup_list_ul:
        film_des = i.text
    await update.message.reply_text(f'{film_name} \n{film_des}\n{url}')

app = ApplicationBuilder().token("5131642226:AAE89c94uSifu9_J3PlBOhC4Jk9Jy5xRwzo").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("now", now))
app.add_handler(CommandHandler("film", film))
app.add_handler(CommandHandler("filmByNumber", filmByNumber))
app.add_handler(CommandHandler("filmInfo", filmInfo))
app.add_handler(CommandHandler("searchFilm", searchFilm))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("random", randomiser))

app.run_polling()
