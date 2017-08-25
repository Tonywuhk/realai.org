---
permalink: /course/lab/gce-jupyter/
---
# Lab - Running Jupyter on Google Compute Engine

*Last Updated: July 26, 2017*

It is very easy to setup a remote [Jupyter Notebook](http://realai.org/course/jupyter/) with [Google Compute Engine](http://realai.org/course/google-compute-engine/). First we create a firewall rule. Then we create a virtual machine subject to that rule. Finally a few commands to install Jupyter, we're all set to launch and access it from the web.

## Create a Firewall Rule

Click on the 3-line icon on the top left corner of cloud console, go to **Networking** and **Firewall rules**. Here we name the rule *jupyter* and use the same name as the **Target tag**. To allow incoming traffic from all over the Internet, we set **Source IP range** to be *0.0.0.0/0* ([CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation)), and **Specified protocal and port** is *tcp:8888*, the default port to be used by Jupyter Notebook. Click **Create** to add this rule.

![](http://realai.org/course/lab/gce-jupyter-1.png)

**Exercise:** Follow the same steps to create a rule *tensorboard* for port 6006. [TensorBoard](https://www.tensorflow.org/get_started/summaries_and_tensorboard) is a suite of [TensorFlow](https://www.tensorflow.org/) visualization tools.

## Create a Virtual Machine

Click on the 3-line icon on the top left corner of your [Cloud Console](https://console.cloud.google.com), go to **Compute Engine** and **VM instances**. Create a [f1-micro](https://cloud.google.com/compute/pricing#predefined_machine_types) machine with a [Ubuntu](http://realai.org/course/ubuntu/) 16.04 LTS boot image.

![](http://realai.org/course/lab/gce-jupyter-2.png)

Expand the **Management, disks, networking, SSH keys** section at the bottom of the above screenshot, then add the tag of the firewall rule created earlier. Click **Create** to launch this virtual machine.

![](http://realai.org/course/lab/gce-jupyter-3.png)

## Install and Launch Jupyter Notebook

Now the VM instance is running, and on the **VM instances** page it should be assigned an **External IP**, this is the IP address we will later use to access Jupyter Notebook. To install Jupyter, SSH to this VM:

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

## (Optional) Testing Jupyter Notebook with TensorFlow

Install TensorFlow:

```bash
sudo pip3 install tensorflow
```

Now we can [run a short TensorFlow program](https://www.tensorflow.org/install/install_linux#run_a_short_tensorflow_program) in Jupyter Notebook to validate both installations:

![](http://realai.org/course/lab/gce-jupyter-4.png)

## (Optional) Installing Matplotlib

[Matplotlib](https://matplotlib.org/) is a Python 2D plotting library that can be used in the Jupyter Notebook. To install:

```bash
sudo pip3 install matplotlib
```

This package is used in the Reading MNIST Data ([nbviewer](http://nbviewer.jupyter.org/url/realai.org/course/lab/reading-MNIST-data.ipynb), [GitHub](https://github.com/real-ai/realai.org/blob/master/course/lab/reading-MNIST-data.ipynb), [download](http://realai.org/course/lab/reading-MNIST-data.ipynb)) session of [Jupyter Notebook](http://realai.org/course/jupyter/) to plot the image of a handwritten digit.

