Title: TIL: Hotwire's Turbo with Python
date: 2021-04-25
slug: hotwire-turbo-with-python

[Hotwire's Turbo Streams](https://turbo.hotwire.dev/handbook/streams) can use
WebSockets to stream updates. How to do this is not well documented in the
handbook. This post contains my notes on building a prototype to figure out
how to do it. I used Tornado as webserver but the technique is completely
backend agnostic.


## What are Turbo Streams?

Turbo Streams allow you to send small fragments of HTML and replace parts of
the page with that new HTML. An example of a fragment you can send:

```
<turbo-stream action="append" target="messages">
  <template>
    <div id="message_1">
      This div will be appended to the element with the DOM ID "messages".
    </div>
  </template>
</turbo-stream>
```

## My setup

I wanted to build a web page that allows the user to submit a file for
processing and then retrieve their processed file once it is ready. For this
it would be nice to show a spinner or some kind of progress bar to the user
while the file is being worked on.

The form itself is a standard HTML form. It sends the form contents to `/convert`
using a POST request. The response is a HTTP status 303 redirect to `/status/<job_id>`.

The status page contains the following piece of JS in its `<head>` tag:

```
<script type="module">
  import { connectStreamSource } from 'https://cdn.skypack.dev/@hotwired/turbo';

  const wsUrl = ((window.location.protocol === "https:") ? "wss://" : "ws://") + window.location.host + "/status/{{ job_id }}"

  document.eventSource = new WebSocket(wsUrl);
  connectStreamSource(document.eventSource);
</script>
```

This is a template that the server renders, which means the `{{ job_id }}` is
replaced by the actual job ID.

Once the page loads a WebSocket is connected to `/status/<job_id>` over which
the server can send Turbo Stream templates that update what is shown to the user.


The body of the status page contains a `<div>` element telling the user that
the document is being processed:
```
<div id="status">
  <div class="spinner-border" role="status">
    <span class="visually-hidden">Processing...</span>
  </div>
</div>
```

The WebSocket handler at `/status/<job_id>` then sends a message like the
following once the file has been converted:
```
<turbo-stream action="replace" target="status">
  <template>
    <div id="status">
      <p><a href="/documents/{{ job_id }}/output/document.pdf">Download your PDF</a></p>
    </div>
  </template>
</turbo-stream>
```
which replaces the DOM element with the ID `status`.

That is all there is to using Turbo Streams via a long running WebSocket.

The project I used this for is [https://github.com/betatim/pdf-it](https://github.com/betatim/pdf-it).
