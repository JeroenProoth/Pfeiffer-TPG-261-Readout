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
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

Just a small script to readout two Pfeiffer TGP 261's. 
As I couldn't get serial readout to work, I instead use the TGP control connector's 2 and 5 pin to readout a 0-10 VDC signal.
These pints are connected to two Keithley Multimeters, which are then read out using RS232. Complete overkill, but it works.

There is also a KEYSIGHT Agilent 53132A connected, which reads out a 6 MHz Quartz crystal via GPIB. The quartz crystal is driven by a MAXTEK-TM400.

### Built With
* [Python 3.6.4](https://www.python.org/downloads/release/python-364/)


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


