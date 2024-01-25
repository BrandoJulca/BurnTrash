import subprocess
import sys
import os
import shutil

print("Eliminando temporales (1)...")

# Elimina todos los archivos con extensión .tmp en C:\Windows y sus subdirectorios
for root, dirs, files in os.walk('C:\\Windows'):
    for file in files:
        if file.endswith('.tmp'):
            file_path = os.path.join(root, file)
            os.remove(file_path)
# Imprimir un mensaje en la consola de Visual Studio Code

print("Eliminando temporales (2)...")
# Elimina el contenido de la carpeta C:\Users\%username%\AppData\Local\Temp
temp_user_path = os.path.join('C:\\Users', os.getenv('username'), 'AppData', 'Local', 'Temp')
shutil.rmtree(temp_user_path, ignore_errors=True)

print("Eliminando temporales (3)...")
# Elimina el contenido de la carpeta c:\Windows\Temp
temp_windows_path = 'C:\\Windows\\Temp'
shutil.rmtree(temp_windows_path, ignore_errors=True)
print("Temporales Eliminados exitosamente")

print("Vaciando caché...")
# Ejecutar el comando ipconfig /flushdns
try:
    subprocess.run(['ipconfig', '/flushdns'], check=True, text=True)
    print("Caché vaciado exitosamente")
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar el comando: {e}")
    sys.exit()

print("¡Ordenador limpio! | De nada, </BranDev>.")
input("Presiona Enter para salir...")

#python -m PyInstaller --onefile --icon="BURNTRASH.ico" BurnTrash.py