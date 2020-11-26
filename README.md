# Pfeiffer-TPG-261-Readout
Python Script for TPG 261 Readout

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

Just a small script to read out two Pfeiffer TGP 261's. 
As I couldn't get serial readout to work, I instead use the TGP control connector's 2 and 5 pin to read out a 0-10 VDC signal.
These pins are connected to two Keithley Multimeters, which are then read out using RS232. Complete overkill, but it works.

There is also a KEYSIGHT Agilent 53132A connected, which reads out a 6 MHz Quartz crystal via GPIB. The quartz crystal is driven by a MAXTEK-TM400.


Readout is done every second, which in some cases generates a ton of data. [Reduce_size.py](https://github.com/JeroenProoth/Pfeiffer-TPG-261-Readout/blob/main/reduce_size.py) allows you to reduce the file size of the gathered data depending on some error. 
In some cases, you can reduce your filesize by a factor of 100 without losing any significant data. It's very specific to my measurements, but I added it for completeness.

### Built With
* [Python 3.6.4](https://www.python.org/downloads/release/python-364/)


## Getting Started

You will need to install:
* [pyvisa-py](https://pypi.org/project/PyVISA-py/)
* [NI-VISA](https://www.ni.com/nl-be/support/downloads/drivers/download.ni-visa.html#346210)
* [NI-488.2](https://www.ni.com/nl-be/support/downloads/drivers/download.ni-488-2.html#345631), if you intend to use GPIB communication.

## Contact

[![Issues][issues-shield]][issues-url]

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/JeroenProoth/Pfeiffer-TPG-261-Readout.svg?style=for-the-badge
[contributors-url]: https://github.com/JeroenProoth/Pfeiffer-TPG-261-Readout/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JeroenProoth/Pfeiffer-TPG-261-Readout.svg?style=for-the-badge
[forks-url]: https://github.com/JeroenProoth/Pfeiffer-TPG-261-Readout/network/members
[stars-shield]: https://img.shields.io/github/stars/JeroenProoth/Pfeiffer-TPG-261-Readout.svg?style=for-the-badge
[stars-url]: https://github.com/JeroenProoth/Pfeiffer-TPG-261-Readout/stargazers
[issues-shield]: https://img.shields.io/github/issues/JeroenProoth/Pfeiffer-TPG-261-Readout.svg?style=for-the-badge
[issues-url]: https://github.com/JeroenProoth/Pfeiffer-TPG-261-Readout/issues


