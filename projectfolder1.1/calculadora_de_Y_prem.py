def y_prem(p_rem):
	
		#Fórmula para o cálculo de Y através do valor do fósforo 
		#remanescente(P-Rem)
	
	Y = ((4.002) - (0.125901) * (float(p_rem)) + (0.001205) * (float((p_rem))**2) - (0.00000362) * ((float(p_rem))**3))

	Y = format(Y, '.4f')	

	return Y

