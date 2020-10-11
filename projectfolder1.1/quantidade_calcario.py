def quant_calc(SC, PF, PRNT, NC):

	#Fórmula para corrigir o valor da necessidade de calcário(NC), 
	#de acordo com a superfície do solo a ser coberta, a profundidade
	#que o corretivo será incorporado e o Poder reativo de 
	#neutralização total do calcário a ser utilizado.
	
	QC = (float(NC)) * ((float(SC))/100) * ((float(PF))/20) * (100/(float(PRNT)))

	QC = format(QC, '.1f')
	
	return QC

