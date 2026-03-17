---
title: "Embed pentru orice album de Picasa"
date: 2010-02-01 08:39:03 +0000
categories: ["Social Media"]
tags: ["cum-sa-faci", "embed", "google", "picasa"]
author: titus_capilnean
---

Azi dimineață m-am lovit de faptul că trebuia să pun un slideshow de Picasa, pe un blog. De obicei, pun direct codul de embed, din pagina albumului(fie că este Picasa, fie că este Flickr sau orice alt hoster de poze care oferă posibilitatea de a face slideshowuri). De data asta, nu aveam acces la cont și a trebuit să găsesc o soluție.

M-am uitat în codul de embed de la un alt album(să zicem al meu) și am înlocuit datele importante de acolo. Pentru asta trebuie să afli 2 elemente importante:  
  
1\. contul de Google de pe care vrei să extragi albumul – nume.prenume(sau nickname, depinde de cum e mailul persoanei x@gmail.com)  
2\. codul albumului de pe Picasa

Primul se află foarte simplu.

Dacă vrei să afli codul de album, trebuie să intri în feed-ul RSS al albumului și să copiezi din link numărul de identificare pentru albumul respectiv:

http://picasaweb.google.com/data/feed/base/user/_nume.user(aflat la pasul 1)_ /albumid/**1230709345452241857**

Din fericire, codul de embed pentru Picasa este universal. Trebuie doar modificate datele de identificare ale utilizatorului, chestie care se face destul de ușor. Să vă arăt.

Hai să analizăm un pic codul de embed și să vedem unde trebuie puse datele noi.

<embed type=”application/x-shockwave-flash” src=”http://picasaweb.google.com/s/c/bin/slideshow.swf” width=”400″ height=”267″ flashvars=”host=picasaweb.google.com&hl=en_US&feat=flashalbum&RGB=0x000000&feed=http%3A%2F%2Fpicasaweb.google.com%2Fdata%2Ffeed%2Fapi%2Fuser%2F**(nume user de la pasul 1)** %2Falbumid%2F**(cod aflat la pasul 2)** %3Falt%3Drss%26kind%3Dphoto%26hl%3Den_US” pluginspage=”http://www.macromedia.com/go/getflashplayer”></embed>

Practic trebuie să înlocuiești parantezele cu cele 2 informații de care vorbeam mai sus și gata.

Iei codul nou și îl pui pe blog/site. Merge 100%. Sper că o să fie util cuiva. Mie mi-a fost 🙂
