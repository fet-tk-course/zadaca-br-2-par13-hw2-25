[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija

## O projektu

[Ovdje ukratko opišite domenu vaše aplikacije i njenu svrhu]

## Tim

- **Student A**: [Ime Prezime] - resurs: `/resursi_a`
- **Student B**: Arslan Telarević - resurs: `/resursi_b`

## Instalacija i pokretanje

### Preduvjeti

- Python 3.10 ili noviji
- pip

### Koraci

1. Klonirajte repozitorij:
```bash
git clone <url-repozitorija>
cd <naziv-repozitorija>
```

2. Kreirajte virtuelno okruženje:
```bash
python -m venv venv
```

3. Aktivirajte virtuelno okruženje:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Instalirajte zavisnosti:
```bash
pip install -r requirements.txt
```

5. Pokrenite aplikaciju:
```bash
uvicorn main:app --reload
```

6. Otvorite browser na adresi: `http://localhost:8000/docs`

## API Endpointi

### Resurs A: `/resursi_a`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/resursi_a` | Lista svih resursa (sa query filterom) |
| GET | `/resursi_a/{id}` | Dohvatanje resursa po ID-u |
| POST | `/resursi_a` | Kreiranje novog resursa |
| PUT | `/resursi_a/{id}` | Potpuna zamjena resursa |
| PATCH | `/resursi_a/{id}` | Djelimično ažuriranje resursa |
| DELETE | `/resursi_a/{id}` | Brisanje resursa |

**Primjer zahtjeva:**
```bash
# Kreiranje novog resursa
curl -X POST "http://localhost:8000/resursi_a" \
  -H "Content-Type: application/json" \
  -d '{"polje1": "vrijednost", "polje2": 123}'
```

### Resurs B: `/resursi_b`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/resursi_b` | Lista svih resursa (sa query filterom) |
| GET | `/resursi_b/{id}` | Dohvatanje resursa po ID-u |
| POST | `/resursi_b` | Kreiranje novog resursa |
| PUT | `/resursi_b/{id}` | Potpuna zamjena resursa |
| PATCH | `/resursi_b/{id}` | Djelimično ažuriranje resursa |
| DELETE | `/resursi_b/{id}` | Brisanje resursa |

## Korištenje AI alata

### Alat: [GitHub Copilot / ChatGPT / ...]
**Model:** Gemini ,Claude(Sonnet 4.6)

**Primjer 1:**
- **Prompt:** "Kreiraj SQLModel klase za entitet Proizvođač automobila (Manufacturer) sa poljima za naziv, državu, godinu osnivanja, broj zaposlenih, prihod i web stranicu, uključujući Create i Update sheme."
- **Kako je pomoglo:** Modeliranje podataka je ubrzano.
- **Prilagodbe:** Morao sam ručno dodati Optional tipove i Field(default=None) za polje website. Također, zbog specifičnosti Python 3.12/3.14 okruženja, bilo je potrebno precizno definisati tipove podataka (anotacije) kako bi Pydantic ispravno prepoznao polja

**Primjer 2:**
- **Prompt:** "Implementiraj PATCH endpoint za djelimično ažuriranje proizvođača koristeći exclude_unset=True i objasni kako spriječiti prepisivanje postojećih podataka praznim vrijednostima."
- **Kako je pomoglo:** Dobio sam precizan šablon za korištenje model_dump(exclude_unset=True) i setattr funkcije. Ovo mi je pomoglo da razumijem razliku između potpune zamjene resursa (PUT) i djelimične izmjene (PATCH)
- **Prilagodbe:** Prvobitno je kod uključivao exclude_none=True, ali sam to uklonio jer bi to spriječilo korisnika da namjerno postavi neko polje (npr. website) na null. Također sam prilagodio poruke o greškama na bosanski jezik i dodao provjeru postojanja resursa (404 Not Found) prije procesiranja podataka.

- 

## Napomene

Upravljanje okruženjem i verzijama: Tokom implementacije utvrđeno je da verzija Python 3.14 (pre-release) uzrokuje greške u pydantic validaciji zbog promjena u načinu interpretacije tipova (anotacija). Problem je riješen migracijom na stabilnu verziju Python 3.11, što je osiguralo potpunu kompatibilnost sa SQLModel bibliotekom.


Prvojera 2:
u zad1 ,u modelsb dodane validation funckije koje provjeravaju da li u poslatom json formatu od strane korisnika sadrzi ime i employees u slucaju da nije uneseno iybacit ce greesku.
isto u routes u post metodi dodana je funkcija koja provjerava da li unos od strane korisnika vec postoji .
U zad2 nova get metoda ocekuje standardan ulaz od korisnika gdje se prije samog ulaska u funkciju provjerava da li je sve ispravno uneseno i pretvara se u pzdantic model.Ova metoda sta radi prebrojava po id sve u bayi dostupne proizvodjace i na kraju ispise.
