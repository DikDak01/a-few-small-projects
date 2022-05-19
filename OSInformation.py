import platform
import os

print("Stützräderprotokoll")
print("Author: Nik Nak")

print(60 * "-")
print('\033[35m', os.name)

print(60 * "-")
print(platform.system())
print(platform.release())
print(platform.platform())

print(60 * "-")
print(platform.version())
print(platform.machine())
print(platform.architecture())

print(60 * "-")
print(platform.processor())
print(platform.python_branch())
print(platform.python_version())

print(60 * "-")
print(platform.uname())
print(60 * "-")
