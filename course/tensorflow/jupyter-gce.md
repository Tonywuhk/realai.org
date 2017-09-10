---
permalink: /course/tensorflow/jupyter-gce/
title: Course | TensorFlow | Running TensorFlow in Jupyter on Google Compute Engine
---
[Home](http://realai.org/) > [Course](http://realai.org/course/)

* &gt; [Google Cloud Platform](http://realai.org/course/google-cloud-platform/) > [Google Compute Engine](http://realai.org/course/google-cloud-platform/#google-compute-engine) >
* &gt; [Jupyter Notebook](http://realai.org/course/jupyter/) >

# Running TensorFlow in Jupyter on Google Compute Engine

*Last Updated: August 27, 2017*

It is very easy to run [TensorFlow](http://realai.org/course/tensorflow/) in a Jupyter Notebook on the cloud. We first need to create two [firewall rules](https://cloud.google.com/compute/docs/vpc/firewalls) on the Google Cloud Platform to allow web access to TensorBoard and Jupyter Notebook, then we create a [virtual machine](https://cloud.google.com/compute/) (VM) instance subject to these rules. After several bash commands to set up TensorFlow and Jupyter Notebook, we'll be ready to test our environment on the web.

## Create Firewall Rules

Click on the 3-line icon on the top left corner of [cloud console](https://console.cloud.google.com/), go to *VPC Network* and *Firewall rules*, then click *CREATE FIREWALL RULE*. Here we name the rule `jupyter` and use the same name as the *Target tag*. To allow incoming traffic from all over the Internet, we set *Source IP range* to be *0.0.0.0/0* ([CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation)), and *Specified protocal and port* to be `tcp:8888`, the default port to be used by Jupyter Notebook. Click *Create* to add this rule.

![](http://realai.org/course/tensorflow/jupyter-gce-1.png)

Now follow the same steps above to create a rule `tensorboard` for port `tcp:6006`. [TensorBoard](https://www.tensorflow.org/get_started/summaries_and_tensorboard) is a suite of TensorFlow visualization tools.

## Create a Virtual Machine

Click on the 3-line icon on the top left corner of your [Cloud Console](https://console.cloud.google.com), go to *Compute Engine* and *VM instances*. Create an [n1-standard-1](https://cloud.google.com/compute/pricing#predefined_machine_types) instance with a [Ubuntu](http://realai.org/course/ubuntu/) 16.04 LTS boot image.

![](http://realai.org/course/tensorflow/jupyter-gce-2.png)

Expand the *Management, disks, networking, SSH keys* section at the bottom of the above screenshot, then add the tag of the firewall rules created earlier. Click *Create* to launch this VM.

![](http://realai.org/course/tensorflow/jupyter-gce-3.png)

## Install TensorFlow and Jupyter Notebook

Now the VM instance is running, and on the *VM instances* page it should be assigned an *External IP*, this is the IP address we will later use to access TensorBoard and Jupyter Notebook. We will use [pip](http://realai.org/course/pip/) to install TensorFlow and Jupyter Notebook. *SSH* to this VM, then enter the following commands:

```bash
curl https://bootstrap.pypa.io/get-pip.py | sudo python3 -
sudo pip install tensorflow jupyter
```

The first line downloads a pip installation script, passes it to [Python 3](http://realai.org/course/python/), which runs the script to install pip. In the second line, pip is [run with the superuser privileges](https://en.wikipedia.org/wiki/Sudo) to install TensorFlow and Jupyter Notebook.

There is a command we need to issue every time to launch Jupyter Notebook. If this VM is mainly used for practicing with Jupyter Notebook, we can add the command to the *.bashrc* [startup file](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html) by entering the following in our terminal:

```bash
echo >> .bashrc
echo "# Start Jupyter Notebook" >> .bashrc
echo "jupyter notebook --ip=0.0.0.0 &" >> .bashrc
```

Jupyter Notebook should start automatically next time we SSH to this VM. That's it, the setup is complete! Type `source .bashrc` to run our new *.bashrc* without leaving this terminal. Jupyter Notebook should be live on the web at `http://<External IP>:8888`. Access token can be found in the terminal. To exit Jupyter, type `ps` and [kill](https://ss64.com/bash/kill.html) it by [process ID](https://en.wikipedia.org/wiki/Process_identifier).

## Testing

We can [run a short TensorFlow program](https://www.tensorflow.org/install/install_linux#run_a_short_tensorflow_program) in Jupyter Notebook to validate both installations:

![](http://realai.org/course/tensorflow/jupyter-gce-4.png)

The first line [imports](https://docs.python.org/3.5/reference/import.html) TensorFlow as a Python [module](https://docs.python.org/3.5/tutorial/modules.html). The second line creates a constant tensor, which forms a simple computation graph with just one node. The third line initiates a session. In the final line, the session runs the constant to obtain its value.

## (Optional) Installing Matplotlib

[Matplotlib](https://matplotlib.org/) is a Python 2D plotting library that can be used in the Jupyter Notebook. To install:

```bash
sudo pip install matplotlib
```

This package is used in the Reading MNIST Data ([nbviewer](http://nbviewer.jupyter.org/url/realai.org/course/lab/reading-MNIST-data.ipynb), [GitHub](https://github.com/real-ai/realai.org/blob/master/course/lab/reading-MNIST-data.ipynb), [download](http://realai.org/course/lab/reading-MNIST-data.ipynb)) session of [Jupyter Notebook](http://realai.org/course/jupyter/) to plot the image of a handwritten digit.

