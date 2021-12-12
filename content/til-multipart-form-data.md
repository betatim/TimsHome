Title: TIL: Howto create multipart form data in Python
date: 2021-12-12
slug: python-create-multipart-formdata

_[What is a TIL?](../til-explained)_

Today I learnt how to encode data as `multipart/form-data` in Python. This is
useful if you want to construct the [body of a `POST` request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) yourself.

Once you find the answer it is surprisingly simple: [`encode_multipart_formdata()` in urllib3](https://urllib3.readthedocs.io/en/1.26.4/reference/urllib3.fields.html#urllib3.encode_multipart_formdata).

```
fields = {
    "foo": "bar",
    "somefile": ("somefile.txt", "contents of somefile"),
    "imagegfile": ("cats.png", open("cats.png").read(), "image/png"),
}

body, header = encode_multipart_formdata(fields)
```

You can then use `body` as the body of your POST request and the value of
header for the `content-type` header.

This is also a great example of why you should create "Today I Learnt"s. I had
figured out how to do this a few months ago, but it still took me 30 minutes
to find the bit of code I created back then. If I had written it down here it
would have taken minutes.
