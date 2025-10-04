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
