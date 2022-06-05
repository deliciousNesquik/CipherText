from random import randint

def cipher(input_text: str) -> list:
	"""
	Данная функция выполняет шифрование
	текстовой информации.

	Принимает текст
	в типе данных строка ,а возвращает список,
	состоящий из зашифрованного текста и ключа
	для расшифровки текста.

	Способ шифрации текста
	осуществляется путём перевода символа в
	его цифровое значение и преобразование этого
	значения в более сложную конструкцию.

	1. преобразование символа в его цифровое значение.
	2. запись этого числа в общий список в типе данных int.
	3. преобразование числа в более сложную конструкцию путём
	   его увеличения или уменьшения.
	4. запись в ключ той операции по счёту над числом.
	5. возращение списка содержащего текст и ключ
	"""
	output_text = ""
	output_key = ""

	output_text = list(map(lambda x: int(ord(x)), input_text))

	for index in range(len(output_text)):
		operation = randint(1, 4)

		if operation == 1:
			output_text[index] += 255
			output_key += "1"

		elif operation == 2:
			output_text[index] -= 255
			output_key += "2"

		elif operation == 3:
			output_text[index] *= 255
			output_key += "3"

		elif operation == 4:
			output_text[index] /= 255
			output_key += "4"

	return [":".join(map(str, output_text)), output_key]

def uncipher(input_text: str, input_key: str) -> str:
	"""
	Данная функция выполняет дешифрование
	текстовой информации.

	Принимает зашифрованный текст
	в типе данных строка и ключ для его расшифровки в типе данных строка,
	а возвращает список, состоящий из зашифрованного текста и ключа
	для расшифровки текста.

	Способ дешифрации текста
	осуществляется путём облегчения сложной конструкции
	с помощью ключа для расшифровки текста и перевод из
	цифрового типа в символьный тип

	1. разделение строки на список
	2. облегчение цифр внутри списка с помощью ключа
	3. перевод из цифрового типа данных в символьный тип
	4. возращения расшифрованного текста
	"""

	output_text = input_text.split(":")
	output_text = list(map(float, output_text))

	for index in range(len(output_text)):
			operation = input_key[index]

			if operation == "1":
				output_text[index] -= 255

			elif operation == "2":
				output_text[index] += 255

			elif operation == "3":
				output_text[index] //= 255

			elif operation == "4":
				output_text[index] *= 255

	output_text = list(map(int, output_text))
	output_text = list(map(lambda x: str(chr(x)), output_text))

	return "".join(output_text)


if __name__ == "__main__":
	pass