# django-fullstack

[![Docker Repository on Quay.io](https://quay.io/repository/sspross/django-fullstack/status "Docker Repository on Quay.io")](https://quay.io/repository/sspross/django-fullstack)

Full stack django example project build on multiple docker containers ready for `development` and `production`.

**Batteries**

- `postgres` (with `postgis` and `hstore` extensions)
- `nginx` 
- `gunicorn` 
- `redis` 
- `celery`
- `rabbitmq`

**Create your own**

This repository is an instance of [cookiecutter-django-fullstack](https://github.com/sspross/cookiecutter-django-fullstack). Check it out to create your own django fullstack project.

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
- Or so something like `docker-compose run django python manage.py shell|migrate|collectstatic`

## Deployment

### Docker Registry

Register your django app image (e.g. this repo) to a docker registry. E.g. [quay.io](https://quay.io/), which builds your container images on git push.

0. Push your repository to GitHub
0. Create an account on [quay.io](https://quay.io/)
0. Add a repository and link it to your GitHub repository
0. Update `image`s of `django` and `worker` in `tutum.yml` to `quay.io/YOURUSER/YOURDJANGOPROJECT`  

### Managed Cloud Deployment

You can deploy this app in many different ways of course. E.g. just checking it out on a server and running it with `docker-compose` (not recommended for production use and that's so 2014). So we use [tutum.co](https://www.tutum.co/) to manage our cloud (nodes on e.g. DigitalOcean or Amazon) and deployment of our docker images. 

0. Create an account on [tutum.co](https://www.tutum.co/)
0. Create at least 1 node (e.g. on DigitalOcean). How many nodes you need and which containers are best on which nodes depends heavy on your kind of application. But you can change this later very easy thanks to tutum.co
0. Update `VIRTUAL_HOST` of `django` in `tutum.yml`to `nginx.YOURDJANGOPROJECT.YOURUSER.svc.tutum.io` and use it to create a new stack on tutum.co
0. Start it and browse to [http://nginx.YOURDJANGOPROJECT.YOURUSER.svc.tutum.io/](http://nginx.YOURDJANGOPROJECT.YOURUSER.svc.tutum.io/)

## Todos:

- [ ] Fix code live editing in development
- [ ] `docker-compose.yml` and `tutum.yml` are very similar....
- [ ] How to use a domain... and is this `vhost.d` the best way?
- [ ] Add Celery test
- [ ] Add Postgis
- [ ] Try Kubernetes (with GCE)

## Tipps & Tricks

- Delete all docker containers `docker rm -f $(docker ps -a -q)`
- Delete all docker images `docker rmi -f $(docker images -q)`

