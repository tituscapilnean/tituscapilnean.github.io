---
title: "Filme virusate circula libere pe internet"
date: 2009-07-06 15:30:00 +0000
categories: ["Social Media"]
tags: ["avi", "film", "nou", "torrent", "virus", "windows-media-player"]
author: titus_capilnean
---

De câteva zile încoace, de când au apărut noile filme la cinematografe, au apărut pe internet două tipuri de torrente și filme shared pe DC++ – cele flimate în cinematograf(TS CAM) și cele așa-zise ”DVD”, ambele în formate .avi

Am descărcat la un moment dat unul din acelea calitate ”DVD” și am încercat să îl rulez cu VLC VideoLan Player, cu cele mai noi K-lite Codecs instalate pe Windows. Filmul părea de 6 secunde lungime și cerea să fie rulat în Windows Media Player – deja un lucru bizar, dădea de bănuit.

L-am rulat pe Windows Media Player:

![](http://3.bp.blogspot.com/_X8QCWf-Nggg/SlI13gnwVMI/AAAAAAAABKU/l_vAOcfZNAE/s400/virus1.jpg)

După cele 6 secunde mi s-a deschis o fereastră de browser, care arăta așa:

![](http://1.bp.blogspot.com/_X8QCWf-Nggg/SlI2hPkchJI/AAAAAAAABKc/M0AZZGPouFc/s400/virus3.jpg)

Observați formatul paginii cu elementele de identificare Microsoft împrăștiate peste tot, așa încât să deruteze orice utilizator mai neatent și nerăbdător să descarce niște codecuri care să îl ajute să vadă filmul. Dacă ne uităm mai atent la bara de adresă a site-ului, se observă că în loc de un site Microsoft, apare o adresă de IP cel puțin dubioasă. Fail.

deci videocodec.exe este virus!

Dacă dai vre-un click pe pagină, oriunde ai da, se descarcă acel virus pe calculatorul tău.

Deștept, nu?

![](http://4.bp.blogspot.com/_X8QCWf-Nggg/SlI3d29Mu2I/AAAAAAAABKk/geVGZpAeiYo/s400/virus4.jpg)

Pt. geeks: artea și mai deșteaptă a virusului este că au reușit să includă în partea de header a fișierului exact identificatorul de codec-avi și cele 6 secunde în corpul filmului, restul până la 700 MB fiind cod ASCII la întâmplare. Din fericire, G-Spot Codec information îl detectează ca și fake, mai ales că decodorul folosit e WMV și nu AVI.

Și mai deștept.

Filme virusate până acum – Ice Age 3, The Proposal, Transformers 2, ce să mai, majoritatea box office hit-urilor de luna trecută și luna asta.

Aveți grijă ce descărcați de pe net, pentru că s-ar putea să vă alegeți cu un gândac în loc de film.
