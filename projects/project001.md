# Projekt I
*Miłe złego początki*

---

## Opis

Celem pierwszego projektu jest napisanie skryptu, który wczytuje plik(i) tekstowy i rysuje na konsoli histogram wszystkich wyrazów w pliku. Należy znaleźć tekst jakiejś książki po angielsku i po polsku (tłumaczenie) i zbadać rozkłady.

## Wymagania:
- nazwa pliku jako parametr skryptu
- wyświetlanie histogramu od najczęściej do najrzadziej występujących wyrazów
- opcjonalny parametr określający dla ilu wyrazów histogram wyświetlić (domyślnie 10)
- opcjonalny parametr określający minimalną długość histogramowanego słowa (domyślnie 0)
- *(opcjonalnie)* dodatkowy, opcjonalny parametr, przyjmujący listę wyrazów ignorowanych
- *(opcjonalnie)* dodatkowy, opcjonalny parametr, przyjmujący ciąg/ciągi znaków, których nie mogą zawierać zliczane wyrazy
- *(opcjonalnie)* dodatkowy, opcjonalny parametr, przyjmujący ciąg/ciągi znaków, które muszą zawierać zliczane wyrazy
- *(opcjonalnie)* kolorowy histogram, który mnie oczaruje
- *(opcjonalnie)* dodatkowy parametr z nazwą katalogu; program przechodzi przez wszystkie pliki tekstowe w tym katalogu, zlicza słowa i robi histogram jak wyżej
- *(opcjonalnie)* ma się wyświetlać jakiś pasek postępu

## Przydatne biblioteki:
- [ascii_graph](https://github.com/kakwa/py-ascii-graph)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [rich](https://github.com/Textualize/rich)
- [tqdm](https://github.com/tqdm/tqdm)




