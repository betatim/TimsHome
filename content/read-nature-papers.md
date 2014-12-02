title: Read any Nature Paper for Free
date: 2014-12-02

Today [Nature](http://www.nature.com)
[announced](http://www.nature.com/news/nature-makes-all-articles-free-to-view-1.16460)
that all papers published in their journals will be "made free to read
in a proprietary screen-view format that can be annotated but not
copied, printed or downloaded" all articles they have published.

If you want to read opinions about the merit of this move check out what Michael Eisen has to say

Michel Eisen wonders if [Nature’s “free to view” is a magnanimous gesture or a cynical ploy?](http://www.michaeleisen.org/blog/?p=1668) Considering how hard
they make it to find the link to the free-as-in-beer version of a paper, you
might think so.

### Bookmarklet

I bring you the <a href="javascript:(function()%7Bfunction%20callback()%7B(function(%24)%7Bvar%20jQuery%3D%24%3Bwindow.location%20%3D%20%22http%3A%2F%2Fwww.readcube.com%2Farticles%2F%22%2B%24(%22dd.doi%22).html().substr(4)%7D)(jQuery.noConflict(true))%7Dvar%20s%3Ddocument.createElement(%22script%22)%3Bs.src%3D%22https%3A%2F%2Fajax.googleapis.com%2Fajax%2Flibs%2Fjquery%2F1.7.1%2Fjquery.min.js%22%3Bif(s.addEventListener)%7Bs.addEventListener(%22load%22%2Ccallback%2Cfalse)%7Delse%20if(s.readyState)%7Bs.onreadystatechange%3Dcallback%7Ddocument.body.appendChild(s)%3B%7D)()">Nature, read now!</a> bookmarklet. Just drag it to
your bookmarkbar, click it when viewing the public page of an article
and be taken straight to the full text of the article.

If you can not drag the bookmarklet here is the source so you can
create it manually. To create the "Nature, read now!" Bookmarklet you
need to copy the code below into the URL field of a new bookmark.

    :::javascript
    javascript:(function(){function callback(){(function($){var jQuery=$;window.location = "http://www.readcube.com/articles/"+$("dd.doi").html().substr(4)})(jQuery.noConflict(true))}var s=document.createElement("script");s.src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js";if(s.addEventListener){s.addEventListener("load",callback,false)}else if(s.readyState){s.onreadystatechange=callback}document.body.appendChild(s);})()

### Example

Head over to [Proton transport through one-atom-thick
crystals](http://www.nature.com/nature/journal/vaop/ncurrent/full/nature14015.html),
the latest paper on how graphene will revolutionise the world. Hit the
"Nature, read now!" bookmarklet button, et voila you see the full text.