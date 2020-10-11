def met_mg(Y, Al, Mt, t, X, ca, mg):
	
	CA = ((float(Y)) * (float(Al)) - ((float(Mt) * float(t))/100))

	CD = ((float(X)) - ((float(ca)) + (float(mg))))

	#Se o valor de CA ou CD for menor que 0, seus valores devem ser
	#considerados igual a 0 para a continuação dos cálculos.

	if CA < 0:
		CA = 0
	if CD < 0:
		CD = 0 

	NC = (float(CA) + float(CD))

	NC = format(NC, '.1f')

	return NC
