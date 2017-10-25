---
permalink: /course/google-cloud-platform/
redirect_from: /course/GCP/
---

# Google Cloud Platform

[Cloud](https://en.wikipedia.org/wiki/Cloud_computing) is an IT infrastructure that offers a range of computing services to its users. [Google Cloud Platform](https://cloud.google.com/) (GCP) is the public cloud offered by Google. It consists of a set of physical assets, such as computers and hard disk drives, [around the globe](https://cloud.google.com/about/locations/). Commonly used GCP [services](https://cloud.google.com/docs/overview/cloud-platform-services) include computing & hosting, storage, networking, and big data. [Local currency billing and payments](https://support.google.com/cloud/answer/6224682) are available for many countries and regions.

## Cloud Shell

[Cloud Shell](https://cloud.google.com/shell/) ([documentation](https://cloud.google.com/shell/docs/)) is a [free](https://cloud.google.com/shell/pricing) shell environment for managing cloud resources. [No SLA applies](https://cloud.google.com/shell/sla) to this service. It enables access to the Cloud SDK [`gcloud`](https://cloud.google.com/sdk/gcloud/) tool directly from browser. Cloud Shell’s [features](https://cloud.google.com/shell/docs/features) include a 5GB free persistent disk storage, and when Cloud Shell is started, it provisions a f1-micro virtual machine instance running Debian. Cloud Shell is intended for [interactive use only](https://cloud.google.com/shell/docs/limitations). Prolonged usage is not supported and may result in session termination without a warning.

Cloud Shell can be used to quickly move small files between virtual machine instances with the following command:

* [`gcloud compute scp`](https://cloud.google.com/sdk/gcloud/reference/compute/scp) - copy files to and from Google Compute Engine virtual machines via scp

It can automatically generate ssh keys to access instances, and copy files to and from the disk space in Cloud Shell. Remove the copied file and `.ssh` directory restores Cloud Shell to its original state. Larger files need to be [transferred through Cloud Storage](https://cloud.google.com/compute/docs/instances/transfer-files#gcstransfer).

## Google Compute Engine

[Google Compute Engine](https://cloud.google.com/compute/) (GCE) is a GCP service that delivers scalable, high-performance virtual machines (VMs). It charges for usage based on a [pricing sheet](https://cloud.google.com/compute/pricing) but also offers a [free-trial](https://cloud.google.com/free/docs/frequently-asked-questions) for new customers. After sign-up, users will be able to manage [VM instances](https://console.cloud.google.com/compute/instances) of different machine types. These machine types typically have 1 to 64 virtual CPUs, 3.75 to 240 GB memory and are charged at different rates. Each instance requires a disk to boot from. For example, a 10 GB boot disk image can be chosen for a VM to run Ubuntu 16.04 [LTS](https://wiki.ubuntu.com/LTS). Virtual machines can be used for many purposes other than AI research. For those interested, a trading algorithm can be hosted in just [6 easy steps](https://robotwealth.com/run-trading-algorithms-google-cloud-platform-6-easy-steps/), as of July 2017.

### Lab Sessions

* [Firefox on Remote Desktop](http://realai.org/course/google-cloud-platform/firefox-on-remote-desktop/)
* [TensorFlow](http://realai.org/course/tensorflow/) > [Running TensorFlow in Jupyter on Google Compute Engine](http://realai.org/course/tensorflow/jupyter-gce/)
* [Neural Machine Translation on Cloud GPU](http://realai.org/course/google-cloud-platform/gce-gpu-nmt/)
* [Running StarCraft II Learning Environment on Google Compute Engine](http://realai.org/course/google-cloud-platform/gce-sc2le/)

## Other Products

[Colaboratory](https://colab.research.google.com) is a research project created to help disseminate machine learning education and research. It's a Jupyter notebook environment that requires no setup to use. Unlike [Cloud Datalab](https://cloud.google.com/datalab/), it is not a fully supported or generally-available Google product.

## Resources

* Links: [Medium](https://medium.com/google-cloud)

## Comparisons

Cloud computing is a major focus of the AI [industry](http://realai.org/industry/#cloud-computing). Other notable cloud service platforms include [Amazon Web Services](https://aws.amazon.com/) and [Microsoft Azure](https://azure.microsoft.com/).

* 2017 June 6. [Google Cloud Platform Vs. Amazon Web Services](https://dev.to/bugfenderapp/google-cloud-platform-vs-amazon-web-services). *dev.to*.
* 2017 March 14. [A Tale of Two Clouds: Amazon vs. Google](https://medium.com/@robaboukhalil/a-tale-of-two-clouds-amazon-vs-google-4f2520516a38). *Medium*.

