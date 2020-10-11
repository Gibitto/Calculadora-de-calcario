#A fórmula matemática do cálculo da NC em si, pelo método de
#saturação por bases, ou método de São Paulo:

def met_sp(T, Ve, SB):
	
	NC = (((float(Ve))/100) * (float(T)) - (float(SB)))
	
	NC = format(NC, '.2f')
	
	return NC	

