# Preparing XR Stage Deliverables

So far we have covered Houdini TOPs usage concepts and automated common videogrammetry reconstruction tasks.

We might want to further post-process the volumetric video data to generate an OpenUSD "Clip" (.usda) file that links to Alembic (.abc) per-frame mesh sequences with OpenEXR (.exr) DWAA compressed linear gamma 1.0 per-frame texture maps. 

This is one of the deliverable asset types that VFX artists who work with DCC packages like Autodesk Maya, Autodesk 3dsMax, SideFX Houdini, and Blender would enjoy having access to. 

This final media transcoding process is a required step if the end output for the volumetric video is meshes and texture maps that will be used for visual effects/real-time focused workflows like creating crowds in XR stage virtual production shoots.

The final content would be formatted as:

* $HIP/abc/Mesh.usda (An OpenUSD ASCII Clip)  
* $HIP/abc/Mesh.\[\#\#\#\#\].abc  (An Alembic mesh sequence)  
* $HIP/abc/Mesh\_u1\_v1.\[\#\#\#\#\].exr (An OpenEXR image sequence)

## Why OBJs Meshes Kinda Suck in 2024

Wavefront OBJ meshes are just about past their "peak saturation point" of being the most accessible file format used in the VFX/XR sector. Other options like Autodesk FBX, Alembic, and OpenUSD all have their own unique upsides that are worth considering.

From a workflow automation perspective, where you have to move around TBs of data to a NAS (Network Attached Storage) system, there are a lot of downsides to continuing to use and store Wavefront OBJ files since the file format is inherently ASCII plain-text formatted uncompressed data.

The biggest issue is that OBJ files have no compact no binary representation option so data compression support of any kind is not a thing. This results in having to deal with mesh sequences that are greatly bloated in file size, which inevitably slows down all file transfers, backups, file load/save times, and direct media playback stages.

For practicality reasons, it can still make sense to have a photogrammetry program like Reality Capture or Metashape generate an .obj file as its output… but you will really want to think about transcoding the per-frame mesh data into an Alembic (.abc) or OpenUSD Crate (.usd) per-frame sequence when you go to write this data to backups, or pass the scans on  to external clients. It's the VFX artist \+ post-production workflow friendly thing to do.

Also, when talking about media & entertainment software in general, it is rare to have a fully multi-threaded OBJ mesh file loading library since OBJ meshes are loaded by reading ASCII files which are not (typically) binary seekable. Loading a per-frame 650 MB OBJ mesh sequence in a program like Autodesk Maya is a real pain\!

Along the same line not storing OBJ files, unless you have a strong need to do that, (which is defined by a "legacy" application compatibility requirement)... you might want to consider moving away from XYZ ASCII and PLY ASCII point cloud data storage and switch over to the very compact compressed [e57 point cloud file format](http://libe57.org/). Houdini has its own [Lidar Import](https://www.sidefx.com/docs/houdini/nodes/sop/lidarimport.html) node that does wonders when you want to load in e57 data with per-point color values.
