#Программа для шифрации и дешифрации текста
#Версия 1.0
#Автор deliciousNesquik
#Дата создания 05.06.2022

from cipher_moodle import cipher, uncipher
from pyfiglet import Figlet

def main():
	preview = Figlet(font="slant")
	print(preview.renderText("Cipher text"))

	while True:
		print("  Выберите операцию [шифрация - 1] [дешифрация - 2]: ", end="")
		operation = input("")

		if operation == "1":
			text = ""
			while text == "":
				text = input("\tВведите текст для шифрации: ")

			func = cipher(text)
			print(
			f"""
	Зашифрованный текст: {func[0]}
	Ключ для текста: {func[1]}
	Расшифрованный текст: {text}
			""")

			print("-" * 55)

		elif operation == "2":
			cipher_text = ""
			while cipher_text == "":
				cipher_text = input("\tВведите зашифрованный текст: ")

			key = ""
			while key == "":
				key = input("\tВведите ключ: ")

			func = uncipher(cipher_text, key)
			print(
			f"""
	Зашифрованный текст: {cipher_text}
	Ключ для текста: {key}
	Расшифрованный текст: {func}
			""")

			print("-" * 55)

		else:
			print("\t[ОШИБКА][НЕ ИЗВЕСТНАЯ КОМАНДА]")
			print("-" * 55)


if __name__ == "__main__":
	main()