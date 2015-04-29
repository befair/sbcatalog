# Social Business Catalog

[Social Business Catalog (beta)](http://sbcatalog.labs.befair.it) è un aggregatore, una vetrina ed una API
per fornitori e prodotti dell'economia solidale.

### Perché

per avere un deposito (`repository`) da cui attingere e su cui riversare i dati dei fornitori e prodotti ecosol italiani;

### Come

con tecnologie "smart" che ci consentono di fare prototipazione rapida e "toccare con mano" la sfida.... e con grande entusiasmo!

SBcatalog propone:

* una interfaccia web gradevole e di semplice consultazione su PC, tablet e smartphone;
* una API che consenta ai programmatori di caricare e scaricare i cataloghi dei fornitori con cui sono in relazione;
* l'integrazione con [il portale nazionale dell'economia solidale](http://www.economiasolidale.net);

Visione d'insieme dove AGGREGATOR = SBCatalog:
![Visione d'insieme](./docs/SBCatalog_comprehensive_view.png "Visione d'insieme")

Lo schema è stato preso dalla tesi di Matteo Micheletti "Definition and implementation of a data exchange and share standard between solidarity-based group management programmes"

**NOTA**: i nomi dei siti/software sono solo a titolo esemplificativo e non esaustivo, per una lista completa si veda il [wikibook GAS ed Economia Solidale](http://it.wikibooks.org/wiki/GAS_ed_Economia_solidale/Gruppo_d%27Acquisto_Solidale#Scegliere_un_gestionale_.28comparazione.29)

### Cosa

In particolare OGGI il contesto è costituito da questi elementi:

  * la rete **italiana** dell'economia solidale (REES ITA);
  * il formato GDXP che già sanno esportare ed importare GasDotto e Gasista Felice e in più ha passato un primo vaglio tecnico del gruppo di comunicazione della REES ITA;
  * (da condividere) una collocazione su sottodomini `*.economiasolidale.net` ad esempio: `sbcatalog.economiasolidale.net`
  * una interfaccia che raggiunga gli obiettivi PRIMARI:
    * visualizzazione e ricerca fornitori e prodotti;
    * multicanalità;
    * API import/export GDXP;
    * semplicità per l'utente;
  * una interfaccia che potrà raggiungere gli obiettivi SECONDARI:
    * ricerca per territori e categorie;
    * georeferenziazione;
    * API CRUD + import/export GDJP (corrispondente GDXP in json)
  * e infine:
    * utenti e interfaccia web di modifica delle anagrafiche e dei listini e API per la sincronizzazione con i vari software per i GAS
    * import (o possibilità di) "rating" dei fornitori e prodotti fatto su altre piattaforme

**Ora l'obiettivo è di fare un proof-of-concept per dire che "SI... PUÒ... FARE!!"**, ma anche **LO STIAMO FACENDO!**.

Sì perché l'economia solidale è questo, è inventarsi modi nuovi, è riscoprire le relazioni, è superare delle sfide
e ormai in molti lo stiamo facendo. Con leggerezza, dedizione e costanza: e ce la stiamo facendo.

Grazie a tutti quelli che ci provano

[Il team beFair](http://www.befair.it)

## Prerequisiti

* Installare mongo ed npm (su Debian: sudo apt-get install mongodb npm)
* Su Debian, creare un symlink per l'eseguibile di node (sudo ln -s /usr/bin/nodejs /usr/bin/node)
* Installare harp con npm (sudo npm install -g harp)

## Installazione

### Server

    $ pip install -r requirements.txt
    $ cd sbcatalog
    $ cp settings_dist.py settings.py
    $ ./run.py

### Client

    $ cd sbcatalog-ui/public
    $ harp server
    $ firefox http://localhost:9000

### Utilizzo API

    $ curl -d @<file.gdxp> -H "Content-type: text/xml" http://localhost:5000/gdxp/supplier/

## Autori

* Luca Ferroni
* Andrea Colangelo
* Antonio Esposito
* Matteo Micheletti
* Michele Sorcinelli

## License

sbcatalog is Copyright © 2015 beFair.it

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License version 3, as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranties of MERCHANTABILITY,
SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Affero General Public License for more details.

You should have received a [copy of the GNU Affero General Public License](./LICENSE.md)
along with this program.  If not, see <http://www.gnu.org/licenses/>.

