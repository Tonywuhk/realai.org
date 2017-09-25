---
permalink: /course/google-cloud-platform/firefox-on-remote-desktop/
---
# Firefox on Remote Desktop

*Last Updated: September 25, 2017*

[Firefox](https://www.mozilla.org/en-US/firefox/) is a free and open-source web browser developed by [Mozilla](https://www.mozilla.org/en-US/about/). [Xfce](https://xfce.org/) is a lightweight desktop environment for UNIX-like operating systems that aims to be fast and low on system resources. Below are steps to set up a Firefox browser on a Xfce4 desktop that can be accessed using Windows’ default [Remote Desktop](https://support.microsoft.com/en-hk/instantanswers/ff521c86-2803-4bc0-a5da-7df445788eb9/how-to-use-remote-desktop) client. The virtual machine (VM) used in this example is an [f1-micro](https://cloud.google.com/compute/pricing#predefined_machine_types) instance with a Ubuntu 16.04 LTS boot image created in [Google Compute Engine](https://cloud.google.com/compute/). We can use Google Cloud’s default [firewall rules](https://console.cloud.google.com/networking/firewalls/) here which already allow RDP on port 3389.

## Installations

On the newly created VM, install Xfce4, [xrdp](http://www.xrdp.org/), and Firefox:

```bash
sudo apt update
sudo apt install xfce4
sudo apt install xrdp
sudo apt install firefox
```

## Configure xrdp

```bash
echo xfce4-session > .xsession
sudo vi /etc/xrdp/startwm.sh
```

The last line in `startwm.sh` should be `. /etc/X11/Xsession`. Replace it with `startxfce4`.

![](http://realai.org/course/google-cloud-platform/firefox-on-remote-desktop-1.png)

This is a good point to create a [persistent disk snapshot](https://cloud.google.com/compute/docs/disks/create-snapshots) if this setup will be reused in the future.

## Launch Remote Desktop

```bash
sudo passwd <Your User Name>
```

This password will be used to remotely log onto the virtual machine running xrdp.

Now restart xrdp and the remote desktop will be up and running:

```bash
sudo service xrdp restart
```

## Connect to Remote Desktop

Enter the VM’s External IP in Windows’ Remote Desktop client, then log onto the VM using the password created earlier. Now we can launch Firefox by clicking on the Earth icon at the bottom of the desktop:

![](http://realai.org/course/google-cloud-platform/firefox-on-remote-desktop-2.png)

