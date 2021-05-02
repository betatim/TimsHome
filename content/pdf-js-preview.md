Title: TIL: PDF JS Preview
date: 2021-05-02
slug: pdf-js-preview

Today I learnt how to use [PDF.js](https://mozilla.github.io/pdf.js/) to
add a PDF preview to a HTML form without having to upload the file to a server.

I needed this to build a multi-step form that shows a preview before we have
reached the last step in the form submission.

A demo is worth a thousand words:

<p class="codepen" data-height="383" data-theme-id="light" data-default-tab="result" data-user="betatim" data-slug-hash="abpjwaZ" style="height: 383px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="PDF preview form">
  <span>See the Pen <a href="https://codepen.io/betatim/pen/abpjwaZ">
  PDF preview form</a> by Tim (<a href="https://codepen.io/betatim">@betatim</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>
<br>

Check out the [code of the codepen](https://codepen.io/betatim/pen/abpjwaZ) to
see how it is done.

This is a useful little snippet of JavaScript that means users do not have to
upload the PDF to your servers first to get a preview image. In this case the
API that receives the PDF does not offer an option to render only the first
page. You have to upload the whole document, basically submitting the form,
and then tidy up again when the user decides not to submit the form.

A advantage of doing the rendering on the client side is that you do not have
to upload the PDF first. This can be a huge benefit if your users are on a
slow internet connection and have large files.

A drawback of using PDF.js is that if your PDF is expensive to render, it can
take a while to get that preview image on a low powered device like a mobile
phone.

One thing that took me a while to figure out is that you should not include the
`pdf.worker.js` via a `<script>` tag. Instead you should set `pdfjsLib.GlobalWorkerOptions.workerSrc = "https://unpkg.com/pdfjs-dist/build/pdf.worker.js"` in your JS. Figuring this out
took a while because a lot of examples either load it in `<script>` tag or do
not make any mention of it. If you load it the wrong way you will see a warning
in your console about PDF.js using a "dummy worker".
