import winreg
import platform
import os

def foo(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            try:
                software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
            except EnvironmentError:
                software['version'] = 'undefined'
            try:
                software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
            except EnvironmentError:
                software['publisher'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list

software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + foo(winreg.HKEY_CURRENT_USER, 0)

#for software in software_list:
#    print('Name=%s, Version=%s, Publisher=%s' % (software['name'], software['version'], software['publisher']))
#print('Number of installed apps: %s' % len(software_list))

#вывод конкретной программы
print('Windows ' + platform.release())
print('Пользователь ' + os.getlogin())
prog_name = 'ViPNet CSP'
for software in software_list:
    if software['name'] == prog_name:
        print('Name=%s Version=%s' % (software['name'], software['version']))
prog_name = 'ViPNet Client'
for software in software_list:
    if software['name'] == prog_name:
        print('Name=%s Version=%s' % (software['name'], software['version']))
prog_name = 'КриптоПро ЭЦП Browser plug-in'
for software in software_list:
    if software['name'] == prog_name:
        print('Name=%s Version=%s' % (software['name'], software['version']))
prog_publisher = 'Rostelecom'
for software in software_list:
    if software['publisher'] == prog_publisher:
        print('Name=%s Version=%s' % (software['name'], software['version']))
prog_name = 'Единый Клиент JaCarta'
for software in software_list:
    if software['name'] == prog_name:
        print('Name=%s Version=%s' % (software['name'], software['version']))
prog_name = 'Драйверы Рутокен'
for software in software_list:
    if software['name'] == prog_name:
        print('Name=%s Version=%s' % (software['name'], software['version']))
prog_name = 'JLSS'
for software in software_list:
    if software['name'] == prog_name:
        print('Name=%s Version=%s' % (software['name'], software['version']))
prog_name = 'ФСРАР-Крипто3'
for software in software_list:
    if software['name'] == prog_name:
        print('Name=%s Version=%s' % (software['name'], software['version']))
