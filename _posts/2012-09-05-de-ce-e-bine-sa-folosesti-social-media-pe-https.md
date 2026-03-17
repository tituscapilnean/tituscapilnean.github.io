---
title: "De ce e bine sa folosești social media pe HTTPS"
date: 2012-09-05 07:00:29 +0000
categories: ["Altele de online"]
tags: ["furt", "https", "online", "vox-populi"]
author: titus_capilnean
# BROKEN_IMAGES: 1 image(s) could not be resolved
#   - http://tituscapilnean.ro/wp-content/uploads/2012/09/security-web-150x150.jpg
---

_Guestpost scris de Mihnea Beldescu, viitor Phd, geek și twitterist._

[](/wp-content/uploads/2012/09/security-web.jpg)Răspunsul scurt la aceasta intrebare e simplu: **Pentru ca să nu-ți fie furat contul.**

Un pic mai pe larg, există o diferență importantă între HTTP și HTTPS: In primul caz datele sunt transmise în clar(de ex. Parolele sunt un câmp text simplu) iar în al doilea caz datele sunt criptate înainte de a fi transmise. În cazul Facebook și Twitter criptarea in discuție e pe 128 biți. Ca să vă faceți o idee despre durata de timp necesară pentru a sparge o astfel de criptare puteți arunca un ochi pe acest articol. Majoritatea criptării folosite în mod curent pe Internet este pe 128 biți iar pe unele site-uri de internet banking am observat că se folosește o criptare pe 256 biti, care este de multe ori mai greu de spart printr-o metodă de tip brute-force.

Dacă folosiți deja Facebook sau Twitter pe HTTPS puteți să stați destul de linistiți, (mult) mai repede câștigați la loto decât să vă spargă cineva contul prin brute-force. Desigur, asta nu se aplică atunci când intrați într-un showroom de magazin, după aceea repede pe Facebook de pe vreun telefon sau tabletă lăsată la dispoziție și plecați înainte de a da Logout. Dar chiar și în acest caz, respectivul nu va putea să schimbe parola dacă nu o introduce întâi pe cea veche.

Acum vine partea “distractivă”. Să ne imaginăm urmatorul scenariu: Ești cu iPhone-ul într-un pub. Pentru că nu prea mai ai trafic de date „3G” intri pe rețeaua WiFi din dotarea localului. Dacă în vecinătatea ta se afla un hacker cu adevărat bun, nu prea ai nicio șansă. Folosind un tip de atac de tipul MITM (man-in-the-middle) respectivul se înfățișează ca fiind routerul wireless la care ești conectat, iar de aici, relativ simplu îți poate fura sesiunea de Facebook (sau Twitter etc). Important de notat ca fură sesiunea (de fapt un cookie – celebrele cookies) nu parola și atunci pentru Facebook o sa pară ca un request vine ca din partea utilizatorului de drept. Desigur, dacă ai da logout imediat, sesiunea nu ar mai fi validă si ai scăpat de problemă.

Din fericire hackeri experimentați nu se află pe toate drumurile. Veste proastă este ca există un program de Android ce poate face așa ceva, condiția fiind ca utiliztorul să aiba telefonul root-at pentru a putea face astfel de manevre. Cu ajutorul unui astfel de program (de exemplu, unul se poate descărca de aici) orice utilizator fără absolut nicio cunoștință primară de hacking, networking sau programare poate să fure sesiuni, ceea ce ar putea destule neplăceri pe care nu cred că e nevoie să le enumăr aici.

Câteva sfaturi pentru a nu ți se întâmpla așa ceva:

  * În primul rand treci pe HTTPS. Pentru Facebook e foarte simplu: Account Settings -> Security -> Secure Browsing și se bifează căsuța respectivă
  * Pentru Twitter:Settings -> Account -> HTTPS only să fie bifat
  * Folosiți pe cât vă permite traficul de internet pe telefon (și bateria) conexiunea 3G. Consumă mai mult decât WiFi
  * Aveți grijă ce aplicații autorizați să aibă acces la cont. Sunt destule cazuri în care aplicații rogue au început să posteze mesaje publicitare (mai ales pe Twitter) sau alte minuni.
