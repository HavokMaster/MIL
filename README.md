# Master's Image Loader
A Custom Image Loader for AI/ML purposes that I wrote because why not!

# Usage:

* Use `loadImages` function to load all images from a folder.

* The `imageDir` specifies which folder will be searched for images. By default it is set to "images/".

* `size` can be specified as a tuple to resize all images during loading itself.

* `serialize` can be set to True to store loaded images in a pickle format in a dumpfile of the name `dumpName` that is by default "images.pkl"

* `bgr2rgb` can be set to True to convert to RGB format as this loader uses OpenCV to read images which are in BGR format.

* `loadFromDump` loads the images from a dump file, by default it loads from "images.pkl"

* `getClasses` returns list of all classes which can be used to refer the labels.
