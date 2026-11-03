---
title: "5 Plugin-uri de Wordpress necesare pentru blogul tau"
date: 2009-08-01 12:00:00 +0000
categories: ["Social Media"]
tags: []
author: titus_capilnean
---

![](http://farm3.static.flickr.com/2012/2113909936_36aa728b59.jpg)

sursa FOTO

Când mi-am instalat pentru prima dată WordPress 2.3.8, imediat am căutat și am cerut câteva recomandări de ce extensii aș avea nevoie. N-am găsit nicăieri centralizate toate plugin-urile de care are nevoie un blog pentru a putea fi folosit la capacitate maximă. Am făcut articolul ăsta în special pentru cei care și=au instalat un WordPress și simt nevoia să scoată mai multe de la el.

Eu am instalat și activat **24 de plugin-uri** și o să vă povestesc despre majoritatea dintre ele, în ordinea importanței lor pentru blog. Primele 5 consider că sunt vitale pentru funcționarea în stare bună a oricărui blog. Ce e mai jos vă oferă facilități mișto, dar alegeți voi dacă vreți să vi le instalați sau nu.

  1. Akismet – cel mai celebru și **cel mai bun tool antispam**. La început poate să nu pară util, însă când blogul va deveni mai citit, vor apărea și roboții de spam care vor încerca să publice comentarii la întâmplare. Îl recomand călduros pentru orice blog, ca prim plugin de instalat.  
Se instalează automat, iar pentru configurare are nevoie de API Key-ul de WordPress, care se obține din contul de pe WordPress.com – dacă nu ai user, îți faci și apoi preiei API Key-ul și îl introduci în setările Akismet.
  2. Comments Notifier – cu ajutorul lui **primești comentariile direct pe mail,** ca să fii mereu la curent cu ce se întâmplă pe blog. Reacționează inclusiv la ping-back-uri(linkuri externe către articolul tău). Se instalează foarte ușor și se configurează de la Opțiuni – unde se introduce adresa de mail unde vrei să trimiți comentariile. E foarte util mai ales pentru blogurile colective, pentru că poți introduce mai multe adrese de mail către care să se trimită notificări.
  3. Google Analytics Plugin – în loc să introduci codul de Analytics direct în cod, WordPress are o soluție mai elegantă, prin acest plugin. Se instalează foarte ușor – Install New și apoi se introduce codul de tracker – UA-xxxxx-yy din contul de Analytics. Dacă nu ai cont, se face în câteva minute pe google.com/analytics
  4. ntz Antispam – probabil că v-ați întrebat ca mine – de ce două filtre de spam? Pentru că dacă trece ceva de unul, de al doilea sigur nu trece. Pluginul ăsta minuscul oprește foarte eficace spamul pe blog. Install and enjoy!
  5. Smart 404 – Se întâmplă ca din când în când utilizatorii de pe blogul tău să greșească un link, să dea click pe ceva ce nu mai există, să tasteze în plus caractere și să ajungă la o pagină de eroare. Pluginul acesta le va arăta câteva articole de citit în caz că au ajuns pe pagina 404 din greșeală. Practic înlocuiește pagina veche cu anunțul de eroare cu o pagină nouă, mult mai plină de informații și variante. Se instalează ca orice alt plugin, însă la configurație mai trebuie să modifici fișierul _404.php_ sau să cauți condiționala de _404_ din _MainPageTemplate.php_(depinde foarte mult de tema pe care o ai)Codul care trebuie să îl introduci:


    
    
         <?php if (smart404_has_suggestions()) : ?>
         Try one of these links:
         <?php smart404_suggestions(); ?>
         <?php endif; ?>

Acestea sunt din punctul meu de vedere cele 5 pluginuri obligatorii pentru orice blog. Data viitoare o să povestesc despre alte 5 pluginuri care îmi fac blogul să arate mai bine ![:D ](/assets/img/posts/2009/5-plugin-uri-de-wordpress-necesare-pentru-blogul-tau/yahoo_bigsmile.gif)

Spor la scris!

  * June 14, 2011 -- Plugin-urile de Wordpress pe care le folosesc pe blog
  * April 20, 2011 -- Problema e la departamentul de marketing si comunicare
  * August 30, 2009 -- Adevarul despre adolescenti si Twitter
