### Hexlet tests and linter status:
[![Actions Status](https://github.com/Konst-Pav/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/Konst-Pav/python-project-49/actions)    [![Maintainability](https://api.codeclimate.com/v1/badges/0db0ca962bd1856f5413/maintainability)](https://codeclimate.com/github/Konst-Pav/python-project-49/maintainability)

____

### **Brain games**
5 простых математических игр
- **Brain-even** — четное или нечетное число
[![asciicast](https://asciinema.org/a/ZNEnQUXCY7oPWlsWVYh9XPHeM.svg)](https://asciinema.org/a/ZNEnQUXCY7oPWlsWVYh9XPHeM)

- **Brain-calc** — задачи на сложение, вычитание и умножение
[![asciicast](https://asciinema.org/a/9HSfIGzHDuXDva8DL7zP4ohPf.svg)](https://asciinema.org/a/9HSfIGzHDuXDva8DL7zP4ohPf)

- **Brain-gcd** — максимальный общий делитель
[![asciicast](https://asciinema.org/a/ZfY8Mrd2SliIRvYL78eJiBBip.svg)](https://asciinema.org/a/ZfY8Mrd2SliIRvYL78eJiBBip)

- **Brain-progression** — какое число пропущено в прогрессии
[![asciicast](https://asciinema.org/a/mXJS98uV5Unevl2p1eIiOBDB3.svg)](https://asciinema.org/a/mXJS98uV5Unevl2p1eIiOBDB3)

- **Brain-prime** — является ли простым число
[![asciicast](https://asciinema.org/a/XRMk73I0xaAPB3eAErs1XBMgX.svg)](https://asciinema.org/a/XRMk73I0xaAPB3eAErs1XBMgX)


____
#### Для запуска игр нужно
- Python 3.10
- Poetry 1.2
____
#### Команды Makefile
**make build** — poetry build — команда для получения директории dist/ и пакетов для установки  
**make install** — poetry install  
**make brain-games** — poetry run brain-games  
**make publish** — poetry publish --dry-run — проверка готовности к публикации  
**make package-install** — python3 -m pip install --user dist/*.whl — установка программы  
**make package-reinstall** — python3 -m pip install --user --force-reinstall dist/\*.whl — переустановка программы  
**make lint** — poetry run flake8 brain_games — проверка линтера flake8 
____
