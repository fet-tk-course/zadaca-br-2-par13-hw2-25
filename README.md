[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija

## O projektu

Ovo je REST API aplikacija za upravljanje auto salonom. Aplikacija omogućava vođenje evidencije o automobilima koji su na stanju, njihovim specifikacijama (godina, cijena, kilometraža, tip pogona), kao i praćenje informacija o proizvođačima automobila.

## Tim

- **Student A**: Tarik Jukan - resurs: `/cars`
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

### Resurs A: `/cars`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/cars` | Lista svih automobila (sa query filterima za godinu i električni pogon) |
| GET | `/cars/{id}` | Dohvatanje specifičnog automobila po ID-u |
| POST | `/cars` | Dodavanje novog automobila na stanje |
| PUT | `/cars/{id}` | Potpuna zamjena podataka o automobilu |
| PATCH | `/cars/{id}` | Djelimično ažuriranje podataka automobila |
| DELETE | `/cars/{id}` | Brisanje automobila iz baze |

**Primjer zahtjeva:**
```bash
# Kreiranje novog automobila
curl -X 'POST' \
  '[http://127.0.0.1:8000/cars/](http://127.0.0.1:8000/cars/)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "model_name": "Golf 8",
  "year": 2021,
  "price": 35000.0,
  "is_electric": false,
  "mileage": 45000,
  "color": "siva",
  "description": "Odlično stanje, prvi vlasnik",
  "manufacturer_id": 1
}'
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

## Napomene

Upravljanje okruženjem i verzijama: Tokom implementacije utvrđeno je da verzija Python 3.14 (pre-release) uzrokuje greške u pydantic validaciji zbog promjena u načinu interpretacije tipova (anotacija). Problem je riješen migracijom na stabilnu verziju Python 3.11, što je osiguralo potpunu kompatibilnost sa SQLModel bibliotekom.

## Zadatak 3 – Dokumentacija projekta

## Opis dodanog u Z1 i Z2
Zadatak1: U model CarCreate dodani su Pydantic validatori za provjeru ispravnosti unosa. Uspostavljena je veza sa tabelom proizvođača. 
Zadatak2: Rute i Logika U POST endpointu implementirana je provjera duplikata. Kreiran je i novi, nestandardni GET endpoint /cars/statistics koji računa globalnu statistiku automobila u salonu.


## Opis promjena u modelu
Dodani strani ključ: manufacturer_id unutar modela Car.
Relacija: Strani ključ povezuje resurs Car sa resursom **Manufacturer (Proizvođač) preko polja manufacturer.id.


## Opis validacijskih pravila i HTTP statusa
Validacija naziva modela: Naziv ne smije biti prazan string i mora imati najmanje 2 znaka.
Greška: Ukoliko pravilo nije ispunjeno, vraća se HTTP 422 Unprocessable Entity.
Validacija cijene price Cijena automobila mora biti strogo veća od nule.
Greška: Ukoliko je cijena nula ili negativna, vraća se HTTP 422 Unprocessable Entity.
Provjera duplikata (POST): Sistem ne dozvoljava unos automobila sa identičnim nazivom modela i godinom proizvodnje.
Greška Ako automobil već postoji, vraća se HTTP 409 Conflict.


## Primjeri zahtjeva i očekivanih odgovora za nove endpointe

## 1. POST /cars/ (Kreiranje novog automobila)
Primjer zahtjeva (Body):
    {
      "model_name": "Golf 8",
      "year": 2024,
      "price": 25000.0,
      "is_electric": false,
      "mileage": 15000,
      "color": "Crna",
      "description": "Odlično stanje",
      "manufacturer_id": 1
    }
Očekivani odgovor:
    {
      "id": 1,
      "model_name": "Golf 8",
      "year": 2024,
      "price": 25000.0,
      "is_electric": false,
      "mileage": 15000,
      "color": "Crna",
      "description": "Odlično stanje",
      "manufacturer_id": 1
    }


# 2. GET /cars/statistics 
Primjer zahtjeva:GET http://localhost:8000/cars/statistics
Očekivani odgovor (HTTP 200 OK):
    {
      "ukupno_automobila": 2,
      "prosjecna_cijena": 23500.0,
      "prosjecna_kilometraza": 18500.0
    }