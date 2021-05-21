Title: TIL: Configure Traefik on bare metal
date: 2021-05-21
slug: traefik-config-bare-metal

_[What is a TIL?](../til-explained)_

Today I learnt how to configure [traefik](https://doc.traefik.io/traefik/) as reverse proxy for a service
running on "bare metal". I have a webserver listening on `http://localhost:8080`
and would like it to be reachable from the internet. With HTTPS.

I setup traefik v2.4.8 by downloading it and creating two config files.

The first config file sets up the basic, mostly static configuration. It lives
at `/etc/traefik/traefik.toml`:

```
[entryPoints]
  [entryPoints.web]
    address = ":80"
    [entryPoints.web.http.redirections.entryPoint]
      to = "websecure"
      scheme = "https"

  [entryPoints.websecure]
    address = ":443"

[api]
  dashboard = true

[certificatesResolvers.lets-encrypt.acme]
  email = "my-email@example.com"
  storage = "acme.json"
  [certificatesResolvers.lets-encrypt.acme.tlsChallenge]

[providers.file]
  filename = "/etc/traefik/traefik_dynamic.toml"
  watch = true
```

The interesting part (and where it would differ if your service was running in
a docker container) is the `[providers.file]` section. It points to the "dynamic"
configuration file (the second one I created) which configures the routers and services:
```
[tls.options]
  [tls.options.modern]
    minVersion = "VersionTLS13"

[http.middlewares.apiAuth.basicAuth]
  users = [
    # use `htpasswd -n admin` to generate the secret
    "admin:$apr1$.h4Eecwq$something-secret."
  ]

[http.routers.api]
  rule = "Host(`traefik-dashboard.example.com`)"
  entrypoints = ["websecure"]
  middlewares = ["apiAuth"]
  service = "api@internal"
  [http.routers.api.tls]
    certResolver = "lets-encrypt"
    options = "modern"

[http.routers.myservice]
  rule = "Host(`my-service.example.com`)"
  service = "myservice"
  [http.routers.myservice.tls]
    certResolver = "lets-encrypt"
    options = "modern"

[http.services]
  [http.services.myservice.loadBalancer]
    [[http.services.myservice.loadBalancer.servers]]
      url = "http://localhost:8080/"
```

After this run `traefik --configuration=/etc/traefik/traefik.toml` as root and
you will be able to visit the dashboard at https://traefik-dashboard.example.com.

The service which is listening on `localhost:8080` will be available at
https://my-service.example.com.

The cool thing is that traefik takes care of obtaining the TLS certificates from
Let's Encrypt.

To run traefik on my ubuntu machine I used `systemd` with the following
unit file:
```
[Unit]
# Wait for network stack to be fully up before starting proxy
After=network.target

[Service]
User=root
Restart=always
ProtectHome=yes
ProtectSystem=strict
PrivateTmp=yes
PrivateDevices=yes
ProtectKernelTunables=yes
ProtectKernelModules=yes
ReadWritePaths=/opt/traefik/state/acme.json
WorkingDirectory=/opt/traefik/state/
ExecStart=/opt/traefik/bin/traefik \
            --configfile /etc/traefik/traefik.toml

[Install]
# Start service when system boots
WantedBy=multi-user.target
```

And that was it. My service is reachable from the internet and uses HTTPS.
