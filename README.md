NAVODILA ZA UPORABO
# Meme_maker
Projektna naloga pri predmetu UVP - spletna aplikacija za delanje slik s (poljubno postavljenim) besedilom.

## O programu

### Opis


Spletna aplikacija za delanje memov, ki podpira delo z več uporabniki in beleži njihove meme.

Program je razdeljen na model in spletni vmesnik. Model (save_memes.py) vsebuje samo en razred: razred Memes poskrbi za potrebne mehanizme za
MEME_maker; to so na primer atributi, ki so besedilo, x in y koordinati, ter te atribute 
po potrebi shrani ali pa prebere iz posamezne .json datoteke uporabnika. In ustrezne metode, kot npr add_meme. 

Na začetku spletni vmesnik od uporabnika zahteva prijavo s funkcijo nastavi_ime(), ki sprejme uporabnikov piškotek. Spletni vmesnik vsako spremembo stanja shrani
v uporabnikovo .json datoteko, pri tem pa uporablja funkcije, definirane v modelu.

### Orodja

Projekt je bil zgrajen z ogrodjem:
* [Bottle](https://bottlepy.org/docs/dev/)

## Navodila za uporabo

### Pogoji

Za zagon programa na računalniku je potrebno imeti nameščen Python.
Za dobro uporabniško izkusnjo ne potrebujes nicesar drugega

### Namestitev in zagon

Repozitorij naložite na računalnik in ga odprite z ukazno vrstico. Nato zaženite spletni vmesnik z ukazom 
```
python -i spletni_vmesnik.py
```
in sledite povezavi.

### Delanje mema

Na strani se registrirajte (POZOR: uporabniško ime in geslo ne smeta vsebovati šumnikov ali drugih posebnih črk, temveč zgolj ASCII znake)
oz. prijavite. Stran vas bo nato preusmerila ne izbiro slike, z že privzeto sliko test.jpg ali vašo zadnjo obravnavano sliko.

* Nastavitev mema: za nastavitev novega mema morate prilepiti ustrezen url slike(za eno sliko lahko ustvarite samo en meme).
    * to vas pripelje na urejevalnik, vanj samo vpišete besedilo, x in y in kliknete koncano, kar vam bo shranilo meme
* Vsi memsi: to stran dostopate s klikom na 'seznam vseh memov' v navigacijski vrstici. Na tej strani se nahaja besedilo vseh vaših memov urejenih po času s zadnjim shranjenim na 1. mestu.
Nazaj na urejevalnik memov dostopate s klikom na ime slike ki vam bo vrnila v urejevalnik tudi izbrani meme.

## Avtor
 
[Jan Kamnikar](https://github.com/JanKamnikar)

## Licenca

Ta projekt je pod MIT licenco - za vec podrobnosti glej datoteko LICENSE.md.