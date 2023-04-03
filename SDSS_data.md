# SDSS Data Information

## [Describing SDSS images](https://sdss4.org/dr17/imaging/imaging_basics/)

The SDSS imaging camera scanned the sky in strips along great circles. Each strip consists of six parallel scanlines, 13 arcmin wide, with gaps of about the same width. Thus two strips, offset slightly from each other, together make a single stripe 2.5 degrees wide. Each scanline includes data in all five filters, ugriz. The fundamental units of SDSS images are fields Each field can be uniquely identified by a sequence of three numbers:

- the run number, which identifies the specific scan,
- the camera column, or "camcol," a number from 1 to 6, identifying the scanline within the run, and
- the field number. The field number typically starts at 11 (after an initial rampup time), and can be as large as 800 for particularly long runs.

Note that you can search of any area in the sky using the ra and dec value. However, knowing the run, camcol, and field number is useful for downloading the images as well as getting more information about the image. The run-camcol-field identifier can also be useful to download the FITS files for each SDSS filter, for example, 3704-3-91. Entering that identifier into the [Science Archive Server Imaging Fields](https://dr12.sdss.org/fields) search will create links to download the individual filter images as FITS files.

> [Navigate](https://skyserver.sdss.org/dr18/VisualTools/navi/) from the link.

> An additional number, rerun, specifies how the image was processed. There have been multiple reprocessings of the data over the years. Each reprocessing has been denoted by an integer (the first being rerun 0, the latest being rerun 301). Each rerun consists only in a change to the photometric pipeline, not to the underlying data.

### The Filters

In the camera schematic above, note that there are five rows of CCDs, labeled u, g, r, i and z. The SDSS camera has five filters, which together span the optical window. Each filter images a section of sky nearly, but not exactly, simultaneously (each filter is separated by 71.72 seconds of drift scan time).

The five filters stands for:

- u: Ultraviolet
- g: Green
- r: Red
- i: Infrared
- z: Farther-infrared

The wavelengths are:

| Image | Approximate wavelength |
| ----- | ---------------------- |
| u     | 3551 Å                 |
| g     | 4686 Å                 |
| r     | 6165 Å                 |
| i     | 7481 Å                 |
| z     | 8931 Å                 |

> The JPEGs shown in the SkyServer Navigate tool are a composite of the g, r, and i images.

## [Imaging Data Files](https://sdss4.org/dr17/imaging/images/)

The [Science Archive Server](https://data.sdss.org/sas/) provides two versions of the FITS images, which can be used for quantitative analysis:

- corrected frames for each field and band (sky-subtracted, calibrated)
- atlas images for each object (sky-subtracted, but uncalibrated)

> To use the images, it is useful to know the point-spread function (PSF). The SDSS photo software has estimated the PSF from the images.

### PSF Data

The `photo` software fits a PSF as a function of position for every SDSS field. General metadata on the PSF is stored in the `photoField` file on SAS, which is equivalent to the field table in CAS. Specifically, the psf_width parameter reports the average FWHM of a double Gaussian fit to the PSF. In addition, this file reports the parameters of that fit, as the data model describes.

## [Imaging Data Catalogs](https://sdss4.org/dr17/imaging/catalogs/)

### Image Classes

| Class        | Name     | Code |
| ------------ | -------- | ---- |
| Unknown      | UNK      | 0    |
| Cosmic Ray   | CR       | 1    |
| Defect       | DEFECT   | 2    |
| Galaxy       | GALAXY   | 3    |
| Ghost        | GHOST    | 4    |
| Known object | KNOWNOBJ | 5    |
| Star         | STAR     | 6    |
| Star trail   | TRAIL    | 7    |
| Sky          | SKY      | 8    |
