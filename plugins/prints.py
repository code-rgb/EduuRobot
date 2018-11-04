import config
import urllib

bot = config.bot


def prints(msg):
    if msg.get('text'):
        if msg['text'].startswith('/print ') or msg['text'].startswith('!print '):
            try:
                bot.sendPhoto(msg['chat']['id'], f"https://api.thumbnail.ws/api/{config.keys['screenshots']}/thumbnail/get?url={urllib.parse.quote_plus(msg['text'][7:])}/&width=1280",
                              reply_to_message_id=msg['message_id'])
            except:
                bot.sendMessage(msg['chat']['id'], 'Ocorreu um erro ao enviar a print, favor tente mais tarde.',
                                reply_to_message_id=msg['message_id'])
            return True
