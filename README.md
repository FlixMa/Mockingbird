# Mockingbird

## TL;DR - Key Features

- Uses Photoshop documents
- Supports Bulk-Edit
- Supports single and multi-frame mockups
- Supports transparency
- Supports resizing (aspect fit)
- Supports Multicore Systems

<img src="https://github.com/FlixMa/Mockingbird/raw/master/assets/ipad129_iphone11.png" width="100%">

## The Long Story

This tool helps you to embed your app screenshots inside Apples device mockups.
Because the script reads the original photoshop documents Apple provides within their marketing guidelines, there is no need to wait for updates of the library after new product releases.
Multi-Frame Mockups, e.g. one containing iPad and iPhone, are supported.


### Installation

The only prerequisite is Python 3.6 or higher. On macOS its comfy to install it via homebrew, i.e. `brew install python3`.
To install mockingbird, use `pip3 install mockingbird-psd`.


### Instructions

Your screenshots need to be organized into folders.
Each folder represents one device and contains the screenshots for every feature you wish to showcase.
The folders are specified using the `--screenshots` parameter.
Concerning the layers of the photoshop document, the folders should be given from background to foreground.

You might also want to have a look at the usage message `mockingbird --help`

#### Single-Frame mockups:

`mockingbird --frame ./iphone_11.psd --screenshots ./iphone11`


#### Multi-Frame mockups:

`mockingbird --frame ./ipad_iphone.psd --screenshots ./ipad129inch ./iphone11`

This command uses the dual-device psd file and combines it with the images from `./ipad129inch` in the background device and `./iphone11` in the foreground device.
