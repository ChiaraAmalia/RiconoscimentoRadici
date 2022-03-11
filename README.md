## Progettazione e sviluppo di un algoritmo per il riconoscimento e la stima della crescita dell'apparato radicale mediante immagini RGB

## Obiettivi del progetto

L’obiettivo è quello di analizzare immagini di piantine (es. fagioli, ceci, lenticchie)
collocate su una carta di germinazione in funzione dell’accrescimento radicale.Per
far ciò e necessario individuare ed estrarre l’apparato radicale della pianta e produrne
lo scheletro, semplificando la struttura della radice senza modificarne le
caratteristiche. Ciò costituisce una base di partenza per il calcolo di parametri
relativi alla crescita dell’apparato radicale sulla base dei dati ottenuti e all’individuazione
di eventuali giunzioni e terminazioni.</br>
L’algoritmo deve essere in grado di estrapolare dall’immagine in RGB del campione
il suo apparato radicale, filtrando le altre unità presenti nell’immagine del
campione, come il bulbo, le luci e la scacchiera ai lati della carta di germinazione
su cui poggiano le radici.</br>
A questo punto, avendo ottenuto un’immagine contenente il solo apparato radicale
della pianta è necessario ricavarne lo scheletro, su cui verranno poi evidenziati
eventuali nodi e terminazioni delle singole radici.</br>

Per lo sviluppo del progetto è stato utilizzato Python (versione 3.9) come linguaggio
di programmazione, integrando un insieme di librerie utili all’analisi dell’apparato
radicale.

