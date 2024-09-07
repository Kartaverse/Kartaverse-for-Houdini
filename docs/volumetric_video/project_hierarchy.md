# Project Hierarchy

## Generic Houdini VolCap Project Folder Hierarchy:

* $HIP/abc/  
* $HIP/audio/  
* $HIP/comp/  
* $HIP/desk/  
* $HIP/dxo/texture/  
* $HIP/dxo/reconstruction/  
* $HIP/e57/  
* $HIP/flip/  
* $HIP/geo/  
* $HIP/hda/  
* $HIP/images/\#\#\#\#/  
* $HIP/images/\#\#\#\#/texture/  
* $HIP/images/\#\#\#\#/reconstruction/  
* $HIP/logs/  
* $HIP/metadata/  
* $HIP/metadata/xmp/  
* $HIP/obj/  
* $HIP/render/  
* $HIP/scripts/  
* $HIP/screenshots/  
* $HIP/tex/  
* $HIP/video/  
* $HIP/zip/


Note: Houdini uses "$HIP" as a token/environment variable. It's a quick way to express a relative file path that is the parent folder to the currently open Houdini scene/project.

Note: The symbols "\#\#\#\#" represent the image sequence frame number.

## Metadata Folder Hierarchy

* $HIP/metadata/xmp/  
* $HIP/metadata/obj\_model\_export\_params.xml  
* $HIP/metadata/xyz\_model\_export\_params.xml  
* $HIP/metadata/rec\_region.rcbox

The "rec\_region.rcbox" file is the Reality Capture exported reconstruction region cropping box file. This allows you to trim the model to retain the geometry that exists within the bounding box region you define.

The "obj\_model\_export\_params.xml" file is saved from the Reality Capture GUI. It is the export settings used to define the mesh and texture generation parameters used.

The "xyz\_model\_export\_params.xml" file is saved from the Reality Capture GUI. It is the export settings used to define the point cloud and per-point sample color generation parameters used.

Note: Houdini uses "$HIP" as a token/environment variable. It's a quick way to express a relative file path that is the parent folder to the currently open Houdini scene/project.

Note: The symbols "\#\#\#\#" represent the image sequence frame number.

## "Frameset" Per-Frame Folder for Reality Capture CLI:

The Reality Capture CLI (command-line) program can be used to process multi-view imagery from a volumetric video camera rig. This is most flexibly done by having FFmpeg process individual takes to extract each of the camera view's recorded video clips into image sequences.

A collection of per-timeline frame based "frameset" folders are then used to hold the camera view images. Each of the frameset folders represent a single moment in time. 

What this means in practice, is the image sequence based media is split apart and stored in numbered sub-folders in the images directory with a pre-frame folder name like "0001", "0002", "0003", etc.

The media from a multi-view rig that captured a 144 frame duration sequence with 50 camera views would then be placed into a folder hierarchy named like this:

* $HIP/images/\[0001-0144\]/texture/Camera.\[0001-0050\].tif

To support this workflow, the following folder structure is created inside the Houdini project folder:

Starting Folder Contents:

* $HIP/images/\[\#\#\#\#\]/  
* $HIP/images/\[\#\#\#\#\]/texture/  
* $HIP/images/\[\#\#\#\#\]/reconstruction/

After Reality Capture CLI Finishes Folder Contents:

* $HIP/images/\[\#\#\#\#\]/mesh\_u1\_v1.png  
* $HIP/images/\[\#\#\#\#\]/mesh.xyz  
* $HIP/images/\[\#\#\#\#\]/mesh.e57  
* $HIP/images/\[\#\#\#\#\]/mesh.abc  
* $HIP/images/\[\#\#\#\#\]/mesh.obj  
* $HIP/images/\[\#\#\#\#\]/mesh.mtl  
* $HIP/images/\[\#\#\#\#\]/project\_align.rcproj  
* $HIP/images/\[\#\#\#\#\]/project\_align/  
* $HIP/images/\[\#\#\#\#\]/project\_obj.rcproj  
* $HIP/images/\[\#\#\#\#\]/project\_obj/  
* $HIP/images/\[\#\#\#\#\]/project\_xyz.rcproj  
* $HIP/images/\[\#\#\#\#\]/project\_xyz/  
* $HIP/images/\[\#\#\#\#\]/texture/CAM\[1-200\].xml  
* $HIP/images/\[\#\#\#\#\]/texture/CAM\[1-200\].tif  
* $HIP/images/\[\#\#\#\#\]/reconstruction  
* $HIP/images/\[\#\#\#\#\]/metadata/xyz\_model\_export\_params.xml  
* $HIP/images/\[\#\#\#\#\]/metadata/obj\_model\_export\_params.xml  
* $HIP/images/\[\#\#\#\#\]/metadata/rec\_region.rcbox

Note: The symbols "\#\#\#\#" represent the image sequence frame number.

## Volumetric Video Output Hierarchy:

A folder is used to hold the flat mesh-sequence outputs which allows for easier media playback by 3D DCC packages and game engines:

* $HIP/obj/mesh.\#\#\#\#.obj  
* $HIP/obj/mesh.\#\#\#\#.mtl  
* $HIP/obj/mesh\_u1\_v1.\#\#\#\#.png  
* $HIP/obj/mesh\_u1\_v1.\#\#\#\#.exr

Note: Houdini uses "$HIP" as a token/environment variable. It's a quick way to express a relative file path that is the parent folder to the currently open Houdini scene/project.

Note: The symbols "\#\#\#\#" represent the image sequence frame number.

Note: Houdini uses "$HIP" as a token/environment variable. It's a quick way to express a relative file path that is the parent folder to the currently open Houdini scene/project.