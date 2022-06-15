# -*- coding: utf-8 -*-
def årgang():
    aar=input('Angi årgang for filene:' )
    aar_1t = str(int(aar) - 1)
    aar_t1 = str(int(aar) + 1)
    return(print("Du lager nå filer for " + aar))

def kontroll_merge(tabell1, tabell2):
    return(tabell1.merge(tabell2,indicator = True, how='left').loc[lambda x : x['_merge']!='both'])

def createhierarchy():
    import requests
    import io
    start_aar_kommuneliste=input('Hvilket år skal kommunelisten gjelde for?:' )
    slutt_aar_kommuneliste= str(int(start_aar_kommuneliste) + 1)

    url_komm = "http://data.ssb.no/api/klass/v1/classifications/231/codes?from=" + start_aar_kommuneliste + "-01-01&to=" + slutt_aar_kommuneliste + "-01-01&csvSeparator=;"
    headers = {'content-type': 'text/csv', 'charset' : 'ISO-8859-1'}
    response = requests.get(url_komm, headers=headers).content
    kommuner = pd.read_csv(io.StringIO(response.decode('ISO-8859-1')), sep = ';')
    kommuner = kommuner[['code']]
    kommuner.rename(columns={'code':'region'}, inplace = True)
    kommuner = kommuner[~kommuner.region.str.contains("E")]
    
    kommuner = kommuner[(kommuner['region']!= '2111')]
    EAKUO = kommuner[(kommuner['region']!= '0301')].copy()
    EAKUO['to'] = 'EAKUO'
    EAK = kommuner.copy()
    EAK['to'] = 'EAK'
    EKA = kommuner.copy()
    EKA['to'] = 'EKA' + EKA['region'].str[0:2]
    
    url_ekg = "http://data.ssb.no/api/klass/v1/classifications/112/corresponds?targetClassificationId=131&from=" + start_aar_kommuneliste + "-01-01&to=" + slutt_aar_kommuneliste + "-01-01"
    headers = {'content-type': 'text/csv', 'charset' : 'ISO-8859-1'}
    response = requests.get(url_ekg, headers=headers).content
    EKG = pd.read_csv(io.StringIO(response.decode('ISO-8859-1')), sep = ',')
    EKG = EKG[['sourceCode', 'targetCode']]
    EKG.rename(columns={'sourceCode':'to', 'targetCode':'region'}, inplace = True)
    EKG = EKG.astype({'region':str})
    EKG['region']=EKG['region'].apply(lambda x: '{0:0>4}'.format(x))
    
    kommunehierarki = pd.concat([EAKUO, EAK, EKA, EKG]).drop_duplicates()
    kommunehierarki['sign'] = '+'
    kommunehierarki.rename(columns={'region':'from'}, inplace = True)
    kommunehierarki['periode'] = start_aar_kommuneliste
    kommunehierarki.to_parquet("kommunehierarki" + start_aar_kommuneliste + ".parquet")
    print('\n kommunehierarki skrevet ut i .parquet til samme mappe som din notebook ligger i.')
    return(kommunehierarki)

def hierarchy(tabell, hierarki):
    hierarki = hierarki.rename(columns={'from':'region'})
    merge = pd.merge(tabell, hierarki, on = ['region','periode'])
    #col = input('Hvilke variabler skal du gruppere langs:')
    agg = merge.groupby(['to','periode','kontoklasse','funksjon','art','regnskapsomfang'])[['belop']].sum().reset_index().rename(columns={'to':'region'})
    sam = pd.concat([tabell,agg])
    return(sam)

