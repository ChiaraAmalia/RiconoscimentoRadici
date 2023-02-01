## Progettazione e sviluppo di un algoritmo per il riconoscimento e la stima della crescita dell'apparato radicale mediante immagini RGB

## Obiettivi del progetto

L’obiettivo è quello di analizzare immagini di piantine (es. fagioli, ceci, lenticchie) collocate su una carta di germinazione in funzione dell’accrescimento radicale.Per far ciò e necessario individuare ed estrarre l’apparato radicale della pianta e produrne lo scheletro, semplificando la struttura della radice senza modificarne le caratteristiche. Ciò costituisce una base di partenza per il calcolo di parametri relativi alla crescita dell’apparato radicale sulla base dei dati ottenuti e all’individuazione
di eventuali giunzioni e terminazioni.</br>
L’algoritmo deve essere in grado di estrapolare dall’immagine in RGB del campione
il suo apparato radicale, filtrando le altre unità presenti nell’immagine del
campione, come il bulbo, le luci e la scacchiera ai lati della carta di germinazione
su cui poggiano le radici.</br>
A questo punto, avendo ottenuto un’immagine contenente il solo apparato radicale
della pianta è necessario ricavarne lo scheletro, su cui verranno poi evidenziati
eventuali nodi e terminazioni delle singole radici.</br>

## Sviluppo del progetto

### Setup Sperimentale
Lo sviluppo del progetto si basa sulle immagini campione fornite, ottenute attraverso la tecnica GrowScreen-PaGe[1]. Per ottenere tali immagini sono stati posti su carte di germinazione i semi germinati, fissati con del nastro adesivo di carta, a sua volta fissato con l’utilizzo di mollette. Per nutrire le piantine, la carta di germinazione viene imbevuta d’acqua e sostanze nutrienti utili a far crescere la pianta e fissata su una piastra di plexiglas (PMMA). Su ambo i lati della carta di germinazione, fissati sulla stessa piastra di materiale plastico, sono posti un codice QR e una striscia di quadratini disposti alternativamente, come una scacchiera. Analizzando il codice QR è possibile estrarne il codice identificativo relativo al campione posto sulla carta di germinazione, ulteriormente riportato in chiaro al di sotto di esso.

### Catalogazione campioni
Le immagini dei campioni sono scattate con una fotocamera che rinomina i file secondo l’ordine in cui sono state scattate, non riportando quindi informazioni utili ai nostri scopi. Tuttavia, i file in sé contengono molte informazioni sotto forma di metadati, tra questi la data e l’ora originali in cui è avvenuto lo scatto. Considerando sia le informazioni contenute nei metadati che il codice identificativo estratto dal QR-code è possibile riconoscere il campione e i suoi giorni di vita; tali dati possono quindi essere utilizzati per catalogare le piantine. Tale catalogazione si articola su una serie di passaggi:
<ul>
  <li>Controllo della presenza dei campioni nella cartella di lavoro</li>
  <li>Estrazione dei campioni</li>
  <li>Decodifica del QR-code</li>
  <li>Archviazione dei campioni</li>
</ul>

### Individuazione della regione di interesse
Ora che le immagini sono archiviate in cartelle rinominate attraverso il codice identificativo di ciascuna piantina e i relativi file al loro interno sono ordinati in base alla data e l’ora originale dello scatto, vengono svolti una serie di passaggi al fine di individuare l’area di interesse (region of interest). Le immagini vengono recuperate, dopo aver controllato che il file di interesse si trovi nella relativa sottocartella, prendendo il path dell'omonimo file ed estraendo solo le immagini con estensione '.jpg' o '.png', ottenendo una lista di tutte le immagini presenti nella cartella. Avendo recuperato le immagini, le operazioni che seguono al fine della rilevazione della regione di interesse sono:
<ul>
  <li>Ritaglio dell'immagine secondo misure specifiche, in modo da prendere solo l'area di interesse, compresa tra la scacchiera</li>
  <li>Conversione in HSV, per distinguere ancor più chiaramente l'apparato radicale</li>
  <li>Applicazione della maschera per il riconoscimento dell'apparato radicale, con conversione ad immagine binaria al fine di individuare i contorni all'interno dell'immagine, potendo quindi ottenere un'immagine ulteriormente ritagliata, potendo poi visualizzare nitidamente l'apparato radicale della piantina in esame.</li>
  <li>Effettuiamo successivamente la rimozione del nastro in quanto nell'immagine è presente un nastro al fine di mantenere ferma la piantina durante la crescita, comportando però dei problemi nel riconoscimento dell'apparato della stessa. Si è proceduto quindi alla rimozione del nastro, mediante il calcolo della concentrazione di pixel bianchi nella zona superiore della maschera invertita.</li>
  <li>Thinning dell'immagine per visualizzare in maniera più dettagliata l'apparato radicale della piantina, mediante l'operazione di erosione e successiva applicazione del thinning in cui i pixel assumono valore o 0 o 1 </li>
  <li>A questo punto siamo andati a calcolarci perimetro e area dell'apparato radicale, in centimetri</li>
