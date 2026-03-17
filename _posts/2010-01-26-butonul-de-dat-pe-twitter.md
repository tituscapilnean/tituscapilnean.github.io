---
title: "Butonul de dat pe Twitter"
date: 2010-01-26 06:14:50 +0000
categories: ["Social Media"]
tags: ["buton", "share", "twitter"]
author: titus_capilnean
# BROKEN_IMAGES: 1 image(s) could not be resolved
#   - http://tituscapilnean.ro/wp-content/uploads/2010/01/comm.jpg
---

Totul a pornit de aici:

[![comm](/wp-content/uploads/2010/01/comm.jpg)](/wp-content/uploads/2010/01/comm.jpg)

> PS: Ca tot era vorba de Twitter, daca aveai un buton pe aici pe undeva, ii trageam si un ReTweet, dar asa…

comentariu lăsat de Cristi

Inițial, eram pe punctul să instalez un plugin care trimite mesajele pe Twitter, însă și așa trebuie să mă apuc de curățenie prin jungla de pluginuri instalate pe blog(da, nu e bine să ai prea multe – încetinesc mult încărcarea și dau erori dacă nu sunt compatibile – jquery vs. prototype).

Am căutat câteva zile, pe mai multe bloguri care au un buton de genul ăsta, și m-am oprit la subiectiv, pentru că mi s-a părut cel mai curat mod de a trimite articole pe Twitter.

Ideea din spate este să pui un link dinamic, care preia automat **titlul articolului** și **permalinkul(cel scurt)** și le transmite, ca parametri către Twitter.com. Pe lângă asta, poți adăuga un scurt mesaj personalizat, ca să recunoască lumea de unde vin respectivele tweeturi.

Cum se face? Simplu, introduci următorul cod, undeva pe blogul tău, în index.php/single-post.php/page.php, obligatoriu în interiorul The Loop.

_< a href=”http://twitter.com/home?status=<?php the_title(); ?> – <?php echo bloginfo(‘home’).”/?p=”.$post->ID; ?>”>Dă-l pe Twitter</a>_

Cam asta e toată filosofia 🙂

Dacă nu vă iese ceva, puteți să îmi puneți întrebări aici și încerc să vă răspund.
