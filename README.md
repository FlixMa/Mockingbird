# Mockingbird

## TL;DR - Key Features

- Uses Photoshop documents
- Supports Bulk-Edit
- Supports single and multi-frame mockups
- Supports transparency
- Supports resizing (aspect fit)
- Supports Multicore Systems


## The Long Story

This tool helps you to embed your app screenshots inside Apples device mockups.
Because the script reads the original photoshop documents Apple provides within their marketing guidelines, there is no need to wait for updates of the library after new product releases.
Multi-Frame Mockups, e.g. one containing iPad and iPhone, are supported.


### Prerequisites

- Python 3
- OpenCV 4 (might work with lower versions)
- psd-tools (can be installed from pip)


### Instructions

Your screenshots need to be organized into folders.
Each folder represents one device and contains the screenshots for every feature you wish to showcase.
The folders are specified using the `--screenshots` parameter.
Concerning the layers of the photoshop document, the folders should be given from background to foreground.

You might also want to have a look at the usage message `python3 mockingbird.py --help`

#### Single-Frame mockups:

`python3 mockingbird.py --frame ./iphone_11.psd --screenshots ./iphone11`


#### Multi-Frame mockups:

`python3 mockingbird.py --frame ./ipad_iphone.psd --screenshots ./ipad129inch ./iphone11`

This command uses the dual-device psd file and combines it with the images from `./ipad129inch` in the background device and `./iphone11` in the foreground device.
