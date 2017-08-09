---
permalink: /course/lab/rdp-netsurf-xfce4/
---
# Lab - Using Remote Desktop to NetSurf on Xfce4 via Xrdp

*Last Updated: July 28, 2017*

[NetSurf](http://www.netsurf-browser.org/) is a lightweight open-source web browser. [Xfce](https://xfce.org/) is a lightweight desktop environment for UNIX-like operating systems. Both aim to be fast and low on system resources. Below are steps to set up a NetSurf browser on a Xfce4 desktop that can be accessed using Windows’ default [Remote Desktop](https://support.microsoft.com/en-hk/instantanswers/ff521c86-2803-4bc0-a5da-7df445788eb9/how-to-use-remote-desktop) client. The virtual machine (VM) used in this example is an [f1-micro](https://cloud.google.com/compute/pricing#predefined_machine_types) instance with a Ubuntu 16.04 LTS boot image created in [Google Compute Engine](https://cloud.google.com/compute/). We can use Google Cloud’s default [firewall rules](https://console.cloud.google.com/networking/firewalls/) here which already allow RDP on port 3389.

## Installations

On the newly created VM, install NetSurf, Xfce4, and [xrdp](http://www.xrdp.org/):

```bash
sudo apt-get update
sudo apt-get install netsurf-gtk
sudo apt-get install xfce4
sudo apt-get install xrdp
```

## Create Password

```bash
sudo passwd <Your User Name>
```

This password will be used to remotely log onto the virtual machine running xrdp.

## Configure xrdp

```bash
echo xfce4-session > .xsession
sudo vi /etc/xrdp/startwm.sh
```

The last line in `startwm.sh` should be `. /etc/X11/Xsession`. Replace it with `startxfce4`.

![](http://realai.org/course/lab/rdp-netsurf-xfce4-1.png)

Now restart xrdp and the remote desktop will be up and running:

```bash
sudo service xrdp restart
```

## Connect to Remote Desktop

Enter the VM’s External IP in Windows’ Remote Desktop client, then log onto the VM using the password created earlier. Now we can access NetSurf from by clicking *Applications*, then *Internet* on the top-left corner of the remote desktop.

![](http://realai.org/course/lab/rdp-netsurf-xfce4-2.png)

To set the default browser, from *Applications*, click *Settings*, then *Preferred Applications*. In the *Preferred Applications* dialog window, choose *Other* and enter `netsurf`.

![](http://realai.org/course/lab/rdp-netsurf-xfce4-3.png)

Now we can launch the browser by clicking on the Earth icon at the bottom of the desktop:

![](http://realai.org/course/lab/rdp-netsurf-xfce4-4.png)

