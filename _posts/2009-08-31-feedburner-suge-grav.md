---
title: "Feedburner suge grav – updated"
date: 2009-08-31 19:15:13 +0000
categories: ["Social Media"]
tags: ["alternativa", "crestere", "feedburner", "il-dezinstalez", "statistici-feed", "suge"]
author: titus_capilnean
---

![Feedburner suge](http://farm1.static.flickr.com/63/157700814_552e4f94e2.jpg?v=0) sursa foto

Am tot testat diverse metode de abonare la blogul meu, printre care și Feedburner, care este în proprietatea Google, deci ai zice că are garanția să ”facă succesuri” ușor și profi.

Din păcate, Feedburner și-a dovedit lunile ăstea două slăbiciuni mari. Pur și simplu nu se aduce la zi în Bloglines, rămâne cu cam **2-3 săptămâni în urmă** și ai impresia că omul nu a mai scris pe blog de ceva vreme. Azi am înțeles de ce aveam doar 42 de abonați la feed. Se dezabonau pentru că vedeau lipsa artificială de activitate de pe blog.

Ei bine, azi am scăpat de Feedburner și am revenit la aplicația de RSS a WordPress. **Cum se scapă de Feedburner:**

1\. Te duci în setările plug-inului de FeedBurner și elimini redirecționarea feed-ului către site-ul Feedburner  
2\. Dezactivezi plug-inul.  
3\. Elimini celelalte linkuri de Feedburner de pe blog – din header.php sau sidebar.php, dacă e cazul  
4\. Ștergi plugin-ul cu toate fișierele sale – Delete Plugin  
5\. Aștepți 1-2 ore să se facă resincronizarea pe serverle internaționale  
6\. Gata.

Singurele **2 facilități** care sunt oferite de Feedburner și aveau sens în ecuația blogului meu erau reclamele de RSS și contorizarea abonaților la feed.

Din păcate, reclamele de RSS mi-au adus în 2 luni abia **1,79$** , deci prima facilitate a devenit irelevantă.

Ca să contorizez numărul de oameni abonați la feed-ul meu și alte statistici similare, am găsit un plugin foarte bun și simpatic:

Feed Statistics

Se instalează foarte ușor, iar dacă vrei să afișezi numărul de abonați RSS, introduci în _sidebar.php_ sau în _header.php_ codul :

Am adunat în 8 ore de feed standard 38 50 de abonați 🙂

Aproape la fel de mulți cât în 2 luni pe Feedburner. De aia Feedburner suge.

**Update:** Coincidental, am găsit un articol tot despre Feedburner, pe Re:Fresh, unde se dezbate statistica oferită de Feedburner, relevanța cititorilor de RSS, ca număr, versus unici pe zi.

Rămâne să văd până la sfârștul săptămânii câți abonați de RSS se vor strânge și la mine, ca să pot face o analiză cât de cât a traficului pe feed și ratele de click – WP-FeedStatistics face asta 🙂

Update 2: Se pare că problema cu feed-urile este la abonații de după preluarea Google – cei vechi(de 1,5 – 2 ani) n-au probleme nici cu peste 500-1000 de readers. Încă investighez.
