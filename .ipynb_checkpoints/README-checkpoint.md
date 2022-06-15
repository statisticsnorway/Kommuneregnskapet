# Kommuneregnskapet
For samarbeid om kode på kommunegruppa.
Kun kode skal pushes, aldri data.

I jupyter, pass på å jobb i riktig branch. Velg riktig branch i i git-fanen, gå deretter ut i mappestrukturen. 
Lag ny branch for nytt prosjekt.

## Oversikt over branchene:
1. Kontroll-av-publiseringstabeller
    - Denne branchen lager kontroller for publiseringstabellene. 
2. Omkoding-regnskapet
    - Koder om regnskapsflyten som i dag er i Kompis til Python/R
    - Ikkeholder to mapper:
        1. Regnskapsflyten
            - Flytene er lagt opp i et og et ark. Hver ark må kjøres. Endetabellene lagres på linux og hentes inn igjen i neste ark. 
        2. Regnskapsflyten_v2
            - Har "automatisert" kjøringene av arbeidsflytene. 
            - Trenger kun å kjøre KostraRegnskap, BalanseRegnskap og bøkene som produserer publiseringstabellene. 
3. Kostra-Regnskap
    - Tester å lage en JupyterBook