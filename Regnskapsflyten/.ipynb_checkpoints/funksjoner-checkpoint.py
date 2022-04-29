def kontroll_merge(tabell1, tabell2):
    return(tabell1.merge(tabell2,indicator = True, how='left').loc[lambda x : x['_merge']!='both'])
