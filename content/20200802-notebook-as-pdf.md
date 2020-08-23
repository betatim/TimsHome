Title: Save Jupyter Notebooks as PDF
date: 2020-08-23
slug: jupyter-notebooks-as-pdf

This post introduces a Jupyter notebook extension that I created to help
you save your notebooks as PDFs. It is available as [`notebook-as-pdf`](https://pypi.org/project/notebook-as-pdf/) and the source is on [`betatim/notebook-as-pdf`](https://github.com/betatim/notebook-as-pdf). Try it without having to install anything: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/betatim/notebook-as-pdf/master)

This extension does a few things differently, it will:

* produce a PDF with the smallest number of page breaks,
* attach the original notebook to the PDF,
* automatically generate a table of contents from the main headings; and
* this extension does not require LaTex.

The rest of this post will explain each of those four points in more detail.

![](/images/nb-as-pdf-header.jpg)

This blog post is about turning notebooks into PDF that aren't meant to be printed.


## Create the smallest number of pages

The created PDF will have as few pages as possible, in many cases only one. A quick and unscientific poll on twitter confirmed my hunch that a lot of people save their notebooks as PDF not because they want to print them but to share them with others. Based on this I decided that `notebook-as-pdf` should not be limited
by existing paper formats that people have in their printers.

![](/images/nb-as-pdf-one-page.png)

Most notebooks will be converted into a single page PDF.

This means the PDF you get will be very close to the look of a website, you can keep scrolling with no page breaks. For very long notebooks I discovered that some PDF viewers have a built-in limit to the extent of a page. As a result notebook-as-pdf will insert a page break when the page is longer than about 200in or 508cm.


## Attach the original notebook

Technically a PDF document can be edited, but realistically when you export a notebook to a PDF the result is a "read only" document. Most of the time this is a good thing. The PDF gets attached to emails or shared in others ways. You do not want it to accidentally get edited or changed.

However, sometimes you will have to go back and reproduce the PDF. Maybe some of the numbers do not add up or someone wants to change the dataset or the labels need fixing. This is when having the original notebook attached to the PDF comes in handy.

Most people will have their notebooks in a Git repository or version them some other way. This means that they could just go to the commit that was current when the PDF was created and they should have the version that was used to make the PDF. Technically. In practice people forget to commit the exact version they used or little tweaks get made that get forgotten about.

Luckily, the PDF specification allows you to attach a file to a PDF. notebook-as-pdf uses this feature to attach the original `.ipynb` file to the PDF. This allows you to go back to exactly the version of a notebook that was exported. All you need is the PDF in question.

![](/images/nb-as-pdf-attachment.png)

The [pdf.js](https://mozilla.github.io/pdf.js/) viewer has an "attachments" tab that lets you open the original notebook `.ipynb`.

Unfortunately not all PDF viewers know how to deal with attachments. They will happily open a PDF with an attachment, but they will not let you download it. PDF viewers known to support downloading of file attachments are: Acrobat Reader, [pdf.js](https://mozilla.github.io/pdf.js/) (the viewer used by Firefox) and [evince](https://wiki.gnome.org/Apps/Evince). The [pdftk CLI](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/) program can also extract attached files from a PDF. Sadly Preview for OSX does not know how to give you access to attachments of PDF files.


## Automatically generate a table of contents

Navigating a large notebook can be tricky. This is why notebook-as-pdf will generate a table of contents for the PDF. Every main heading (technically every `<h1>` tag) in the notebook will be converted into an entry in the table of contents. This lets you quickly navigate the contents of the notebook. It also allows you to link people directly to a section you want them to read.

![](/images/nb-as-pdf-table-of-contents.png)

The table of contents view in pdf.js

In a future version lower level headings might be included in the table of contents. This would give you a more detailed view of the notebook structure but also more clutter in the table of contents. Maybe a better solution is to allow people to insert "bookmarks" into the notebook. Each of these bookmarks would then be a table of contents entry.


## Do not use LaTeX

The final feature is that [notebook-as-pdf](https://pypi.org/project/notebook-as-pdf/) uses Chromium to convert the notebook into a PDF. This means you do not need to install LaTeX which can be challenging to get to work because it is such a large and powerful piece of software.

Instead notebook-as-pdf uses the "convert HTML to a PDF" feature of Chromium. The Chromium project spends a lot of time working on making it easy to install and work on all major platforms.

The way notebook-as-pdf uses it is in "headless" mode. This means no window opens up when using it.


This post introduces a Jupyter notebook extension that I created to help
you save your notebooks as PDFs. It is available as [`notebook-as-pdf`](https://pypi.org/project/notebook-as-pdf/) and the source is on [`betatim/notebook-as-pdf`](https://github.com/betatim/notebook-as-pdf). You can try it without having to install anything: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/betatim/notebook-as-pdf/master)
