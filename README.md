#   AutoMachineLearning-Web-App

**AutoMachineLearning Web App** to intuicyjna aplikacja webowa zbudowana w Pythonie, która automatyzuje cały proces Machine Learningu — od eksploracyjnej analizy danych (EDA) po trenowanie modeli i ich eksport.

Dzięki połączeniu bibliotek **Streamlit**, **ydata-profiling** oraz **PyCaret**, możesz przejść od surowego pliku CSV do gotowego modelu ML w kilka minut, bez pisania ani jednej linii kodu modelu.

---

##   Funkcje aplikacji

Aplikacja podzielona jest na 4 główne moduły:

1. **  Upload**: Prześlij swój zestaw danych w formacie CSV. Aplikacja zapamięta go na potrzeby dalszych kroków.
2. **  Profiling**: Automatyczne generowanie raportu EDA (Exploratory Data Analysis) przy użyciu `ydata-profiling`. Sprawdź korelacje, brakujące dane i statystyki kolumn.
3. **  ML (Model Training)**:
* Wybierz zmienną docelową (*Target*).
* Automatyczne czyszczenie danych (konwersja typów, uzupełnianie braków średnią).
* Porównywanie wielu modeli klasyfikacyjnych jednocześnie.
* Wyświetlenie najlepszego modelu i jego parametrów.


4. **  Download**: Pobierz wytrenowany model w formacie `.pkl`, gotowy do wdrożenia w środowisku produkcyjnym.

---

##   Technologie

Aplikacja wykorzystuje następujące biblioteki:

* [Streamlit](https://streamlit.io/) - Interfejs użytkownika.
* [PyCaret](https://pycaret.org/) - Biblioteka Low-Code ML do automatyzacji potoków.
* [ydata-profiling](https://github.com/ydataai/ydata-profiling) - Zaawansowana analiza danych.
* [Pandas](https://pandas.pydata.org/) - Manipulacja i czyszczenie danych.

---

##   Jak zacząć?

### Wymagania

Upewnij się, że masz zainstalowanego Pythona (zalecany 3.10+).

### Instalacja

1. Sklonuj to repozytorium:
```bash
git clone https://github.com/karol2302/AutoMachineLearning-Web-App.git
cd AutoMachineLearning-Web-App

```


2. Zainstaluj wymagane biblioteki:
```bash
pip install streamlit ydata-profiling pycaret pandas

```


3. Uruchom aplikację:
```bash
streamlit run app.py

```



---

##  Przepływ pracy (Workflow)

 
> **Krok 1:** Wgraj plik CSV w zakładce "Upload".
> **Krok 2:** Przejdź do "Profiling", aby zrozumieć strukturę swoich danych.
> **Krok 3:** W zakładce "ML" wybierz kolumnę, którą chcesz przewidzieć i kliknij przycisk trenowania.
> **Krok 4:** Pobierz gotowy plik `.pkl` i ciesz się modelem!

---

## 🧪 Przykładowe czyszczenie danych

Aplikacja posiada wbudowaną funkcję `clean_df`, która automatycznie:

* Usuwa wiersze z brakującym celem danych(*Target*).
* Konwertuje kolumny tekstowe na numeryczne lub kategoryczne.
* Usuwa stałe kolumny (mniej niż 2 unikalne wartości).
* Uzupełnia braki w danych numerycznych średnią.
 

