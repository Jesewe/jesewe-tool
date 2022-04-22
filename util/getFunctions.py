import pymem, re
import GPUtil
from tabulate import tabulate

def r_drawothermodels_2():
    pm = pymem.Pymem('csgo.exe')
    client = pymem.process.module_from_name(pm.process_handle,'client.dll')
    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F',clientModule).start() + 2
    pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)
    pm.close_process()

def showmoney():
    pm = pymem.Pymem('csgo.exe')
    client = pymem.process.module_from_name(pm.process_handle,'client.dll')
    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF',clientModule).start()
    pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)
    pm.close_process()

def gpu_info():
    gpus = GPUtil.getGPUs()
    gpus_list = []

    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f'{gpu.load*100}%'
        gpu_free_memory = f'{gpu.memoryFree}MB'
        gpu_used_memory = f'{gpu.memoryUsed}MB'
        gpu_total_memoru = f'{gpu.memoryTotal}MB'
        gpu_temp = f'{gpu.temperature}'

        gpus_list.append((
            gpu_id,
            gpu_name,
            gpu_load,
            gpu_free_memory,
            gpu_used_memory,
            gpu_total_memoru,
            gpu_temp
        ))
    return str(tabulate(
            gpus_list,
            headers=(
                'ID',
                'Название',
                'Нагрузка',
                'Свободная память',
                'Используемая память',
                'Общая память',
                'Температура'
            ),
            tablefmt='pretty'
        )
    )
