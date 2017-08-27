---
permalink: /course/google-compute-engine/
redirect_from: /course/GCE/
---
# Google Compute Engine

[Google Compute Engine](https://cloud.google.com/compute/) (GCE) is a [Google Cloud](https://cloud.google.com/) service that delivers scalable, high-performance virtual machines (VMs). It charges for usage based on a [pricing sheet](https://cloud.google.com/compute/pricing) but also offers a [free-trial](https://cloud.google.com/free/docs/frequently-asked-questions) for new customers. After sign-up, users will be able to manage [VM instances](https://console.cloud.google.com/compute/instances) of different machine types. These machine types typically have 1 to 64 virtual CPUs, 3.75 to 240GB memory and are charged at different rates. Each instance requires a disk to boot from. For example, a 10GB boot disk image can be chosen for a VM to run Ubuntu 16.04 [LTS](https://wiki.ubuntu.com/LTS). Virtual machines can be used for many purposes other than AI research. For those interested, a trading algorithm can be hosted in just [6 easy steps](https://robotwealth.com/run-trading-algorithms-google-cloud-platform-6-easy-steps/), as of July 2017.

## Cloud Shell

[Cloud Shell](https://cloud.google.com/shell/) ([documentation](https://cloud.google.com/shell/docs/)) is a [free](https://cloud.google.com/shell/pricing) shell environment for managing cloud resources. [No SLA applies](https://cloud.google.com/shell/sla) to this service. It enables access to the Cloud SDK [`gcloud`](https://cloud.google.com/sdk/gcloud/) tool directly from browser. Cloud Shell’s [features](https://cloud.google.com/shell/docs/features) include a 5GB free persistent disk storage, and when Cloud Shell is started, it provisions a f1-micro virtual machine instance running Debian. Cloud Shell is intended for [interactive use only](https://cloud.google.com/shell/docs/limitations). Prolonged usage is not supported and may result in session termination without a warning.

## Lab Sessions

* [Using Remote Desktop to NetSurf on Xfce4 via Xrdp](http://realai.org/course/lab/rdp-netsurf-xfce4/)
* [Running Jupyter](http://realai.org/course/tensorflow/jupyter-gce/)
* [Neural Machine Translation on Cloud GPU](http://realai.org/course/lab/gpu-tf-nmt/)

