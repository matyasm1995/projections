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

## Výstup
1) tisk mapových souřadnic průsečíků rovnoběžek a poledníků po 10°, vypočtených podle zvoleného zobrazení, měřítka a poloměru Země
  a) seznam vzdáleností na ose X - pro zakreslení poledníků
  b) seznam vzdálenostá na ose Y - pro zakreslení rovnoběžek
  - pokud vzdálenost přesáhne hodnotu 1 m, je vypsána "-"
2) tisk mapových souřadnic zadaných bodů
  - pokud vzdálenost přesáhne hodnotu 1 m, je vypsána "-"
3) vykreslení souřadnicové síťě
  - jsou vykresleny jen ty vypočtené rovnoběžky a poledníky, které jsou blíže než 1 m od počátku
4) vykreslení zadaných bodů do souřadnicové sítě
  - jsou vykresleny jen ty vypočtené body, které jsou blíže než 1 m od počátku
