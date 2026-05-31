# Kosmosestartide ja ilmastikutingimuste analüüs

## Äriküsimus

Millised ettevõtted planeerivad lähiajal enim kosmosestarte ja kui suur on ilmastikust tulenev edasilükkamise risk stardiplatvormi asukohas?

Projekt aitab visualiseerida kosmosestartide aktiivsust ning hinnata võimalikke ilmastikuga seotud riske enne starti.

---

# Mõõdikud

## 1. Planeeritud startide arv ettevõtte kohta
Loendatakse mitu planeeritud starti on igal ettevõttel järgmise 30 päeva jooksul.

## 2. Ilmastikurisk stardiplatvormis
Arvutatakse halbade ilmastikutingimuste osakaal stardi ajal:
- tugev tuul
- vihm
- halb nähtavus

## 3. Kõige aktiivsemad stardiplatvormid
Loendatakse millistes asukohtades toimub enim starte.

---

# Andmeallikad

| Allikas | Tüüp | Ajas muutuv? | Roll |
|---|---|---|---|
| The Space Devs Launch Library API | API | Jah, mitu korda päevas | Põhiandmed kosmosestartide kohta |
| Open-Meteo API | API | Jah, tunnipõhiselt | Ilmaandmed stardiplatvormidele |

/HELENI KOMMENTAAR - kui sageli on "regulaarselt"?/
---

# Andmevoog

```mermaid
flowchart LR
    A[Launch Library API] --> B[Python sissevõtt]
    C[Open-Meteo API] --> B
    B --> D[(staging / raw)]
    D --> E[Transformatsioon]
    E --> F[(mart / analytics)]
    F --> G[Power BI või muu näidikulaud]
```

---

# Andmebaasi kihid

| Kiht | Roll |
|---|---|
| staging / raw | Hoiab allikast saadud andmeid muutmata kujul |
| mart / analytics | Hoiab analüütikaks ettevalmistatud ja transformeeritud andmeid |

```

# Riskid

| Risk | Mõju | Maandus |
|---|---|---|
| Launch Library API ei vasta või muudab andmestruktuuri | Andmete sissevõtt võib katkeda ning mõõdikud ei uuene | Lisame veakäsitluse ning kontrollime API vastuse struktuuri enne töötlemist |
| Stardiplatvormi koordinaadid puuduvad | Ilmaandmeid ei saa kõigi startide jaoks pärida | Märgime puudulike andmetega kirjed eraldi või jätame need analüüsist välja |
| Ilmaprognoos muutub kiiresti | Ilmastikurisk võib erineda tegelikust olukorrast stardi hetkel | Kasutame viimast saadaolevat prognoosi ja salvestame päringu aja |

---

# Käivitamine

```bash
# Repo kloonimine
git clone <repo-url>

# Liikumine projekti kausta
cd globaalsete-kosmosestartide-ja-ilmastikutingimuste-analuus
```

Sprint 1 jooksul tehakse esimesed API testid ja arhitektuuri valideerimine.

---

# Saladused ja konfiguratsioon

Projekt kasutab avalikke API-sid ning autentimist hetkel vaja ei ole.

Kui hiljem lisatakse API võtmeid:
- kasutatakse `.env` faili
- `.env` lisatakse `.gitignore` faili
- repos hoitakse ainult `.env.example` faili

---

# Andmevoog lühidalt

## Sissevõtt
Python skript pärib kosmosestartide andmed Launch Library API-st ning ilmaandmed Open-Meteo API-st.

## Laadimine

Sprint 2 jooksul salvestatakse andmed esmalt JSON kujul kausta `data/raw`.

Hilisemates sprintides laaditakse andmed PostgreSQL staging kihti.

## Transformatsioon
Andmed ühendatakse stardiplatvormi koordinaatide alusel ning arvutatakse ilmastikuriskid.

## Näidikulaud
Dashboard kuvab:
- startide arv ettevõtte kohta /HELENI KOMMENTAAR - kas visualiseerime TOP5 ettevõtet? Või lisame filtri et kasutaja saab ise valida kas TOP5 või BOTTOM5 või ettevõtte otsing nime järgi?/
- aktiivseimad stardiplatvormid
- ilmastikuriskid

---


# Tehnilised katsetused

## Launch Library API test

Testiti ühendust The Space Devs Launch Library API-ga.

Kuupäev: 25.05.2025

Tulemus:
- HTTP vastuskood: 200
- API vastas korrektselt
- Kosmosestartide andmed saadi edukalt kätte

Näidistulemus:
Falcon 9 Block 5 | Starlink Group 17-41

---


# Andmekvaliteedi testid

Projekt kontrollib:
- stardi ID unikaalsust
- puuduvate koordinaatide olemasolu
- kuupäevade korrektsust

---

# Projekti struktuur

```text
.
├── README.md
├── docs/
│   └── arhitektuur.md
├── scripts/
│   └── test_api.py
└── data/
```

---

# Kokkuvõte, puudused ja edasiarendused

## Kokkuvõte
Sprint 1 jooksul:
- valiti äriküsimus
- kaardistati API-d
- loodi arhitektuur
- testiti API ligipääsud

## Puudused
- andmebaasi automaatne laadimine pole veel realiseeritud
- dashboard pole veel loodud

## Mis edasi
- automaatne ETL töövoog
- PostgreSQL integratsioon
- visualiseerimine Power BI-s
- ilmastikuriski täpsem arvutamine

---

# Meeskond

| Nimi | Roll |
|---|---|
| [Katrin Laur] | 
| [Helen Vellau] | 
