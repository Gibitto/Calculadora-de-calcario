def def_calc(mg, T):
    
    #Fórmula para definir o tipo de calcário a ser utilizado,
    #calcítico ou dolomítico
    
    TC = ((float(mg) * float(T))/100)

    TC = format(TC, '.3f')

    if float(TC) >= 0.05:
        print("\nUtilize calcário calcítico")
    elif float(TC) < 0.05:
        print("\nUtilize calcário dolomítico")
    
    return TC
