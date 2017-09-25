---
permalink: /course/windows/
---
# Windows

Microsoft Windows, or simply [Windows](https://www.microsoft.com/en-us/windows/), is a metafamily of graphical operating systems developed, marketed, and sold by [Microsoft](http://realai.org/industry/microsoft/).

## Windows Subsystem for Linux

[Windows Subsystem for Linux](https://msdn.microsoft.com/en-us/commandline/wsl/about) (WSL) is a compatibility layer included in the Windows 10 anniversary update. It allows Linux executables to run natively on Windows. Linux distributions including [Ubuntu](http://realai.org/course/ubuntu/), OpenSUSE, and SLES now can be obtained from the Windows Store and [installed](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide) onto Windows machine. According to [FAQs](https://msdn.microsoft.com/en-us/commandline/wsl/faq) on [MSDN](https://msdn.microsoft.com/en-us), files on local drives can be accessed from WSL at `/mnt/<drive letter>/`.

In theory, WSL should allow developers to seamlessly move between the Windows and the Linux ecosystems, getting the best of both. But in practice it's never easy to get two complex systems to work well together. There are still rough edges to be smoothed. For example, the legacy blue color of Windows Console is very difficult to read on modern high-contrast display. Newer builds of Windows 10 >= 16257 get a set of better-looking new colors, but a tool to apply it to previous builds has not yet been published [as of August 2, 2017](https://blogs.msdn.microsoft.com/commandline/2017/08/02/updating-the-windows-console-colors/).

## User Account Control

When [user account control](https://docs.microsoft.com/en-us/windows/access-protection/user-account-control/how-user-account-control-works) (UAC) is enabled, the user experience for a standard user is different from that of an administrator. Consistent with the [principle of least privilege](http://realai.org/course/security/#principle-of-least-privilege), everyday work, which normally does not involve modifying the data of the underlying Windows system, should be conducted using a standard user account.

Extending this practice to the scenario where a typically trusted Windows system needs to temporarily operate in an unsafe environment, e.g. through an untrusted WiFi connection, the following steps can be taken to mitigate security risks:

* 1) [Create a system restore point](https://support.microsoft.com/en-hk/help/4027538/windows-create-a-system-restore-point)
* 2) Create a standard user account
* 3) Perform short-term work in an unsafe environment
* 4) Delete the standard user account
* 5) Restore the system

Note that [cloning a user account](https://answers.microsoft.com/en-us/windows/forum/windows_10-start/copying-user-profile-or-cloning-a-user-account/06aac64f-d1d8-4eb9-bea2-7a55a1a6b04f) doesn't seem to be a supported function in Windows 10, therefore every new user account in step 2 needs to be set up from scratch.

