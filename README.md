# SETUP

1. Run `docker build . -t taj/multi-client` - the `taj/multi-client` is a tag for the docker container that we create.
2. Use docker compose to run our apps in isolated environments by running the command
```sh
docker-compose up -d
```
`-d` would run a daemon process.
3. This is the most annoying part unfortunately - you will have to modify your local `/etc/hosts` file to test this locally

I had to add the following to my `/etc/hosts`

```
...
127.0.0.1       client1.polls.local
127.0.0.1       client2.polls.local
...
```

This gives us the ability to access nginx-proxy inside the dockers - not sure how this works in terms of networking.

NOTE: I'm quite rusty when it comes to `nginx` so there might be a better way to do this and not have to worry about this part. 