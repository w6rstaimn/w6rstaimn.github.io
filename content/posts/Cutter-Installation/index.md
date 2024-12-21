---
title: "Cutter Installation"
summary: "Cutter is an advanced, user-friendly reverse engineering platform powered by Rizin. If you're looking to install Cutter on your Linux system, follow these simple steps."
date: 2024-12-18
draft: false
description: "a description"
tags: ["example", "tag"]
---
 

# How to Install Cutter: A Quick Guide

Cutter is an advanced, user-friendly reverse engineering platform powered by Rizin. If you're looking to install Cutter on your Linux system, follow these simple steps:

### Download Cutter
First, download the latest version of Cutter from its official GitHub repository. For this guide, we'll use Cutter-v2.3.4-Linux-x86_64.AppImage:

Cutter Link : [Get Cutter | Cutter](https://github.com/rizinorg/cutter/releases/tag/v2.3.4)

![](Download-Cutter.png#center)



### Move the Downloaded File
Once the download is complete, the Cutter AppImage will be in your Downloads folder by default. Move the file to a system-wide location for easier access

Run the following command to check your current PATH environment variable:

```mmd
echo $PATH
```
![](echopath.png#center)

### Move the AppImage to a Directory in Your PATH

Use the following command to move the downloaded Cutter AppImage to `/usr/local/bin`,a directory typically included in the PATH:

```mmd
sudo mv ~/Downloads/Cutter-v2.3.4-Linux-x86_64.AppImage /usr/local/bin
```
![](move.png#center)

Explanation:

- **[sudo]()**: Grants administrative privileges required to move files into system directories like /usr/local/bin.

- **[mv]()**: Moves the specified file from one location to another. In this case, the Cutter AppImage is moved from the Downloads folder to `/usr/local/bin`.

### Make Cutter Executable
Next, you'll need to give the file executable permissions to run it

Run the following command to make the Cutter AppImage executable:

```mmd
chmod +x /usr/local/bin/Cutter-v2.3.4-Linux-x86_64.AppImage
```
![](chmod.png#center)

Explanation:

- **[chmod]()**: Changes the file permissions of a specified file.

- **[+x]()**: Adds execute permissions, allowing the file to be run as a program.

### Conclusion
You now have Cutter installed and ready to use on your Linux system! This reverse engineering tool can help you dive deep into binaries and analyze programs effectively. Happy reverse engineering! 😊


### Run Cutter
After making the file executable, you can launch Cutter directly from the terminal and click OK

```mmd
Cutter-v2.3.4-Linux-x86_64.AppImage chall&
```
![](run.png#center)

Explanation:

- **[Cutter-v2.3.4-Linux-x86_64.AppImage]()**: This runs the Cutter application.

- **[chall]()**: The name of the binary file you want to analyze. Replace chall with the actual filename of your binary.

- **[&]()**: Runs the command in the background, allowing you to continue using the terminal for other tasks while Cutter is open.


{{< alert icon="linux" cardColor="#53659A" iconColor="#1d3557" textColor="#f1faee" >}}
Tip, you can also use the Tab key for auto-completion to quickly type the file name in the terminal. Alternatively, consider creating an alias or adding it to your application menu.
{{< /alert >}}


### Configuring Cutter

Once Cutter is running, follow these steps to configure it for optimal usage:

Enable Console, Comments & Section

Go to the Windows menu.

Tick the Console,Comments & checkbox to enable it. This will display inline comments in the disassembly view, providing useful insights during reverse engineering.

Navigate to Info and tick the Sections checkbox. This will show detailed information about the binary’s sections, such as .text and .data.

![](concomsec.png#center)


Now rearrange the sections window by click and hold the title bar and drag it to somewhere else.

![](sections.gif#center)

### Customize Appearance

Go to the Edit menu.

Select Appearance.

Choose your preferred theme to personalize Cutter’s interface.

![](appearance.png#center)

### Enable All References in Disassembly View

Go to the Disassembly menu.

Tick all available reference options. This will display all cross-references, making it easier to analyze the flow of the binary.

![](ref2.png#center)
![](ref.png#center)

#### From this
![](fromthis.png#center)

#### To this
![](tothis.png#center)

### Conclusion

By following these steps, you’ve successfully installed and configured Cutter on your Linux system. Cutter’s powerful features, combined with a user-friendly GUI, make it an excellent tool for reverse engineering. Happy exploring!