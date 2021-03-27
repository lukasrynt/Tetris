# Tetris
## Popis
Hra je napodobeninou slavné počítačové hry Tetris. V této hře padají dolů bloky, známé jako tetromina. Cílem hráče je uspořádat tyto bloky do zaplněných řádků, a získat tak co největší skóre. S větším počtem zaplněných řádků v jednom tahu se zvyšuje získané skóre

## Spuštění
Pro spuštění hry je potřeba:
1.  `git pull` z daného repozitáře na této [adrese](https://gitlab.fit.cvut.cz/BI-PYT/b201/ryntluka/tree/semestralka). Hra je pak ve větvi master tohoto repozitáře.
2. `conda env create --name MYENV` pro vytvoření virtuálního prostředí na svém počítači. Předpokladem je nainstalovaná conda.
3.  `conda activate MYENV` pro aktivaci virtuálního prostředí
4.  `python -m tetris` pro samotné spuštění hry

## Prostředí
Po spuštění se hráči zpřístupní hlavní menu, ve kterém má na výběr kliknutí na jedno z tlačítek:
+   `New Game` - spustí novou hru
+   `Continue Game` - dostupné pouze, pokud byla v dané session už jedna hra rozehrána; pokračuje v rozehrané hře
+   `Quit Game` - pro opuštění hry, dostupné i pomocí klávesy `Esc`

Samotná hra se pak ovládá pomocí šipek a případně klávesou `Esc` pro návrat do hlavního menu (slouží tedy, jako pauza hry).
+   `Šipka nahoru` - k rotaci současně padajícího tetromina
+   `Šipka dolu` - ke zrychlení tetromina
+   `Šipka doleva` - k posunutí tetromina doleva
+   `Šipka doprava` - k posunutí tetromina doprava

