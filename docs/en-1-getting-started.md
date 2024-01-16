# Polideuces 01 - Getting Started

>[Acesse este guia em português / Access this guide in Portuguese](/docs/pt-1-comecando.md)

## Table of Contents

1. [Setup](#setup)
	- [Setup the Raspbberry Pi](#setup-the-raspberry-pi)
	- [Setup Your Machine](#setup-your-machine)
2. [Building the Robot](#building-the-robot)
	- [List of Components](#list-of-components)
	- [Putting Everything Together](#putting-everything-together)
3. [Running the Robot](#running-the-robot)

## Setup

- [ ] TODO: Add reminder to use the Google Translate extension to view english links in Portuguese if needed.

### Setup the Raspberry Pi

1. Sign up for a free [Viam account](https://www.viam.com/).

2. Setup your Raspberry Pi following [Viam's Setup Guide](https://docs.viam.com/get-started/installation/prepare/rpi-setup/)
	- If you're going to use a different board, you should follow [Viam's Setup Guide to your specific board](https://docs.viam.com/), if supported.

3. If you haven't already done it after Viam's setup guide, go to the [Viam app](https://app.viam.com/) and add a new machine by providing a name in the "New machine" field and clicking "Add machine".
	- On the "Setup" tab, select `Linux (Aarch64)` or `Linux (x86_64)` for the appropriate architecture for your computer. Raspberry Pi's are `Linux (Aarch64)`, but you can confirm it by running `uname -m`.
	- Follow the steps shown on the "Setup" tab to install `viam-server` on your Raspberry Pi and wait for confirmation that your computer has successfully connected. 
	- By default, `viam-server` will start automatically when your system boots, but you can [change this behavior](https://docs.viam.com/get-started/installation/manage/) if desired.

4. On the [Viam app](https://app.viam.com/), select your newly created robot and navigate to the "Config" tab. Select the "Raw JSON" mode and copy and paste the contents of `src/polideuces/configs/polideuces-01.json` there.
	- Feel free to change any details of the configurations as you see fit. Just beware to also change it in your electronics and in the `src/polideuces/configs/polideuces-01.json` file so that the scripts can work properly.

### Setup Your Machine

>Make sure you have Python 3 with `pip` and `virtualenv` installed in your machine. You can learn more at:
>- [Download Python - Python.org](https://www.python.org/downloads/)
>- [Python 3 Installation & Setup Guide – Real Python](https://realpython.com/installing-python/)

1. Clone or download this repository with:

```
git clone git@github.com:EEmery/polideuces-01.git
```

You can alternatively click the green "Code" button at the top right hand corner and select "Download ZIP".

2. In your terminal, navigate to the root of the repository folder, then create a new environment and activate it with:

```
python3 -m venv .venv && source .venv/bin/activate
```

3. Install the dependencies with:

```
python3 -m pip install -r requirements/prod.txt
```

4. Add the credentials to your robot in the repository by creating a file called `credentials.jon` in `src/polideuces/secrets/`. The `credentials.json` file should look something like this:

```
{
    "name": "your-robot-name",
    "address": "your-robot-address",
    "credential": "your-credential"
}
```

You can find the robot address in the "Code sample" tab of your Robot's [Viam app](https://app.viam.com/robots). It will look something like:

```python
async def connect():
    opts = RobotClient.Options.with_api_key(
	  # Replace "<API-KEY>" (including brackets) with your machine's api key
      api_key='<API-KEY>',
	  # Replace "<API-KEY-ID>" (including brackets) with your machine's api key id
      api_key_id='<API-KEY-ID>'
    )
    return await RobotClient.at_address('your-robot-address', opts)
```

You can find the credential in your [robots page in the Viam app](https://app.viam.com/robots). There will be a section at the bottom called "Secret Keys". If there is none, click the "Generate key" button. Copy and paste it to you `credentials.json` file.

>WARNING: Make sure to never share or post online your credentials.

## Building the Robot

### List of Components

Take the list of components bellow as a suggestion of parts necessary, but feel free to change them as you see fit. Just make sure to update the code and electronic connections as necessary.

**Actuators**
- 2x Hobby DC Motors with reduction gears and wheels
- 1x DC Motor Driver - L298N

**Sensors**
- 1x Webcam - Logitech C270 720p/30fps HD Webcam with Embedded Microfone
- 1x Accelerometer - ADLX345
- 1x Distance sensor - LV Maxsonar EZ

**Brains**
- Raspberry Pi 3 Model B
- Wire jumpers of multiple sizes (femele-to-female and male-to-female)

**Power Supply**
- 4x 18265 Batteries
- 1x 18265 Batteries Holder
- 1x DC-DC Step Down Converter - Mini560 (7-20V to 5V)
- 1x DC-DC Boost Converter - MT3608 (2V-9V to 5V)
- 1x Power Switch

**Frame**
- M2.5 Screws and nuts
    - Of assorted sizes, but mostly varying approximately from 4mm to 10mm
- M3 Screws and nuts
	- Only for connecting the DC motors to the frame, must be at least 23mm long
- 3D Printed Parts:
    - 1x [Skeleton](/models/Skeleton.stl)
    - 1x [Third Feet](/models/Third%20feet.stl)
    - 1x [Battery Holder](/models/Battery%20Holder.stl)
    - 1x [Sensors Array](/models/Sensors%20Array.stl) (if you decide to print the optional parts, the sensors array become unecessary)
- Optional 3D Printed Parts:
    - 1x [Shell - Mask](/models/Shell%20-%20Mask.stl)
    - 1x [Shell - Top](/models/Shell%20-%20Top.stl)
    - 2x [Shell - Left Side](/models/Shell%20-%20Left%20Side.stl) (you can mirror the STL file before printing to get the right side of the shell)
    - 2x [Shell - Wheel Cap](/models/Shell%20-%20Wheel%20Cap.stl)
- Feel free to check the [Onshape Project](https://cad.onshape.com/documents/57eca4cfdd989f9be606e886/w/89188582492a65a69131f629/e/66d103aafa7007a6db980672?renderMode=0&uiState=659c2bd2daef495b2a084473) for all the 3D printed parts.

### Putting Everything Together

>You can follow along the video guide at:
- [ ] TODO: Add link to video

**Electronics Schematics**

The full wiring of the electronic components should looke something like:

![electronic-schematics](/docs/images/electronics-schematic.png)

### Running the Robot

To run the robot, make sure:
- Your xbox gamepad is turned on and connected to your computer
- The robot is turned on anc connected to the internet

Then simply run:

```
$python3 src/polideuces/controllers/remote_control.py
```
