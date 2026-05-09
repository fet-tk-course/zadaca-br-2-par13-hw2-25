[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija

## O projektu

Ovo je REST API aplikacija za upravljanje auto salonom. Aplikacija omogućava vođenje evidencije o automobilima koji su na stanju, njihovim specifikacijama (godina, cijena, kilometraža, tip pogona), kao i praćenje informacija o proizvođačima automobila.

## Tim

- **Student A**: Tarik Jukan - resurs: `/cars`
- **Student B**: [Ime Prezime] - resurs: `/resursi_b`

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

[Analogno kao za Resurs A]

## Korištenje AI alata

### Alat: Alat: Gemini
**Model:** [GPT-4, Copilot model, ...]

**Primjer 1:**
- **Prompt:** [Npr. "Kreiraj SQLModel klasu za entitet Knjiga sa poljima naslov, autor, godina, isbn"]
- **Kako je pomoglo:** [Opis]
- **Prilagodbe:** [Da li ste morali prilagoditi generisani kod]

**Primjer 2:**
- **Prompt:** [Npr. "Implementiraj PATCH endpoint sa exclude_unset=True"]
- **Kako je pomoglo:** [Opis]
- **Prilagodbe:** [Opis]

## Napomene

[Dodatne napomene specifične za vašu implementaciju]