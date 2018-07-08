# Reinforcement Learning - Coding Challenge 1

In this challenge you'll work on setting up a local environment suitable for
reinforcement learning. We'll use a tool called Docker to facilitate building
and running containers with our code and dependencies. Because this challenge
is "operational" there will be a range of goals - if you're familiar with Docker
you should jump ahead to the stretch goals, but if this is your first time using
it then just getting through the first one or two is reasonable.

## Goal 0 - Understanding "What is Docker?"

This goal does not involve turning anything in, but it is good before you get
started to take a moment and understand what this tool does. Normally when you
install and run software, you are downloading packages and drivers and running
them directly on your local operating system (which in turn mediates the
resources from your physical machine) - this is a sensible approach for most
things, but when you're dealing with complicated projects things can get ugly:

- Inconsistencies deploying across different operating systems - Windows, Mac,
  and Linux can have obscure disagreements about everything from case
  sensitivity to network operations
- Conflicting dependencies across projects - project 1 wants Python 2, project 2
  wants Python 3
- Hidden assumptions - a project works in one environment because it happens to
  have the correct global installation or other dependency, but breaks elsewhere

And even when things do work, they often get "entangled" and it's hard to
reproduce why they're working, and dangerous to remove things or start over.

One possible but absurd solution - just buy a different computer for everything.
If you have a complete dedicated piece of hardware set up for each significant
project/task, then it can be consistent and functional and avoid conflicts.

A slight improvement - instead of actual computers, use virtual machines. These
function the same as separate computers, but with the different hardware
emulated (so you could buy less hardware overall).

A better way - containers. This is what Docker does, and they are similar to
virtual machines in that they function as independent computers and keep things
separate, but they are lighter weight because they share the system kernel. This
means you can run more of them with less hardware, and they're much cheaper to
start and stop (or even destroy and recreate).

Docker is a major player in the container space, and provides a fast workflow
for quickly building, running, and deploying images (operating systems *and*
running software). A `Dockerfile` gives you a standard reproducible formula for
the software you're running, and it works the same across platforms. There is a
learning curve - brushing up on your command line skills is advisable - but the
benefits are significant, and it is a widely used tool in industry.

## Goal 1 - Hello Docker!

Your first task is to install Docker and verify your success by running a basic
container. Docker containers are portable, but Docker itself is still
platform-specific software, so installation will vary. In general, you want the
free community edition, and you don't need to make a Docker ID unless you intend
to publish your own Docker containers.

- Download links: https://www.docker.com/community-edition#/download
- Mac instructions: https://docs.docker.com/docker-for-mac/install/
- Windows instructions: https://docs.docker.com/docker-for-windows/install/

If you use a command line package management tool there is probably a `docker`
package available, e.g. `brew cask install docker` on MacOS and similar 
(distribution-dependent) on Linux.

Once you've installed Docker, you can test by running:
`docker run hello-world`

You should see and message that says your installation is working, and gives
instructions and links to take things further. For more details see:
https://docs.docker.com/samples/library/hello-world/

You should explore the suggested resources, but for now once you've got
`hello-world` working you should move to the text task.

## Goal 2 - Docker Compose and Open AI Gym

https://github.com/ageron/handson-ml/tree/master/docker

## Goal 3 - To JupyterHub and Beyond!

https://github.com/jupyterhub/jupyterhub
