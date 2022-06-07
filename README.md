# Kommuneregnskapet

Table of Contents
=================

* [Omkoding av regnskapet](#omkoding-av-regnskapet)
  * [Bevilgnings- og balanseregnskapet](#bevilgnings--og-balanseregnskapet)
  * [Publiseringsløpet](#publiseringsløpet)

## Omkoding av regnskapet

Denne branshen inneholder regnskapsflyten omkodet til python. 

### Bevilgnings- og balanseregnskapet

  - Disse mappene inneholder flyten for bevilgning og balanse hver for seg. 
  1. Henting av nødvenig data fra Klass
  2. Henting av nødvendig data fra Oracle
  3. Kjøring av regnskapene for kasse, konsolidert og særbedrifter
  4. Sammenslåing av regnskapene, utregning av begrep og regionsaggregering via Kostra-Pakken
  5. Balanseflyten inneholder i tillegg selvkostregnskapet

  - *Foreløpige feil og mangler:*
  - Inputfiler som foreløpig ikke er kodet i python, men som lastes inn via csv:
  1. Hierarkifilene som benyttes inn i KostraRegnskaps-funksjonen
  2. Rentekomp
  3. Særbedriftspopulasjonen
  - Filene ligger : /ssb/stamme03/komakro/pilot_python/*
  - Program for å lese filene til overnevnte sti ligger under Kommuneregnskapet->Regnskapsflyten->2021->Bevilgningsregnskapet->1.Hierarkifilene

### Publiseringsløpet

  - Denne mappen skal inneholde publiseringstabellene. 
  - Per notebook ligger hele løpet fra KostraRegnskaps-funksjonene til ferdige publiseringstabeller
    1. Finansielle tabeller inneholder finansielle grunnlagstall og finansielle nøkkeltall for alle regnskapsomfang
    2. Økonomiske oversikter inneholder alle Øk.ov-tabeller for alle regnskapsomfang
  - *Ønsker for fremtiden:*
    - Per publiseringtabell skal det lages en egen notebook med interaktiv tabell. Denne boken skal hentes inn i notebooken der tabellene produkseres og kan kjøres etter ønske. Forhåpentligvis ved å trykke på en knapp. 
