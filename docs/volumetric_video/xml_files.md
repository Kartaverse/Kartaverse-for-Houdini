# XML Files

Reality Capture scene export parameters can be saved into an XML based file format:

```xml
<ModelExport exportBinary="1" exportInfoFile="1" exportVertices="1" exportVertexColors="0"
   exportVertexNormals="0" exportTriangles="1" exportTexturing="1" meshColor="4294967295"
   tileType="0" exportTextureAlpha="0" exportToOneTexture="0" oneTextureMaxSide="16384"
   oneTextureUsePow2TexSide="1" exportCoordinateSystemType="1" settingsAnchor="0 0 0"
   settingsScalex="1" settingsScaley="1" settingsScalez="1" texturesFileType="png"
   formatAndVersionUID="obj 000 " exportModelByParts="0" exportRandomPartColor="0"
   exportCameras="0" exportCamerasAsModelPart="0" numberAsciiFormatting="%.16e">
  <Header magic="5786949" version="1"/>
</ModelExport>
```

Scene cropping in Reality Capture can be saved to a .rcbox file that internally is an XML based file format:

```xml
<ReconstructionRegion globalCoordinateSystem="+proj=geocent +ellps=WGS84 +no_defs" globalCoordinateSystemName="local:1 - Euclidean"
   isGeoreferenced="1" isLatLon="0" yawPitchRoll="0 -0 -0">
  <widthHeightDepth>6.86994028091431 7.52994060516357 6.13969278335571</widthHeightDepth>
  <Header magic="5395016" version="2"/>
  <CentreEuclid>
    <centre>-0.607471704483032 0.591201782226563 12.0405006408691</centre>
  </CentreEuclid>
  <Residual R="1 0 0 0 1 0 0 0 1" t="0 0 0" s="1"/>
</ReconstructionRegion>
```

When automating multi-view Reality Capture workflows, it is helpful to know that the toolset is able to export each of the active camera locators to an XMP metadata format that includes both the transform matrix and lens distortion parameters. The XMP data is internally stored in an XML based file format:

```xml
<x:xmpmeta xmlns:x="adobe:ns:meta/">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description xcr:Version="2" xcr:PosePrior="locked" xcr:ComponentId="{02FFA67D-FB37-48C9-AAAE-115D1A41F754}"
       xcr:DistortionModel="division" xcr:DistortionCoeficients="-0.266409870680064 0 0 0 0 0"
       xcr:FocalLength35mm="15.8017301481925" xcr:Skew="0" xcr:AspectRatio="1"
       xcr:PrincipalPointU="0.00460590178527446" xcr:PrincipalPointV="-0.00856809553444162"
       xcr:CalibrationPrior="locked" xcr:CalibrationGroup="-1" xcr:DistortionGroup="-1"
       xcr:InTexturing="1" xcr:InColoring="0" xcr:InMeshing="1" xcr:latitude="179.984035152606480N"
       xcr:longitude="33.770888658912980E" xcr:version="2.2.0.0" xcr:altitude="643119440/10000"
       xmlns:xcr="http://www.capturingreality.com/ns/xcr/1.1#">
      <xcr:Rotation>-0.134784620568843 0.851774231082322 -0.506274397261226 0.00661363302515503 -0.510152020736598 -0.860058821009682 -0.990852847761129 -0.119271014930193 0.0631273243627475</xcr:Rotation>
      <xcr:Position>2.24050332940992 1.49823826996755 11.8964921935577</xcr:Position>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
```