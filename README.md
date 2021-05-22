PIFU-HD is a great library for 3D model reconstruction from 2D image.
Source: https://shunsukesaito.github.io/PIFuHD/

The code is for a simple flask application (with ui) where in you can upload a 2D image (front facing is preferred)
and get the 3D model (.obj file), mp4 and uv image file.

I have included the pifu library as well in the code since flask application is directly calling the PIFU library methods.
There are some minor modifications in the code which were made to enable the library to run on my system.
Download pifu library from here https://github.com/facebookresearch/pifuhd and paste in this repository do not replace already existing folders of pifu library from this repository.
The requirements for installation of PiFu library are mentioned in requirements.txt.
Note: Requirements
1. Opengl requirement should be downloaded directly and installed rather than installing using pip.
2. ffmpeg - I tried installing using pip but the pifu code utilizes the executable rather than importing the ffmpeg library and using that. Download the ffpmeg library externally and place it in this repository folder.
