# docker-django-fullstack

Full stack django environment build on multiple docker containers ready for `development` and `production`.

- `postgres` (`postgis` ready)
- `nginx` (static serving)
- `gunicorn` (app server)
- `redis` (cache)
- `celery` (`rabbitmq` as broker)

## Development

### MacOS X

**Setup**

- `brew`
- `pip`

```
brew install docker boot2docker
sudo pip install docker-compose
boot2docker upgrade
boot2docker init
```

In case of errors, try `boot2docker delete && boot2docker init` again.
For more details, read [documentation](https://docs.docker.com/installation/mac/).

Create host alias for current docker host IP with `echo $(boot2docker ip) dockerhost | sudo tee -a /etc/hosts`.
IP can change in future, update it in `/etc/hosts` if necessary.

**Running**

```
boot2docker start
$(boot2docker shellinit)
docker-compose up
```

- Browse to [http://dockerhost/](http://dockerhost/)
- Or something like `docker-compose run django python manage.py shell|migrate|collectstatic`

## Deployment

### Use tutum
brew install tutum

### Ubuntu Server

**Requirements**

- `ansible` on local machine
- Server E.g. Ubuntu 14.04 x64 on Digital Ocean
- Your SSH pub key in `authorized_keys` on server
- Your server's IP or Domain in your ansible inventor (e.g. `/usr/local/etc/ansible/hosts` like `myserver ansible_ssh_port=22 ansible_ssh_host=IP`)
- And enter server's IP, Domain or pattern in `ansible-playbook.yml`
- Run `ansible-playbook ansible-playbook.yml`

### Google Compute Engine

- create account and project at https://console.developers.google.com/project
- install google cloud sdk on local machine https://cloud.google.com/sdk/
- run `gcloud auth login`
- set current project `gcloud config set project PROJECT`

gcloud components update alpha
gcloud config set compute/zone europe-west1-b
gcloud alpha container clusters create guestbook




### Deploy

## Todos:

- Add:
    - [ ] Add Celery test
    - [ ] Postgres / Postgis
- [ ] ansible: use newest docker-compose version, not fixed one
- [ ] ansible: don't use unstable docker.io. but stable uses still fig atm...
- [ ] user Kubernetes with GCE

- http://www.syncano.com/configuring-running-django-celery-docker-containers-pt-1/
- http://davidmburke.com/2014/09/26/docker-in-dev-and-in-production-a-complete-and-diy-guide/


### Tipps & Tricks

- Delete all docker containers `docker rm -f $(docker ps -a -q)`
- Delete all docker images `docker rmi -f $(docker images -q)`

