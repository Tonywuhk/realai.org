---
permalink: /course/google-cloud-platform/gce-sc2le/
title: Course | GCP | GCE | Running StarCraft II Learning Environment on Google Compute Engine
---
[Home](http://realai.org/) > [Course](http://realai.org/course/) > [TensorFlow](http://realai.org/course/tensorflow/) > [IT 101](http://realai.org/course/tensorflow/#it-101) >

# Running StarCraft II Learning Environment on Google Compute Engine

*Last Updated: August 10, 2017*

On [Google Compute Engine](http://realai.org/course/google-cloud-platform/#google-compute-engine), create an [n1-standard-1](https://cloud.google.com/compute/pricing#predefined_machine_types) instance with a Ubunbu 16.04 LTS boot image.

## Installing Conda

```bash
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
rm Miniconda3-latest-Linux-x86_64.sh
```

## Installing Unzip

```bash
sudo apt update
sudo apt install unzip
```

## Installing StarCraft II API and PySC2

The [StarCraft II API](https://github.com/Blizzard/s2client-proto) is an interface that provides full external control of StarCraft II. [PySC2](https://github.com/deepmind/pysc2) is DeepMind's Python component of the StarCraft II Learning Environment (SC2LE). 

```bash
wget http://blzdistsc2-a.akamaihd.net/Linux/SC2.3.16.1.zip
unzip -P iagreetotheeula SC2.3.16.1.zip
rm SC2.3.16.1.zip
pip install pysc2
```

Download a map that will be used to run an agent:

```
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Melee.zip
unzip -P iagreetotheeula Melee.zip -d StarCraftII/Maps/
rm Melee.zip
```

## Installing a Remote Desktop and Play!

Largely follow [these steps](http://realai.org/course/google-cloud-platform/rdp-netsurf-xfce4/). The main commands used are:

```bash
sudo apt install xfce4
sudo apt install xrdp
echo xfce4-session > .xsession

# In the next vi window, replace the last line with "startxfce4"
sudo vi /etc/xrdp/startwm.sh

# sudo passwd <Your User Name>
# make up a password
sudo service xrdp restart
```

Connect to the remote desktop, and find the sequence number of $DISPLAY that the X server uses by either entering `ls /tmp/.X11-unix`, or entering `who` after opening a terminal on the remote desktop. Assuming the sequence number is 10, then we can launch [StarCraft II](http://realai.org/environments/#starcraft-ii) in the remote desktop by entering in our original terminal the command:

```bash
DISPLAY=:10 python -m pysc2.bin.agent --map Simple64
```

The whole experiment took around 30 minutes of time, most of which was spent on downloading the `SC2.3.16.1.zip` file.

![](http://realai.org/course/google-cloud-platform/gce-sc2le-1.png)

