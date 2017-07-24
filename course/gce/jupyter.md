---
permalink: /course/gce/jupyter/
---
# Running Jupyter on Google Compute Engine

It is very easy to setup a remote [Jupyter Notebook](http://jupyter.org/) with [Google Compute Engine](https://cloud.google.com/compute/). First we create a firewall rule. Then we create a virtual machine subject to that rule. Finally a few commands to install Jupyter, we're all set to launch and access it from the web.

## Create a Firewall Rule

Click on the 3-line icon on the top left corner of cloud console, go to **Networking** and **Firewall rules**. Here we name the rule *jupyter* and use the same name as the **Target tag**. To allow incoming traffic from all over the Internet, we set **Source IP range** to be *0.0.0.0/0* ([CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation)), and **Specified protocal and port** is *tcp:8888*, the default port to be used by Jupyter notebook. Click **Create** to add this rule.

![](/assets/images/course-gce-jupyter-1.png)

## Create a Virtual Machine

Click on the 3-line icon on the top left corner of your [Cloud Console](https://console.cloud.google.com), go to **Compute Engine** and **VM instances**. Create a [f1-micro](https://cloud.google.com/compute/pricing#predefined_machine_types) machine with a [Ubuntu](https://www.ubuntu.com/) 16.04 LTS boot image.

![](/assets/images/course-gce-jupyter-2.png)

Expand the **Management, disks, networking, SSH keys** section at the bottom of the above screenshot, then add the tag of the firewall rule created earlier. Click **Create** to launch this virtual machine.

![](/assets/images/course-gce-jupyter-3.png)

Now the VM instance is running, and on the **VM instances** page it should be assigned an **External IP**, this is the IP address we will later use to access Jupyter Notebook. Now SSH to the VM to install Jupyter:

```bash
# Install pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
rm get-pip.py

# Install Jupyter
sudo pip3 install jupyter
```

That's it, the setup is complete! We can launch Jupyter Notebook from the SSH terminal:

```bash
jupyter notebook --ip=0.0.0.0
```

Now Jupyter Notebook should be live on the web at `http://<External IP>:8888`. Access token can be found in the SSH terminal. To exit Jupyter, press "Ctrl-c" twice.

