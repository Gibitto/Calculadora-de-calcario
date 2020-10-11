def y_arg(arg):
	
	#Fórmula para o cálculo de Y através do valor da Argila
	
	Y = (0.0302) + (0.06532) * (float(arg)) - (0.000257) * ((float(arg))**2)

	Y = format(Y, '.4f')

	return Y
