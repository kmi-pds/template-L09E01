# L09E01 - Chord system

Dnešním úkolem je implementovat zjednodušenou verzi Chord systému z přednášky. Před spuštěním sítě nastavíme počet uzlů (například 8). Pomoci knihovny `distsim` vytvoříme instanci třídy `Network` se stejným počtem uzlů, kde každý uzel obsahuje `Link` do všech ostatních uzlů. Dále vytvoříme jeden uzel, který nebude součástí Chord systému (můžeme mu říkat klient).

Následně síť spustíme, každý uzel v chord systému vypočítá odpovídající "finger table", pomoci které bude probíhat směrování. Následně klient opakovaně kontaktujte libovolný uzel v chord systému s požadavkem doručení zprávy jinému náhodnému uzlu z Chord systému.

V Chord systému neřešíme přidávání a odebírání uzlů. Systém od začátku disponuje maximálním počtem uzlů.