</ul>  

### Studio dello scheletro
Una volta ottenuto lo scheletro, possiamo effettuare su di esso diverse misurazioni, sia sull’apparato radicale nella sua totalità sia sui singoli segmenti che lo compongono. Il passo successivo consiste nell’implementare le basi per lo studio di tali segmenti ricercando i nodi e le terminazioni dell’apparato. Le operazioni svolte sono quindi state:
<ul>
  <li>Per l'individuazione di nodi e terminazione è stato utilizzato l'algoritmo di rilevazione Harris Corner Detector</li>
  <li>Le immagini risultanti dall’applicazione dell’algoritmo di Harris non vengono popolate da singoli punti distanti fra loro, ma da un accumulo di punti che non delineano in maniera precisa le informazioni riguardanti i nodi e le terminazioni. Questi agglomerati vanno quindi sostituiti da un punto medio che possa riassumere le informazioni ottenute con l’algoritmo di Harris, migliorando di conseguenza l’immagine risultante e facilitando la sua analisi.</li>
  <li>Con l’operazione di clustering vengono riprodotte sullo scheletro le informazioni più importanti, descrivendo al meglio le caratteristiche dell’apparato radicale. Queste informazioni devono quindi essere estratte dall’immagine ed elaborate sotto forma di dati tecnici per facilitarne la lettura, come l'angolazione e la lunghezza di ogni singolo segmento.</li>
</ul>

## Risultati
In questa sezione vengono riportati i relativi risultati ottenuti dal calcolo del perimetro e dell'area, sia in pixel che in centrimetri, di alcuni campioni più rilevanti.

## Conclusioni e Sviluppi futuri
Lo sviluppo del progetto ha portato alla realizzazione di un algoritmo in grado
di riconoscere l’apparato radicale di piantine poste su carta di germinazione e di
analizzare le caratteristiche dei segmenti che compongono le radici. Il progetto pone le basi per il miglioramento e lo sviluppo di utilità che possano facilitare l’utilizzo dell’algoritmo sviluppato da parte di utenti più o meno specializzati. Vi sono ancora diversi elementi che possono essere introdotti e quelli di maggiore interesse sono:
<ul>
  <li>Sviluppo di un'interfaccia grafica </li>
  <li>Introduzione di ulteriori parametri</li>
  <li>Implementazione di un algoritmo per l'autoarchiviazione delle immagini, direttamente all'avvenimento dello scatto</li>
  <li>Migliore integrazione con la riga di comando</li>
  <li>Implementazione di algoritmo complementare per lo scatto automatico</li>
  <li>Implementazione di una base di dati</li>
</ul>

Ulteriori dettagli relativi all'attività svolta sono riportati nella seguente [tesi](https://github.com/ChiaraAmalia/RiconoscimentoRadici/blob/main/Tesi%20-%20Chiara%20Amalia%20Caporusso%20S1087171.pdf)

### Tecnologie utilizzate
Per lo sviluppo del progetto è stato utilizzato Python (versione 3.9) come linguaggio di programmazione, integrando un insieme di librerie utili all’analisi dell’apparato radicale (NumPy, ZBar, Request, Exif, scikit-image).

