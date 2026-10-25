# Python projekti

Repozitorij s manjim Python projektima za učenje i vježbanje neuronskih mreža, mrežne, gui i rada sa sistemskim naredbama.

## Projekti

| Datoteka | Opis |
|---|---|
| `neural-network-simple.py` | Jednostavna neuronska mreža implementirana pomoću NumPyja za prepoznavanje rukom pisanih znamenki. |
| `IPsocket.py` | Skripta za vježbanje mrežne komunikacije i rada sa socketima. |
| `Tkinter_login.py` | Primjer grafičkog sučelja za prijavu izrađenog pomoću Tkintera. |
| `wifi-pass-viewer.py` | Windows skripta za pregled spremljenih Wi-Fi profila i prikaz dostupne spremljene lozinke odabranog profila. |

## Instalacija

### 1. Kloniranje repozitorija

```bash
git clone [https://github.com/abesic1/Python-Projekti--](https://github.com/abesic1/Python-Projekti--)
cd Python-Projekti--
```

### 2. Izrada virtualnog okruženja

```powershell
python -m venv .venv
```

Aktivacija u Windows PowerShellu:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalacija ovisnosti

U glavnoj mapi napravi datoteku `requirements.txt` sa sljedećim sadržajem:

```text
numpy
scikit-learn
```

Ako je virtualno okruženje aktivirano, instaliraj pakete naredbom:

```powershell
python -m pip install -r requirements.txt
```

## Pokretanje

Naredbe pokreni iz glavne mape projekta, s aktiviranim virtualnim okruženjem.

### Neuronska mreža

```powershell
python neural-network-simple.py
```

Skripta koristi skup podataka `load_digits` iz biblioteke scikit-learn. Ulazne vrijednosti normaliziraju se dijeljenjem sa 16, a oznake znamenki pretvaraju se u one-hot zapis.

Mreža ima:

- 64 ulazne značajke.
- Skriveni sloj s 32 neurona i ReLU aktivacijom.
- Izlazni sloj s 10 izlaza, po jedan za svaku znamenku.
- Softmax za izračun postotka vjerojatnosti tijekom treniranja.
- Ručno implementiranu propagaciju pogreške unatrag i ažuriranje parametara.

Na kraju se ispisuje točnost na podacima korištenima za treniranje. Taj rezultat nije točnost na zasebnom testnom skupu.

### Mrežna komunikacija

```powershell
python IPsocket.py
```

Prije pokretanja provjeri IP adresu, port i ostale mrežne postavke definirane u skripti.

### Grafičko sučelje za prijavu

```powershell
python Tkinter_login.py
```

Projekt prikazuje primjer sučelja za prijavu. Sam prikaz forme ne podrazumijeva sigurnu autentifikaciju ili sigurno spremanje lozinki.

### Pregled spremljenih Wi-Fi profila

```powershell
python wifi-pass-viewer.py
```

Skripta koristi Windows naredbu `netsh`. Nakon prikaza spremljenih profila korisnik odabire profil unosom njegova broja.

Napomene:

- Skripta je namijenjena Windowsu.
- Radi sa spremljenim profilima, a ne s lozinkama proizvoljnih obližnjih mreža.
- Prikaz lozinke ovisi o dostupnosti spremljenog ključa i korisničkim ovlastima.
- Koristi je samo na vlastitom računalu ili uz uz dopuštenje vlasnika.
- Nemoj objavljivati ispis koji sadrži lozinke.

## Struktura repozitorija

```text
Python-Projekti/
├── IPsocket.py
├── Tkinter_login.py
├── neural-network-simple.py
├── wifi-pass-viewer.py
└── README.md
```


## Svrha projekta

Projekti su namijenjeni učenju i eksperimentiranju. Prije korištenja u stvarnim aplikacijama potrebno ih je dodatno testirati te prilagoditi sigurnosnim i funkcionalnim zahtjevima.
