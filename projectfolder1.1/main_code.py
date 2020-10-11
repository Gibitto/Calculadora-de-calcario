from metodo_sp import met_sp 
from metodo_mg import met_mg
from quantidade_calcario import quant_calc
from definidor_calcario import def_calc
from calculadora_de_Y_prem import y_prem
from calculadora_de_Y_arg import y_arg

opt = input("Digite '1' se você quiser usar o método de sp e '2' para o método de mg ")
if opt == '1':
	
	#variáveis de met_sp
	T = input("\nInsira o valor da CTC potencial(T): ")
	Ve = input("Insira o valor da saturação por bases esperada(Ve): ")
	SB = input("Insira o valor da soma de bases(SB): ")
	#variáveis de quant_calc
	SC = input("\nInforme a porcentagem da superfície do terreno a ser coberta na calagem: ")
	PF = input("Informe até que profundidade o calcário será incorporado(em cm): ")
	PRNT = input("Informe o PRNT do calcário a ser utilizado(em %): ")
	NC = float(met_sp(T, Ve, SB))
	#variável de def_calc
	mg = input("\nInforme o valor de Mg: ")
	
	print('\nA necessidade de calcário(NC) é igual a: ' + str(met_sp(T, Ve, SB)) + ' toneladas por ha')

	print('\nA quantidade de calcário(QC) é igual a: ' + str(quant_calc(SC, PF, PRNT, NC)) + ' toneladas por ha')

	def_calc(mg, T)
	
elif opt == '2':
	#variáveis de Y
	opt_y = input("Se você quiser calcular o y pelo p-rem digite '1', pela argila digite '2'")

	if opt_y == '1':
		p_rem = input("Insira o valor de P-Rem: ")
		print(str(y_prem(p_rem)))
		global Y1
		Y1 = y_prem(p_rem)
		
		
	elif opt_y == '2':
		arg = input("Insira o valor da Argila em (%): ")
		print(str(y_arg(arg)))
		Y1 = y_arg(arg)
		
	#variáveis de met_mg
	Y = Y1
	Al = input("Insira o valor de Al^3+: ")
	Mt = input("Insira o valor de Mt: ")
	t = input("Insira o valor de t: ")
	X = input("Insira o valor de X: ")
	ca = input("Insira o valor de Ca^2+: ")
	mg = input("Informe o valor de Mg: ")
	NC = float(met_mg(Y, Al, Mt, t, X, ca, mg))

	#variáveis de quant_calc
	SC = input("\nInforme a porcentagem da superfície do terreno a ser coberta na calagem: ")
	PF = input("Informe até que profundidade o calcário será incorporado(em cm): ")
	PRNT = input("Informe o PRNT do calcário a ser utilizado(em %): ")
	#variável de def_calc
	T = input("\nInsira o valor da CTC potencial(T): ")

	if NC == 0 : 
		print("Não há necessidade de calagem")
	else:
		print("\nA necessidade de calcário(NC) é igual a: " + str(NC) + " toneladas por hectare" )
	
	print("A quantidade de calcário (QC) é igual a: " + str(quant_calc(SC, PF, PRNT, NC)) + " toneladas por hectare")
	
	def_calc(mg, T)

