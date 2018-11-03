# Dokumentace k úkolu č.1
Tento program slouží k výpočtu mapových souřadnic průsečíků rovnoběžek a poledníků pomocí úživatelem zvoleného zobrazení. 

Kromě samotného výpočtu program vykreslí výslednou souřadnicovou síť a zakreslí do ní body, které uživatel zadá.

## Vstupy
- zvolené zobrazení
  - L = Lambertovo, B = Braunovo, A = Marinovo, M = Mercatorovo
- poloměr Země
  - volitelný
  - pokud uživatel zadá 0, poloměr je nastaven na 6371,11 km
- měřítko
  - volitelné
  - vždy celočíselné větší než 0
  - např. 50000000 pro měřítko 1 : 50 000 000
- zěměpisná šířka a délka bodů ve stupních

## Výstupy
1) tisk mapových souřadnic průsečíků rovnoběžek a poledníků po 10°, vypočtených podle zvoleného zobrazení, měřítka a poloměru Země
    - seznam vzdáleností na ose X - pro zakreslení poledníků
    - seznam vzdálenostá na ose Y - pro zakreslení rovnoběžek
    - pokud vzdálenost přesáhne hodnotu 1 m, je vypsána "-"
2) tisk mapových souřadnic zadaných bodů
    - pokud vzdálenost přesáhne hodnotu 1 m, je vypsána "-"
3) vykreslení souřadnicové síťě
    - jsou vykresleny jen ty vypočtené rovnoběžky a poledníky, které jsou blíže než 1 m od počátku
4) vykreslení zadaných bodů do souřadnicové sítě
    - jsou vykresleny jen ty vypočtené body, které jsou blíže než 1 m od počátku

## Popis programu
Pro zvýšení přehlednosti programu a snížení opakování shodných částí, je většina výpočtu definována uvnitř funkcí.

K výpočtu jednotlivých zobrazení bylo nutné naimportovat modul Math a pro vykreslní souřadnicové sítě a bodů modul Turtle.

### Popis funkcí
1) Funkce pro přepočet zeměpisné šířky a délky na mapové souřadnice
    - do této sekce lze zařadit prvních 8 funkcí, které představují transformační rovnice pro jednotlivá zobrazení
    - funkce jsou psány vždy zvlášť pro x a y
    - tyto funkce vrací hodnoty mapových souřadnic zaokrouhlených na jedno desetinné místo
2) Funkce pro tvorbu a tisk polí, obsahující hodnoty průsečíků rovnoběžek a průsečíků v mapových souřadnicích
    - v rámci těchto funkcí jsou dosazovány hodnoty zeměpisné šířky a zeměpisné délky do předchozích funkcí
    - v případě, že hodnota vzdálenosti na ose x či y nepřesáhne 1 m, je přidána do pole
    - následně jsou vytisknuty vzdálenosti na ose x a ose y, v případě že přesáhnou 1 m, jsou vypsány jako "-"
    - v rámci této funkce bylo nutné ošetřit chybu vznikající při výpočtu vzdálenosti polů v Mercatorově projekci, které se promítají do nekonečna
    - obě funkce vrací pole vzdáleností na ose x a y, pro další využití v rámci kreslení souřadnicové sítě
3) Funkce pro ověření vstupu uživatele
    - následující dvě funkce ověřují, zda je uživatelův vstup datový typ float nebo integer
    - pokud nejsou tyto podmínky splněné, je po uživatelých požadován nový vstup
    - v případě splnění těchto podmínek, je daný vstup vrácen těmito funkcemi
4) Funkce pro výpočet mapových souřadnic zadaných bodů
    - tato funce má za úkol vypočíst a vytisknout mapové souřadnice bodů zadaných uživatelem
    - během této funkce jsou volány již popsané funkce pro transformaci zeměpisné šířky a délky do mapových souřadnic
    - v rámci této funkce bylo nutné ošetřit několik podmínek
      - zěmepisná šířka musí být z intervalu <-90;90>
      - zeměpisná délka musí být i intervalu <-180;180>
      - znovu bylo nutné ošetetřit výpočet vzdálenosti pólů v případě Mercatorova zobrazení
    - v případě, že vypočetné vzdálenosti přesáhnout opět 1 m, jsou místo nich vypsány "-"
    - funkce požaduje po uživateli další souřadnice bodů, dokud nezadá souřadnice [0,0]
    - tato funkce též vrací pole polí, v nichž jsou zaneseny mapové souřadnice bodů, zadaných uživatelem, pro následné vykreslení
 5) Funkce pro vykreslení souřadnicové sítě a zadaných bodů
    - v rámci této funkce je pomocí modelu Turtle vykreslena souřadnicová síť
    - pro vykreslení sítě jsou využity pole vrácená funkcemi pro výpočet zeměpisné délky a šířky
    - z toho plyne, že jsou vykresleny pouze rovnoběžky a poledníky, jejich vzdálenost nepřesahuje 1 m od počátku
    - následně jsou do souřadnicové sítě zakresleny body zadané uživatelem, ovšem pouze ty, jejich vzdálenost od osy x a y nepřesahuje 1 m
    


V následující části programu jsou do proměných ukládány uživatelovy vstupy a volány postupně všechny výše popsané funkce
 
      
