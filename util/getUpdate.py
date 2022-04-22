import requests, version, re, webbrowser
import jpower

def check_version():
    local_version = version.ver

    try:response = requests.get('https://pastebin.com/raw/T36vsDcx').text
    except:
        jpower.msgbox_error('Ошибка', 'Не удалось установить последнюю версию...')
        response = None

    if response != None:
        github_version = float(re.split('=', response.strip())[1])

        if github_version > local_version:
            jpower.msgbox_info('Информация', 'Обнаружена новая версия программы!')
            try:webbrowser.open('https://jesewe.wixsite.com/hack/jesewe-tools')
            except:pass