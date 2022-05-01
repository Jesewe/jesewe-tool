from util.getUpdate import *
from util.getFunctions import *
import jpower
import os
import time
import ctypes
import pymem, re
import colorama
import urllib.request
from colorama import Fore, Style, Back, init
init(convert=True)

jpower.window_title('Jesewe Tools 1.4')
if not os.path.isdir("C:\Jesewe Tools"):
     os.mkdir("C:\Jesewe Tools")

print(Fore.YELLOW + 'Проверка обновлений...')
check_version()

while True:
    os.system("cls")
    print(Fore.YELLOW + 'Jesewe Tools')
    print(Fore.CYAN + '\n[1] Читы для CS:GO\n[2] Читы для Minecraft\n[3] Steam VAC Bypass Loader\n[4] EZInjector Reborn\n[5] Информация о видеокарте')
    try:
        choose=int(input(Fore.YELLOW + '\nВыберите число > '))
    except Exception as e:
        os.system("cls")
        input(Fore.RED + '[!] Вы ввели недопустимое значение, попробовать еще раз? ')
        os.system("cls")
    else:
        if choose==1:
            try:
                os.system("cls")
                print(Fore.YELLOW + 'CS:GO - Cheat Loader')
                print(Fore.CYAN + '\n[1] Функция WallHack\n[2] Функция ShowMoney\n[3] Osiris\n[4] OneTap V3 Crack\n[5] Aurora\n[6] Victoria\n[7] ThrillTrip\n[8] Weave\n[9] DarkLight')
                choose_cheat=int(input(Fore.YELLOW + '\nВыберите число > '))
            except Exception as e:
                os.system("cls")
                input(Fore.RED + '[!] Вы ввели недопустимое значение, попробовать еще раз? ')
                os.system("cls")
            else:
                if choose_cheat==1:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Загружаю функцию...')
                        r_drawothermodels_2()
                    except Exception:
                        print(Fore.RED + '\n[!] Не удалось найти процесс csgo.exe')
                        jpower.msgbox_error('Ошибка', 'Процесс csgo.exe не найден!')
                    else:
                        print(Fore.GREEN + 'Функцию успешно загружена!')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==2:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Загружаю функцию...')
                        showmoney()
                    except Exception:
                        print(Fore.RED + '\n[!] Не удалось найти процесс csgo.exe')
                        jpower.msgbox_error('Ошибка', 'Процесс csgo.exe не найден!')
                    else:
                        print(Fore.GREEN + 'Функция успешно загружена!')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==3:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Скачиваю Osiris...')
                        url='https://b0b9a68a-874d-42d8-b11a-ec03c27eb1e5.filesusr.com/archives/68390e_996f980e4c2e4ee4ad0af46823926aef.rar?dn=Osiris.rar'
                        urllib.request.urlretrieve(url, 'C:\Jesewe Tools\Osiris.rar')
                    except Exception:
                        print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + 'Загрузка успешно завершена!')
                        print(Fore.CYAN + '\nОткрываю папку с файлом...')
                        os.system('start "" "C:\Jesewe Tools"')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==4:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Скачиваю OneTap V3 Crack...')
                        url='https://b0b9a68a-874d-42d8-b11a-ec03c27eb1e5.filesusr.com/archives/68390e_d4bac57e501c4b19b921195f17147c62.zip?dn=OneTap%20V3%20by%20Jesewe.zip'
                        urllib.request.urlretrieve(url, 'C:\Jesewe Tools\OneTap V3 by Jesewe.zip')
                    except Exception:
                        print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + 'Загрузка успешно завершена!')
                        print(Fore.CYAN + '\nОткрываю папку с файлом...')
                        os.system('start "" "C:\Jesewe Tools"')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==5:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Скачиваю Aurora...')
                        url='https://b0b9a68a-874d-42d8-b11a-ec03c27eb1e5.filesusr.com/archives/68390e_97028a89455c4fd78e483b1f736a83c0.zip?dn=Aurora.zip'
                        urllib.request.urlretrieve(url, 'C:\Jesewe Tools\Aurora.zip')
                    except Exception:
                        print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + 'Загрузка успешно завершена!')
                        print(Fore.CYAN + '\nОткрываю папку с файлом...')
                        os.system('start "" "C:\Jesewe Tools"')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==6:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Скачиваю Victoria...')
                        url='https://b0b9a68a-874d-42d8-b11a-ec03c27eb1e5.filesusr.com/archives/68390e_20a45e827b5847b59d5c06e7a59b1587.zip?dn=Victoria.zip'
                        urllib.request.urlretrieve(url, 'C:\Jesewe Tools\Victoria.zip')
                    except Exception:
                        print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + 'Загрузка успешно завершена!')
                        print(Fore.CYAN + '\nОткрываю папку с файлом...')
                        os.system('start "" "C:\Jesewe Tools"')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==7:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Скачиваю ThrillTrip...')
                        url='https://68390ef0-2b5a-4998-8629-585776492d8f.usrfiles.com/archives/68390e_f8f70a9b82b64253ad478348ab44e30b.zip'
                        urllib.request.urlretrieve(url, 'C:\Jesewe Tools\ThrillTrip.zip')
                    except Exception:
                        print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + 'Загрузка успешно завершена!')
                        print(Fore.CYAN + '\nОткрываю папку с файлом...')
                        os.system('start "" "C:\Jesewe Tools"')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==8:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Скачиваю Weave...')
                        url='https://68390ef0-2b5a-4998-8629-585776492d8f.usrfiles.com/archives/68390e_8911cec6d608488ebfec7a8a61335b43.zip'
                        urllib.request.urlretrieve(url, 'C:\Jesewe Tools\Weave.zip')
                    except Exception:
                        print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + 'Загрузка успешно завершена!')
                        print(Fore.CYAN + '\nОткрываю папку с файлом...')
                        os.system('start "" "C:\Jesewe Tools"')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==9:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Скачиваю DarkLight...')
                        url='https://68390ef0-2b5a-4998-8629-585776492d8f.usrfiles.com/archives/68390e_5ca7b3fd937d49a7b582e3779c076427.zip'
                        urllib.request.urlretrieve(url, 'C:\Jesewe Tools\DarkLight.zip')
                    except Exception:
                        print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + 'Загрузка успешно завершена!')
                        print(Fore.CYAN + '\nОткрываю папку с файлом...')
                        os.system('start "" "C:\Jesewe Tools"')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        elif choose==2:
            try:
                os.system("cls")
                print(Fore.YELLOW + 'Minecraft - Cheat Loader')
                print(Fore.CYAN + '\n[1] Aristois Client\n[2] Impact Client\n[3] Xray Ultimate\n[4] Flux B13 1.8.8\n[5] LiquidBounce Client')
                choose_cheat=int(input(Fore.YELLOW + '\nВыберите число > '))
            except Exception as e:
                os.system("cls")
                input(Fore.RED + '[!] Вы ввели недопустимое значение, попробовать еще раз? ')
                os.system("cls")
            else:
                if choose_cheat==1:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Скачиваю Aristois Client...')
                        url='https://68390ef0-2b5a-4998-8629-585776492d8f.usrfiles.com/archives/68390e_d81cfa9b47c247e2a03dc59f55bad907.jar'
                        urllib.request.urlretrieve(url, 'C:\Jesewe Tools\Aristois-Free.jar')
                    except Exception:
                        print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + 'Загрузка успешно завершена!')
                        print(Fore.CYAN + '\nОткрываю папку с файлом...')
                        os.system('start "" "C:\Jesewe Tools"')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==2:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Скачиваю Impact Client...')
                        url='https://impactclient.net/ImpactInstaller.jar'
                        urllib.request.urlretrieve(url, 'C:\Jesewe Tools\ImpactInstaller-0.9.5.jar')
                    except Exception:
                        print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + 'Загрузка успешно завершена!')
                        print(Fore.CYAN + '\nОткрываю папку с файлом...')
                        os.system('start "" "C:\Jesewe Tools"')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==3:
                    try:
                        os.system("cls")
                        jpower.url_open('https://minecraft-inside.ru/resource-packs/32958-xray-ultimate.html')
                    except Exception:
                        print(Fore.RED + '[!] Не удалось открыть приложение, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + "Приложение успешно открыто!")
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==4:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Скачиваю Flux B13...')
                        url='https://minecraftcheats.ru/wp-content/uploads/2017/11/Flux-b13.zip'
                        urllib.request.urlretrieve(url, 'C:\Jesewe Tools\Flux-b13.jar')
                    except Exception:
                        print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + 'Загрузка успешно завершена!')
                        print(Fore.CYAN + '\nОткрываю папку с файлом...')
                        os.system('start "" "C:\Jesewe Tools"')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==5:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Скачиваю LiquidBounce Launcher...')
                        url='https://downloader.disk.yandex.ru/disk/69458fb5bb2d32cce28a7874bab6ed3182e6f701bcbb85dd0beddfd6873ac335/626e5d57/7vnf--D75glR8PqBr9gpBSHbJ8PMIyXtBrAq6uEnwj01Kksy1iSbk61GqeHzQzHzri7ArMaquHdpPgRxFbnHNQ%3D%3D?uid=0&filename=LiquidLauncher-1.1.3%20Setup.exe&disposition=attachment&hash=yl5ZSONh5nvZRbQZlS7zhf97xWT3%2BGqj9W5rMd76zR4PBzf6T5kxqorURR%2BHB2GTq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&content_type=application%2Fx-dosexec&owner_uid=895810910&fsize=56280198&hid=c5f710eb0f03e66c3881600a59635a26&media_type=executable&tknv=v2'
                        urllib.request.urlretrieve(url, 'C:\Jesewe Tools\LiquidLauncher-1.1.3 Setup.exe')
                    except Exception:
                        print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + 'Загрузка успешно завершена!')
                        print(Fore.CYAN + '\nОткрываю папку с файлом...')
                        os.system('start "" "C:\Jesewe Tools"')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        elif choose==3:
            try:
                os.system("cls")
                print(Fore.CYAN + 'Скачиваю VAC-Bypass-Loader...')
                url='https://68390ef0-2b5a-4998-8629-585776492d8f.usrfiles.com/archives/68390e_20dcb76c99954e7ca3f0004cd6a3c74e.zip'
                urllib.request.urlretrieve(url, 'C:\Jesewe Tools\VAC-Bypass-Loader.zip')
            except Exception:
                print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже!')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
            else:
                print(Fore.GREEN + 'Загрузка успешно завершена!')
                print(Fore.CYAN + '\nОткрываю папку с файлом...')
                os.system('start "" "C:\Jesewe Tools"')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        elif choose==4:
            try:
                os.system("cls")
                print(Fore.CYAN + 'Скачиваю EZInjector Reborn...')
                url='https://68390ef0-2b5a-4998-8629-585776492d8f.usrfiles.com/archives/68390e_8b5e7d5dbe12466da0c43d1dba98c0fc.zip'
                urllib.request.urlretrieve(url, 'C:\Jesewe Tools\Injector.zip')
            except Exception:
                print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже...')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
            else:
                print(Fore.GREEN + 'Загрузка успешно завершена!')
                print(Fore.CYAN + '\nОткрываю папку с файлом...')
                os.system('start "" "C:\Jesewe Tools"')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        elif choose==5:
            try:
                os.system("cls")
                print(gpu_info())
            except Exception:
                print(Fore.RED + '[!] Не удалось собрать инфоормацию, повторите попытку позже.')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
            else:
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        else:
            os.system("cls")
            input(Fore.RED + '\n[!] Вы ввели недопустимое значение, попробовать еще раз? ')
            os.system("cls")
