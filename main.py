from util.getUpdate import *
from util.getSecrets import *
from util.getFunctions import *
from util.getTiktokShare import *

import jpower
import os
import time
import ctypes
import pymem, re
import colorama
import urllib.request
from colorama import Fore, Back, Style

init(convert=True)
jpower.window_title('Jesewe Tools 1.2')

if not os.path.isdir("C:\Jesewe Tools"):
     os.mkdir("C:\Jesewe Tools")

print(Fore.YELLOW + 'Проверка обновлений...')
check_version()

while True:
    os.system("cls")
    print(Fore.YELLOW + 'Jesewe Tools')
    print(Fore.CYAN + '\n[1] Читы для CS:GO\n[2] Steam VAC Bypass Loader\n[3] EZInjector Reborn\n[4] CS:GO Demos Manager\n[5] Информация о видеокарте\n[6] TikTok ShareBot')
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
                print(Fore.YELLOW + 'Cheat Loader')
                print(Fore.CYAN + '\n[1] Функция WallHack\n[2] Функция ShowMoney\n[3] Osiris\n[4] OneTap V3 Crack\n[5] Aurora\n[6] Victoria\n[7] ThrillTrip\n[8] Weave')
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
                        print(Fore.GREEN + '\nФункцию успешно загружена!')
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
                        print(Fore.GREEN + '\nФункция успешно загружена!')
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
                        print(Fore.GREEN + '\nЗагрузка успешно завершена!')
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
                        print(Fore.GREEN + '\nЗагрузка успешно завершена!')
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
                        print(Fore.GREEN + '\nЗагрузка успешно завершена!')
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
                        print(Fore.GREEN + '\nЗагрузка успешно завершена!')
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
                        print(Fore.GREEN + '\nЗагрузка успешно завершена!')
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
                        print(Fore.GREEN + '\nЗагрузка успешно завершена!')
                        print(Fore.CYAN + '\nОткрываю папку с файлом...')
                        os.system('start "" "C:\Jesewe Tools"')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        elif choose==2:
            try:
                os.system("cls")
                print(Fore.CYAN + 'Скачиваю VAC-Bypass-Loader...')
                url='https://68390ef0-2b5a-4998-8629-585776492d8f.usrfiles.com/archives/68390e_20dcb76c99954e7ca3f0004cd6a3c74e.zip'
                urllib.request.urlretrieve(url, 'C:\Jesewe Tools\VAC-Bypass-Loader.zip')
            except Exception:
                print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже!')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
            else:
                print(Fore.GREEN + '\nФайл успешно скачался!')
                print(Fore.CYAN + '\nОткрываю папку с файлом...')
                os.system('start "" "C:\Jesewe Tools"')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        elif choose==3:
            try:
                os.system("cls")
                print(Fore.CYAN + 'Скачиваю EZInjector...')
                url='https://68390ef0-2b5a-4998-8629-585776492d8f.usrfiles.com/archives/68390e_8b5e7d5dbe12466da0c43d1dba98c0fc.zip'
                urllib.request.urlretrieve(url, 'C:\Jesewe Tools\Injector.zip')
            except Exception:
                print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже...')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
            else:
                print(Fore.GREEN + '\nФайл успешно скачался!')
                print(Fore.CYAN + '\nОткрываю папку с файлом...')
                os.system('start "" "C:\Jesewe Tools"')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        elif choose==4:
            try:
                os.system("cls")
                print(Fore.CYAN + 'Скачиваю CS:GO-Demos-Manager...')
                url='https://github.com/akiver/CSGO-Demos-Manager/releases/download/v2.13.15/csgo-demos-manager-2.13.15.exe'
                urllib.request.urlretrieve(url, 'C:\Jesewe Tools\csgo-demos-manager-2.13.15.exe')
            except Exception:
                print(Fore.RED + '[!] Не удалось скачать файл, повторите попытку позже...')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
            else:
                print(Fore.GREEN + '\nСсылка успешно открыта!')
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
                print(Fore.GREEN + '\nИнформация успешно собрана!')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        elif choose==6:
            try:
                os.system("cls")
                print(Fore.RED + '[!] Предупреждение, программа будет нагружать ПК!')
                time.sleep(2)
                print(Fore.RED + '[!] Накрутка работает бесконечно, пока будет работать программа.')
                time.sleep(4)
                obj = tiktok()
                obj.main()
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
            except Exception:
                print(Fore.RED + '[!] Неизвестная ошибка!')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        elif choose==666:
            os.system("cls")
            number_666()
            input(Fore.YELLOW + '\n\nДля продолжения нажмите Enter > ')
        elif choose==404:
            os.system("cls")
            number_404()
            input(Fore.YELLOW + '\n\nДля продолжения нажмите Enter > ')
        elif choose==999:
            os.system("cls")
            number_999()
            input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        elif choose==1007:
            os.system("cls")
            dead_inside()
            input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        else:
            os.system("cls")
            input(Fore.RED + '\n[!] Вы ввели недопустимое значение, попробовать еще раз? ')
            os.system("cls")
