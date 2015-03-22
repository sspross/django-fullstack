# docker-django-fullstack

Full stack django environment as docker image ready for `development` and `production`.

- `postgres` (`postgis` ready)
- `nginx` (static serving)
- `gunicorn` (app server)
- `redis` (cache)
- `celery` (`rabbitmq` as broker)

## TL;DR

- Develop: `docker-compose up` and [http://dockerhost:8000/](http://dockerhost:8000/)
- Setup Deployment: `ansible-playbook ansible-playbook.yml`
- Deploy `fab production deploy`


## Development Setup

### MacOS X

**Requirements**

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

**Create host alias for current VM IP**

`echo $(boot2docker ip) dockerhost | sudo tee -a /etc/hosts`

IP can change in future, update it in `/etc/hosts` if necessary.

**Running**

```
boot2docker start
$(boot2docker shellinit)
docker-compose up
```

Browse to [http://dockerhost:8000/](http://dockerhost:8000/)

Or something like `docker-compose run web python manage.py shell`

## Deployment

**Requirements**

- `ansible`

### Server Setup Example

- Ubuntu 14.04 x64 on Digital Ocean
- Your SSH pub key in `authorized_keys` on server
- Your server's IP or Domain in your ansible inventor (e.g. `/usr/local/etc/ansible/hosts`)
- And enter server's IP, Domain or pattern in `ansible-playbook.yml`
- Run `ansible-playbook ansible-playbook.yml`



