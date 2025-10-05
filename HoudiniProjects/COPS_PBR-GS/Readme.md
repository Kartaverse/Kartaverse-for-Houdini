# COPS Beeble to COLMAP Masking

This COPs network helps prepare live action footage for use in relighting workflows. It applies an alpha mask to each of the PBR textures output by Beeble Switchlight. Additionally, the specular and roughness greyscale images are converted into RGBA texture maps which makes photogrammetry and 3DGS training programs happy.

The source media is read with file nodes from:
$HIP/comp/$F4/basecolor/0000.png
$HIP/comp/$F4/specular/0000.png
$HIP/comp/$F4/roughness/0000.png
$HIP/comp/$F4/normal/0000.png

The processed media is written back to a per-camera view COLMAP file hierarchy using rop_image node based output file paths:
$HIP/colmap/basecolor/images/000001_$F1.png
$HIP/colmap/specular/images/000001_$F1.png
$HIP/colmap/roughness/images/000001_$F1.png
$HIP/colmap/normal/images/000001_$F1.png

# COPS PBR PreviewMaterial

Beeble Switchlight processed PBR texture maps are loaded into a COPs nodegraph and connected to a previewmaterial node. This allows you to assess the PBR maps quickly and easily.

The basecolor and normal texture maps are treated as RGB imagery. The specular and roughness are loaded as mono greyscale imagery. The alpha mask is connected to the opacity channel.

# SOPS PBR-GS PLY Attribute Transfer

In this Houdini project, PBS-GS data is formatted for use in Houdini, and for writing to disk as a modified PLY and BGEO output.

This example works with a set of custom PBR texture map trained 3DGS .ply files. The bakesplat nodes flatten down the specular and roughness data streams to Cd point values. Then the attribute transfer nodes are used to align the specular and roughness point samples to the nearest point in the basecolor ply file.

Finally those attributes are copied into a single data stream with the PBR-GS naming convention. BGEO and PLY output is written to disk using file nodes.

## How was this data created?

As a pre-processing step before 3DGS training was done: Beeble Switchlight was used to create PBR texture maps for each camera view in a video-grammetry style multi-view camera array.

Houdini COPs was used to take the alpha channel from the delit albedo imagery (called basecolor by Beeble) and apply that alpha mask to the other PBR channels. This avoids the 3DGS trained files from having an unwanted colored "fog" fill the volume when postshot or 3DGRUT trains the models.

Each of the PBR texture passes that were created by Beeble were used as the source imagery when generating per-frame multi-view 3DGS files:

- $HIP/ply/0001/basecolor.ply
- $HIP/ply/0001/specular.ply
- $HIP/ply/0001/roughness.ply
- ...

## Display Options

Make sure to set the SOPs and Solaris contexts to have the "Display Options -> Geometry -> Particles -> Display particles as" preference to "Pixels". Then set the "Display Options -> Background -> Color Scheme" preference to "Dark". This will make the point sample rendering clearer in the 3D viewport.

