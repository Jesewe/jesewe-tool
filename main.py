from util.getUpdate import *
from util.getSecrets import *
from util.getFunctions import *
import jpower
import os
import time
import ctypes
import pymem, re
import colorama
from colorama import Fore, Back, Style
from tkinter import messagebox
from pystyle import Write, Colors

jpower.window_title('Jesewe Tools 0.9')
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

print(Fore.YELLOW + 'Проверка обновлений...')
check_version()

while True:
    os.system("cls")
    print(Fore.YELLOW + 'Jesewe Tools')
    print(Fore.CYAN + '\n[1] Читы для CS:GO\n[2] Steam VAC Bypass Loader\n[3] EZInjector Reborn\n[4] Информация о видеокарте\n[5] CS:GO Demos Manager')
    try:
        choose=int(input(Fore.YELLOW + '\nВыберите число > '))
    except Exception as e:
        os.system("cls")
        input(Fore.RED + 'Вы ввели недопустимое значение, попробовать еще раз? ')
        os.system("cls")
    else:
        if choose==1:
            try:
                os.system("cls")
                print(Fore.YELLOW + 'Jesewe Tools')
                print(Fore.CYAN + '\n[1] Функция WallHack\n[2] Функция ShowMoney\n[3] Чит Osiris\n[4] Чит OneTap V3 CRACK\n[5] Чит Aurora')
                choose_cheat=int(input(Fore.YELLOW + '\nВыберите число > '))
            except Exception as e:
                os.system("cls")
                input(Fore.RED + 'Вы ввели недопустимое значение, попробовать еще раз? ')
                os.system("cls")
            else:
                if choose_cheat==1:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Загружаю функцию...')
                        r_drawothermodels_2()
                    except Exception:
                        print(Fore.RED + '\nНе удалось найти процесс csgo.exe')
                        messagebox.showerror('Ошибка', 'Процесс csgo.exe не найден!')
                    else:
                        print(Fore.GREEN + '\nФункцию успешно загружена!')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==2:
                    try:
                        os.system("cls")
                        print(Fore.CYAN + 'Загружаю функцию...')
                        showmoney()
                    except Exception:
                        print(Fore.RED + '\nНе удалось найти процесс csgo.exe')
                        messagebox.showerror('Ошибка', 'Процесс csgo.exe не найден!')
                    else:
                        print(Fore.GREEN + '\nФункция успешно загружена!')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==3:
                    try:
                        os.system("cls")
                        jpower.url_open('https://68390ef0-2b5a-4998-8629-585776492d8f.usrfiles.com/archives/68390e_996f980e4c2e4ee4ad0af46823926aef.rar')
                    except Exception:
                        print(Fore.RED + 'Не удалось скачать файл, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + 'Ссылка успешно открыта!')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==4:
                    try:
                        os.system("cls")
                        jpower.url_open('https://68390ef0-2b5a-4998-8629-585776492d8f.usrfiles.com/archives/68390e_d4bac57e501c4b19b921195f17147c62.zip')
                    except Exception:
                        print(Fore.RED + 'Не удалось открыть ссылку, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + 'Ссылка успешно открыта!')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                elif choose_cheat==5:
                    try:
                        os.system("cls")
                        jpower.url_open('https://68390ef0-2b5a-4998-8629-585776492d8f.usrfiles.com/archives/68390e_97028a89455c4fd78e483b1f736a83c0.zip')
                    except Exception:
                        print(Fore.RED + 'Не удалось открыть ссылку, повторите попытку позже...')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
                    else:
                        print(Fore.GREEN + 'Ссылка успешно открыта!')
                        input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        elif choose==2:
            try:
                os.system("cls")
                jpower.url_open('https://68390ef0-2b5a-4998-8629-585776492d8f.usrfiles.com/archives/68390e_20dcb76c99954e7ca3f0004cd6a3c74e.zip')
            except Exception:
                print(Fore.RED + 'Не удалось скачать файл, повторите попытку позже!')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
            else:
                print(Fore.GREEN + 'Ссылка успешно открыта!')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        elif choose==3:
            try:
                os.system("cls")
                jpower.url_open('https://68390ef0-2b5a-4998-8629-585776492d8f.usrfiles.com/archives/68390e_8b5e7d5dbe12466da0c43d1dba98c0fc.zip')
            except Exception:
                print(Fore.RED + 'Не удалось скачать файл, повторите попытку позже...')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
            else:
                print(Fore.GREEN + 'Ссылка успешно открыта!')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        elif choose==4:
            try:
                os.system("cls")
                print(gpu_info())
            except Exception:
                print(Fore.RED + 'Не удалось собрать инфоормацию, повторите попытку позже.')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
            else:
                print(Fore.GREEN + '\nИнформация успешно собрана!')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
        elif choose==5:
            try:
                os.system("cls")
                jpower.url_open('https://github.com/akiver/CSGO-Demos-Manager/releases/download/v2.13.15/csgo-demos-manager-2.13.15.exe')
            except Exception:
                print(Fore.RED + 'Не удалось скачать файл, повторите попытку позже...')
                input(Fore.YELLOW + '\nДля продолжения нажмите Enter > ')
            else:
                print(Fore.GREEN + 'Ссылка успешно открыта!')
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
            input(Fore.RED + '\nВы ввели недопустимое значение, попробовать еще раз? ')
            os.system("cls")