import subprocess
import importlib
import sys

pip_libraries = ["smbus2", "RPi.GPIO", "atcom"]

apt_packages = ["minicom"]

def install_pip_library(library):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])
        print(f"{library} başarıyla yüklendi.")
    except subprocess.CalledProcessError:
        print(f"{library} yüklenirken bir hata oluştu.")

def install_apt_package(package):
    try:
        subprocess.check_call(["sudo", "apt", "install", "-y", package])
        print(f"{package} başarıyla yüklendi.")
    except subprocess.CalledProcessError:
        print(f"{package} yüklenirken bir hata oluştu.")

def check_library(library):
    try:
        importlib.import_module(library)
        print(f"{library} başarıyla import edildi.")
    except ImportError:
        print(f"{library} import edilemedi. Yükleme başarısız.")

for library in pip_libraries:
    install_pip_library(library)

for package in apt_packages:
    install_apt_package(package)

for library in pip_libraries:
    check_library(library)
