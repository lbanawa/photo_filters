# Intro:
The photo filters application takes images from a specified input folder, applies a filter chosen by the user (choices are "gray" and "sepia"), and outputs filtered images to a specified output folder.

# Installation (conda):
```bash
    conda create --name photo_filters python=3.7 -y
    conda activate photo_filters
    pip install -r requirements.txt
```

# Examples:
By default, the run.py function will take photos from an input folder:
```
photo_filters
│   README.md
│   run.py    
│
└─── input
│   │   photo1.jpg
│   │   photo2.png
│   │   ..
└─── ...
```

and apply a default filter (black and white) to all images in input, then output the filtered photos in a default output folder. The run.py command can be run with default parameters like:
```bash
python run.py
```




If you would like to run photo_filters with non-default settings, the proper for run.py is:
```bash
python run.py -i <input> -o <output> -f <filter>
```

current valid filter types are:
* gray
* sepia

