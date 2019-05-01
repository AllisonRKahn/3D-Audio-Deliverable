# Marvelmind Localization Beacons
Type: HW v4.9 915 MHz with IMU

## Operating Manual
[Marvelmind Operating Manual](https://marvelmind.com/pics/marvelmind_navigation_system_manual.pdf)

## Download Marvelmind Dashboard Desktop Application
Download [latest stable software](https://marvelmind.com/download/).
Find the .exe file and follow the instructions to download.

---

## Basic Setup (Updating Software & Using the Dashboard):
1. One (1) USB to micro-USB cord
2. Marvelmind beacons & modem
3. Marvelmind Dashboard Desktop Application
4. Pin

###### Instructions:
1. Open Marvelmind Dashboard Desktop Application
2. Turn on all beacons using the pin to push the node toward the "KE". Do not toggle the other button towards the "ON."
3. Connect modem to computer with USB to micro-USB cable
4. Make sure that the map is not frozen. If it is frozen, unfreeze the map.
5. Wait for all red boxes in the table of distances to disappear. If red boxes do not disappear, beacons cannot see each other. Move them so that they can communicate.
6. If table of distances is not visible, click **Submap 0** and the table of distances will appear.
7. When you are done, make sure to turn off all beacons.

---

## Project Setup (Server/Client & Access values within code):
1. Two (2) computers or one (1) computer and one (1) Raspberry Pi:
   - one to connect the modem to the computer (server)
   - one to connect the hedgehog
2. Two (2) USB to micro-USB cords
3. Marvelmind beacons & modem
4. Marvelmind Dashboard Desktop Application
5. Pin

###### Instructions:
1. Open Marvelmind Dashboard Desktop Application
2. Turn on all beacons using the pin to push the node toward the "KE". Do not toggle the other button towards the "ON."
3. Connect modem to the computer running Dashboard with USB to micro-USB cable.
4. Make sure that the map is not frozen. If it is frozen, unfreeze the map.
5. Wait for all red boxes in the table of distances to disappear. If red boxes do not disappear, beacons cannot see each other. Move them so that they can communicate.
6. If table of distances is not visible, click **Submap 0** and the table of distances will appear.
7. Connect the hedgehog to the second computer / Raspberry Pi using the USB to micro-USB cable.
8. Edit the files from GitHub. Need to change the tty port in all files to the one that you are using. On a Mac, open Terminal and run
```
ls /dev
```
Find the port number that looks different from the rest. It should look like:
- /dev/ttyACM0 - typical for Linux
- /dev/tty.usbmodem1451 - typical for Mac OS X
9. Run the program.
7. When you are done, make sure to turn off all beacons.

---

## How to Update
Download [latest stable software](https://marvelmind.com/download/).

From the menu, click:
**Firmware**
**Open File**
Locate the latest stable software that you just downloaded to your computer.
Make sure to use HW v4.9 915 MHz software (HEX file extension).
For example, the February 21, 2019 release
Find the folder and open it:
```
hw49_firmware
```
Depending on what you are updated choose the correct HEX file. If you are updating the modem, choose the HEX that has modem in the name along with the correct frequency; for example,
```
2018_09_25_modem_hw49_sw5_96_rd915MHz_d072e1d.hex
```
For the beacons again use the correct frequency and version:
```
2018_09_25_beacon_hw49_sw5_96_rd915MHz_934208f.hex
```
Click the **Default** button on the right side of the dashboard. This resets all the devices back to the default state (makes sure that the beacon is not on the wrong channel).
At the top of that column click **Write all**.
Disconnect that device and repeat with the rest of the beacons/modem.

---

## Distances Table Not Displaying
If the distances are not showing up, then click **Submap 0** located in the bottom left corner of the map.
