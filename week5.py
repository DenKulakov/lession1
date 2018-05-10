def get_vat(payment, percent=18):
	try:
		payment = float(payment)
		vat = payment / 100 * 18
		vat = round(vat, 2)
		return 'Сумма НДС: {}%'.format(vat)
	except (TypeError, ValueError):
		return 'Не могу посчитать, проверьте вводимые данные.'

resutl = get_vat()
print(resutl)
