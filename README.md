# HyperCP - HyperInSpace Community Processor
<html lang="en">

HyperInSpace Community Processor (HyperCP) is a community tool for processing in situ automated and manual, above-water, ocean color radiometry measurements. HyperCP is designed to provide in situ support for hyperspectral missions such as [PACE](https://pace.gsfc.nasa.gov/), multispectral missions such as [Sentinel-3](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-3), and all international missions with interest in aquatic biogeochemistry, algorithm development and satellite validations. 

HyperCP is an open science, open-source Collaboration to facilitate further community development and improvements to the algorithms and the processor package and to allow extensions to new field instrument platforms. See the [Guidelines for Collaboration on the HyperInSPACE Community Processor (HyperCP)](HyperCP_Project_guidelines.md) for information about the Collaboration, how to contribute, and how to reference HyperCP.

The goal of HyperCP is to facilitate consistent, rigorous, traceable and flexible in situ radiometry data processing. The package is developed using state-of-the-art algorithms, protocols for quality assurance, and the uncertainty propagation according to metrological standards. Data output are formatted to text files for submission to the [SeaBASS](https://seabass.gsfc.nasa.gov/) and [OCDB](https://ocdb.eumetsat.int/) databases and saved as comprehensive HDF5 records with automated processing reports
 
Currently, HyperCP supports two hyperspectral radiometers: [Sea-Bird Scientific](https://www.seabird.com/) HyperSAS packages with and without SolarTracker or pySAS platforms, as well as [TriOS](https://www.trios.de/en/radiometers.html) used in manual configuration . Refer to the [Guidelines](HyperCP_Project_guidelines.md) if you are interested in Collaboration to integrate other in situ platforms. Contact emails are also included on this page addresses below the Copyright section.


## Version 1.1.2 (see Changelog.md)

---
```
The MIT license

 Copyright © 2020 United States Government as represented by the Administrator of the National Aeronautics and Space Administration. All Rights Reserved.
 
 Copyright © 2023 EUMETSAT
 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 ```
---

**Main author**: Dirk Aurin, USRA @ NASA Goddard Space Flight Center <dirk.a.aurin@nasa.gov>

**Co-authors**: Nathan Vandenberg @ UVictoria, Maycira Costa @ UVictoria (in the frame of [PySciDON](https://ieeexplore.ieee.org/abstract/document/8121926)), Alexis Deru @ ACRI-ST, Ashley Ramsay @ NPL, Agnieszka Bialek @ NPL, Marine Bretagnon @ ACRI-ST (in the frame of Copernicus' [FRM4SOC-2](https://frm4soc2.eumetsat.int/))

**Contact**: Dirk Aurin, USRA @ NASA Goddard Space Flight Center <dirk.a.aurin@nasa.gov>, Juan Ignacio Gossn @ EUMETSAT <JuanIgnacio.Gossn@eumetsat.int>

## Requirements and Installation

Clone this repository (branch: "master") to a convenient directory on your computer. When HCP/Main.py is launched for the first time, sub-directories will be created and databases downloaded and moved into them as described below. No system files will be changed.

HyperInSpace Community Processor (HyperCP) requires Python 3.X installed on a Linux, MacOS, or Windows computer. The <a href='https://www.anaconda.com/'>Anaconda</a> distribution (or <a href='https://docs.conda.io/en/latest/miniconda.html'>Miniconda</a>) is encouraged. (If you are unfamiliar with Anaconda, a nice walkthrough can be found [here](https://youtu.be/YJC6ldI3hWk).)

All of the package dependencies are listed in the hcp.yml file included with the package. To make sure you have all of the necessary dependencies, navigate to the HCP directory and type

```
prompt$ conda env create -f hypercp.yml
```

and follow the prompts to install the additional package dependencies on your machine within the new virtual environment. When completed you should be in the virtual environment (hcp) and ready to run the package. To return to the environment later before launching the program, type

```
prompt$ conda activate hcp
```

To stay up to date with the latest commits to the master branch, always pull commits prior to useing the software. From the HyperInSPACE directory, type:

```
prompt$ git pull
```

To report an issue, please submit here: https://github.com/nasa/HyperInSPACE/issues

---
## Launching

<center><img src="Data/Img/banner.jpg" alt="banner"></center>

HyperCP is a Main-View-Controller Python package with a GUI that can be launched in several ways, such as by navigating to the project folder on the command line and typing
```
(hypercp) prompt$ python Main.py
```
However you launch the GUI, *watch for important feedback at the command line terminal* in addition to informational GUI windows.

There is a command line option for batching a single level which can be triggered by adding the ```-cmd``` argument to the above command followed by: ```-c config -i inputFile -o outputDirectory -l processingLevel```, where config is the configuration file, and the other arguments are self-explanatory (processingLevel should be in all caps, e.g., ```L1AQC```)

To see an example of a complete workflow of the processing from raw data to the final HDF and SeaBASS/OCDB L2 outputs, both for TriOS and HyperOCR, please see [here](https://gitlab.eumetsat.int/OC/External/frm4soc-cp/-/blob/master/Command_line_example.cmd)

The following sub-directories will be created automatically (if not present) when you first run the program:

- Config - Configuration and instrument files (by subdirectory - auto-created), SeaBASS header configuration files, Main view configuration file
- Logs - Most command line output messages generated during processing are captured for later reference in .log text files here
- Plots - A variety of optional plotting routines are included which create sub-directories (i.e. 'L1AQC_Anoms', 'L1B_Interp', 'L2_Spectral_Filter', 'L2', 'L2_Products'). As with the Data, this path for outputting plots is optional and will be overwritten by choosing an alternate Data/Plots parent directory (see below).
- Data - This directory now comes unpacked in the distribution. By default, it contains only files for seawater absorption properties, top-of-atmosphere solar irradiance, satellite sensor spectral response functions, banner images for the GUI, and the Zhang glint correction database. This is also the optional fallback location for input and/or output radiometry data, though using separate locations for field data is recommended (see below).
- Source - This directory (which comes unpacked with the distribution) holds the majority of the Python source code.

### Database download
When you first launch the software, it will need to download a large (2.3 GB) database (```Zhang_rho_db.mat```; Zhang et al., 2017, OE, 25(4)) for use in glint correction. If this database is not found in Data, a dialog window will appear before the Main.py GUI with guidance on how to proceed. If this download should fail for any reason, further instructions will be given at the command line terminal where Main.py was launched.

---
## Guide

### Quick Start Overview
1. Identify the research cruise, relevant calibration files, and ancillary data files to be used in processing
2. Launch HyperCP and set up the Main window for data directories and the ancillary file
3. Create a new Configuration (or edit and existing Configuration)
4. Add and enable only *relevant* calibration and instrument files to the Configuration; there is no such thing as a standard instrument package
5. Choose appropriate processing parameters for L1A-L2 (do not depend on software defaults; there is no such thing as a standard data collection)
6. HDF files will be produced at each level of processing, plus optional SeaBASS text files for radiometry at L2. Plots can be produced at L1AQC, L1B, and L2. Processing logs and plots are aggregated into PDF Reports at L2 (covering all processing from RAW to L2) written to a dedicated Reports directory in the selected Output directory.


### Main Window
<!---*<center><img src="Data/Img/Main.jpg" alt="banner"></center>*--->

The Main window appears once Main.py is launched. It has options to specify a configuration file, input/output directories, ancillary input files (i.e. environmental conditions and relevant geometries in a SeaBASS file format), single-level processing, and multi-level processing. For batch processing, pop-up windows from "failed" (no output due to either corrupt raw binary data or stringent quality control filtering) files can be suppressed. Producing no output file at a given processing level is often a normal result of quality control filtering, so this option allows batches to continue uninterrupted.

The 'New' button allows creation of a new configuration file. 'Edit' allows editing the currently selected configuration file. 'Delete' is used to delete the currently selected configuration file *and* corresponding auto-created calibration directories (see Configuration). After creating a new configuration file, select it from the drop-down menu, and select 'Edit' to launch the Configuration module and GUI.

The 'Input...' and 'Output Data/Plots Parent Directory' buttons are self explanatory and allow optional selection of data and directories from any mounted/mapped drive. Note that output data and plot sub-directories (e.g. for processing levels) are also auto-created during processing as described below. The parent directory is the directory containing the sub-directories for processing levels (e.g. "/L1A", "/L1B", etc.) If no input or output data directories are selected, '/Data' and '/Plots' under the HCP directory structure will be used by default as the parent directories.

Ancillary data files for environmental conditions and relevant geometries used in processing must be text files in SeaBASS format with columns for date, time, lat, and lon. See https://seabass.gsfc.nasa.gov/ for a description of SeaBASS format. Optional data fields include station number, ship heading, relative sensor azimuth, aerosol optical depth, cloud cover, salinity, water temperature, and wind speed. Example ancillary files are included for use as a template. It is recommended that ancillary files are checked with the 'FCHECK' utility as described on the SeaBASS website. They will be interpreted using the included SB_support.py module from NASA/OBPG.

In case environmental conditions were not logged in the field, or for filling in gaps in logged data, they will be retrieved from GMAO models as described below. The ancillary data file is optional (though strongly advised for adding wind speed at a minimum) provided the sensor suite is equipped with a SolarTracker or equivalent to supply the relevant sensor/solar geometries. If no SolarTracker-type instrument is present to report the relative sensor/solar geometries, the ancillary file must be provided with at least the ship heading and relative angle between the bow of the ship and the sensor azimuth as a function of time (see sample file provided). Application of the Zhang et al. (2017) glint correction will require the addition of GMAO model data for aerosol optical depth.

### Configuration

Launch the configuration module and GUI (ConfigWindow.py) from the Main window by selecting/editing a configuration file or creating a new one. This file will be instrument-suite-specific, and is also deployment-specific according to which factory calibration files are needed, as well as how the instrument was configured on the platform or ship. Some cruises (e.g. moving between significantly different water types) may also require multiple configurations to obtain the highest quality ocean color products at Level 2. Sharp gradients in environmental conditions could also warrant multiple configurations for the same cruise (e.g. sharp changes in temperature may effect how data deglitching is parameterized, as described below).

##### Calibration & Instrument Files:
***NOTE: IT IS IMPORTANT THAT THESE INSTRUCTIONS FOR SELECTING AND ACTIVATING CALIBRATION AND INSTRUMENT FILES ARE FOLLOWED CAREFULLY OR PROCESSING WILL FAIL***

**Note: You do not need to move/copy/paste your calibration and instrument files; HCP will take care of that for you.**

In the 'Configuration' window, click 'Add Calibration Files' to add the *relevant* calibration or instrument files (date-specific HyperOCR or TriOS factory calibrations or ancillary instrument Telemetry Definition Files; e.g. in the case of HyperOCR the '.cal' and '.tdf' files). *Only add and enable those calibration and instrument files that are relevant to the cruise/package you wish to process (see below).*

In the case of HyperOCR, each instrument you add here -- be it a radiometer or an external data instrument such as a tilt-heading sensor -- requires at least one .cal or .tdf file for raw binary data to be interpreted. Two .cal files are required in the case of radiometers calibrated seperately for shutter open (light) and shutter closed (dark) calibrations, as is typical with Satlantic/Seabird HyperOCRs. Instruments with no calibrations (e.g. GPS, SolarTracker, etc.) still require a Telemetry Definition File (.tdf) to be properly interpreted. Compressed archives (.sip) containing all the required cal files can also be imported here, and will be unpacked automatically by the software to place the calibration and telemetry files into the appropriate Config folder.

In the case of TriOS, 3 files are required per radiometer, to provide all the calibration data needed to the processing: for the device number "xxxx", Cal_xxxx.dat and Back_xxxx_dat, respectively contained the raw calibration factors and the background levels, while SAM_xxxx.ini provides initialisation information to the processor. 

Adding new files will automatically copy these files from the directory you identify on your machine into the HCP directory structure.

The calibration or instrument file is selected using the drop-down menu. Enable (in the neighboring checkbox) only the files that correspond to the data you want to process with this configuration. You will need to know which .cal/.tdf files correspond to each sensor/instrument, and which represent light and dark shutter measurements. For example for HyperOCR:
- SATMSG.tdf > SAS Solar Tracker status message string (Frame Type: Not Required)
- SATTHSUUUUA.tdf > Tilt-heading sensor (Frame Type: Not Required) (Note: Use of built-in flux-gate compass is extremely inadviseable on a steel ship or platform. Best practice is to use externally supplied heading data from the ship's NMEA datastream or from a seperate, external dual antenna GPS incorporated into the SolarTracker. DO NOT USE COURSE DATA FROM SINGLE GPS SYSTEMS.)
- SATNAVxxxA.tdf > SeaBird Solar Tracker (Frame Type: Not Required)
- UMTWR_v0.tdf > UMaine Solar Tracker (Frame Type: Not Required)
- GPRMC_NMEAxxx.tdf > GPS (Frame Type: Not Required)
- SATPYR.tdf > Pyrometer (Frame Type: Not Required)
- HEDxxxAcal > Es (Frame Type: Dark)
- HSExxxA.cal > Es (Frame Type: Light)
- HLDxxxA.cal > Li (Frame Type: Dark)
- HSLxxxA.cal > Li (Frame Type: Light)
- HLDxxxA.cal > Lt (Frame Type: Dark)
- HSLxxxA.cal > Lt (Frame Type: Light)

where xxx is the serial number of the SeaBird instrument, followed (where appropriate) by factory calibration codes (usually A, B, C, etc. associated with the date of calibration) ***Be sure to choose the factory calibration files appropriate to the date of data collection.***

For TriOS RAMSES device, you will need to associate each radiometers number to its type of acquisition (Li, Lt or Es), for exemple : 
- SAM_8166.ini  >  LI
- SAM_8329.ini  >  ES
- SAM_8595.ini  >  LT


Selections:
- Add Calibration Files - Allows loading calibration/instrument files into HCP. Once loaded the drop-down box can be used to select the file to enable the instrument and set the frame type.
- Enabled checkbox - Used to enable/disable loading the file in HCP.
- Frame Type 
     - [Seabird] ShutterLight/ShutterDark/Not Required can be selected. This is used to specify shutter frame type (ShutterLight/ShutterDark) for dark correction.
     - [TriOS] LI/LT/ES can be selected. This is used to specify the target of each radiometers.

For each calibration file:
Click 'Enable' to enable the calibration file. Select the frame type used for radiometer data or 'Not Required' for navigational and ancillary data. Data from the GPS and SATNAV instruments, etc. are interpreted using the corresponding Telemetry Definition Files ('.tdf').

Once you have created your new Configuration, CAL/TDF files are copied from their chosen locations into the /Config directory HCP directory structure within an automatically created sub-directory named for the Configuration (i.e. a configuration named "KORUS" creates a KORUS.cfg configuration file in /Config and creates the /Config/KORUS_Calibration directory with the chosen calibration & TDF files.

Level 1A through Level 2 processing configurations are adjusted in the Configuration window. If you are reading this for the first time, the Configuration Window is a good reference to accompany the discussion below regarding processing. *The values set in the configuration file should be considered carefully. They will depend on your viewing geometry and desired quality control thresholds. Do not use default values without consideration.* Level 1AQC processing includes a module that can be launched from the Configuration window to assist with data deglitching parameter selection ('Anomaly Analysis'). Spectral filters are also plotted in L1BQC to help with filter parameterization factors. More details with citations and default setting descriptions are given below. A separate module to assist in the creation of SeaBASS output files is launched in Level 2 processing, and applied to L2 SeaBASS output as described below.

Click 'Save/Close' or 'Save As' to save the configuration file. SeaBASS headers will be updated automatically to reflect your selection in the Configuration window.

### Processing Overview

It will be helpful to set your 'Input Data' and 'Output Data' directories from the Main window. As an example, one could use a cruise directory containing RAW HyperSAS data as the Input Parent Directory, and then create another directory to use as the Output Parent Directory when processing from L0 (raw binary). Files will be automatically sorted by processing level in the automatically created sub-directories (i.e. the software automatically creates and looks for L1A, L1AQC, L1B, L1BQC, and L2 directories under the parent directory). If not selected, the Input/Output parent directories will default to the /Data directory within HCP. Your Main window set-up (including configuration file, Input/Output directories, and Ancillary File) will be saved in Config/main.config using the Save button or upon closing the Main window, and reopened the next time you launch Main.py.

Process the data by clicking on one of the buttons for single-level or multi-level processing. A file selection dialogue will appear. Multiple data files can be processed together (successively) by simply selecting them together in the GUI (e.g. Shift- or Ctrl- click, or Ctrl-A for all, depending on your platform). Input files will be checked for match to expected input level (e.g. L1AQC file input for for L1B processing). Multi-level processing works the same as single-level by processing each input raw file through all levels before moving on to the next raw file. However, it will only continue with a given file if the preceding level was created immediately (within 1 minute) prior. *In other words, if -- due to changes in QA/QC parameterization -- a file is entirely discarded at a given level, but an old file of the same name still exists in that directory, it will be ignored, and processing for that file will be terminated for higher levels.*


<!---*Bug: Very rarely, when running the program for the first time, the first RAW binary data file opened for processing is not read in properly. Processing will fail with the error message: [filename] does not match expected input level. The file will process properly if run a second time (assuming it is a healthy file). Cause unknown.*-->

#### Level 1A - Preprocessing

Process data from raw binary (Satlantic HyperSAS '.RAW' collections) to L1A (Hierarchical Data Format 5 '.hdf'). Calibration files and the RawFileReader.py script allow for interpretation of raw data fields, which are read into HDF objects.

**Solar Zenith Angle Filter**: prescreens data for high SZA (low solar elevation) to exclude files which may have been collected post-dusk or pre-dawn from further processing. *Triggering the SZA threshold will skip the entire file, not just samples within the file, so do not be overly conservative with this selection, particularly for files collected over a long period.* Further screening for SZA min/max at a sample level is available in L1BQC processing.
**Default: 60 degrees (e.g. Brewin et al., 2016)**

#### Level 1AQC

Process data from L1A to L1AQC. Data are filtered for vessel attitude (pitch, roll, and yaw when available), viewing and solar geometry. *It should be noted that viewing geometry should conform to total radiance (Lt) measured at about 40 degrees from nadir, and sky radiance (Li) at about 40 degrees from zenith* **(Mobley 1999, Mueller et al. 2003 (NASA Protocols))**. Unlike other approaches, HCP eliminates data flagged for problematic pitch/roll, yaw, and solar/sensor geometries *prior* to deglitching the time series, thus increasing the relative sensitivity of deglitching for the removal of non-environmental anomalies.

**SolarTracker**: Select when using the Satlantic SolarTracker package. In this case sensor and solor geometry data will come from the SolarTracker (i.e. SATNAV**.tdf). If deselected, solar geometries will be calculated from GPS time and position with Pysolar, while sensor azimuth (i.e. ship heading and sensor offset) must either be provided in the ancillary data or (eventually) from other data inputs. Currently, if SolarTracker is unchecked, the Ancillary file chosen in the Main Window will be read in, subset for the relevant dates/times, held in the ANCILLARY_NOTRACKER group object, and carried forward to subsequent levels (i.e. the file will not need to be read in again at L2). If the ancillary data file is very large (e.g. for a whole cruise at high temporal resolution), this process of reading in the text file and subsetting it to the radiometry file can be slow.

**Rotator Home Angle Offset**: Generally 0. This is the offset between the neutral position of the radiometer suite and the bow of the ship. This *should* be zero if the SAS Home Direction was set at the time of data collection in the SolarTracker as per Satlantic SAT-DN-635. If no SolarTracker was used, the offset can be set here if stable (e.g. pointing angle on a fixed tower), or in the ancillary data file if changeable in time. Without SolarTracker, L1C processing will require at a minimum ship heading data in the ancillary file. Then the offset can be given in the ancillary file (dynamic) or set here in the GUI (static). *Note: as SeaBASS does not have a field for this angle between the instrument and the bow of the ship, the field "relaz" (normally reserved for the relative azimuth between the instrument and the sun) is utilized for the angle between the ship heading (NOT COG) and the sensor.*

**Rotator Delay**: Seconds of data discarded after a SolarTracker rotation is detected. Set to 0 to ignore. Not an option without SolarTracker.
**Default: 60 seconds (Vandenberg 2017)**

**Pitch & Roll Filter** (optional): Data outside these thresholds are discarded if this is enabled in the checkbox. These data may be supplied by a tilt-heading sensor incorporated in the raw data stream accompanied by a telmetry definition file (.tdf) as per above, or can be ingested from the Ancillary file (see SAMPLE_Ancillary_pySAS.sb provided in /Data).
**Default: 5 degrees (IOCCG Draft Protocols; Zibordi et al. 2019; 2 deg "ideal" to 5 deg "upper limit")**

**Absolute Rotator Angle Filter** (optional): Angles relative to the SolarTracker neutral angle beyond which data will be excluded due to obstructions blocking the field of view. These are generally set in the SolarTracker or pySAS software when initialized for a given platform. Not an option without SolarTracker or pySAS.
**Default: -40 to +40 (arbitrary)**

**Relative Solar Azimuth Filter** (optional): Relative azimuth angle in degrees between the viewing Li/Lt and the sun.
**Default: 90-135 deg (Mobley 1999, Zhang et al. 2017); 135 deg (Mueller 2003 (NASA Protocols)); 90 deg unless certain of platform shadow (Zibordi et al. 2009, IOCCG Draft Protocols)**

##### Deglitching (optional)

Light and dark data are screened for electronic noise ("deglitched" - see Anomaly Analysis), which is then removed from the data (optional, but strongly advised).
**(e.g. Brewin et al. 2016, Sea-Bird/Satlantic 2017)**

*Currently, spectra with anomalies in any band are deleted in their entirety, which is very conservative. It may be sufficient to set the anomalous values to NaNs, and only delete the entire spectrum if more than, say, 25% of wavebands are anomalous.*

##### Anomaly Analysis & Thresholding (optional)

Running the Anomaly Analysis to parameterize the deglitching algorithm requires L1AQC files, so they must first be processed to L1AQC with no deglitching and then loaded into the Anomaly Analysis tool to be reprocessed to L1AQC with deglitching.

Deglitching is highly sensitive to the parameters described below, as well as some environmental conditions not otherwise controlled for in L1AQC processing and the overall variability of the radiometric data itself. Therefore, a separate module was developed to tune these parameters for individual files, instruments, and/or field campaigns and conditions. A sharp temperature change of the instrument, shutter malfunction, or heavy vibration, for example, could impact "glitchy-ness" and change the optimal parameterization.

Due to high HyperOCR noise in the NIR, deglitching is currently hard-coded to only perform deglichting between 350 - 850 nm. Deglitching is conservative: i.e. if a value in any waveband within a timeseries is flagged, all data for that timestamp are removed.

The tool is launched pressing the Anomaly Analysis button in the Configuration Window. A dialog will appear to select an L1AQC file for deglitching, after which a GUI will display timeseries plots of the light (shutter open) and dark (shutter closed) data for a given waveband. Metadata including date, time, wind, cloud, waves, solar and sensor geometry are shown in the top of the window. In addition, the software allows the user to define the file naming scheme of photographs collected in the field, presuming they are named with date and time. The software will look in a directory called /Photos in the designated input directory structure and match all photos within 90 minutes of the mean collection time for the file. Matched photos can by scanned using the button on the right to launch the viewer. The slider below the metadata allows for adjustment of the wavelength to be screened (the Update button will update the figures for any changes in sensor or parameterization), and radio buttons allow selection between Es, Li, or Lt sensors. Sensors are parameterized independently of each other, and seperately for the light and dark signals. Plots are interactive and can be explored in higher detail by panning with the left mouse button or zooming with the right mouse button (a small "A" box in the bottom left of the plot restores it to all data, or right-click for more options).

For each waveband of each sensor, and for both light and dark shutter measurements, the time series of radiometric data are low-pass filtered with a moving average over time using discrete linear convolution of two one dimensional sequences with adjustable window sizes (number of samples in the window). For darks, a *STATIONARY* standard deviation anomaly (from the moving average in time) is used to assess whether data are within an adjustable "sigma factor" multiplier within the window. For lights, a *MOVING* standard deviation anomaly (from the moving average of separately adjustable window size) is used to assess whether data are within a separately adjustable sigma. The low-band filter is passed over the data twice (forward and backward). First and last data points for light and dark data cannot be accurately filtered with this method, and are always discarded.

Adjust the window size and sigma parameters for each instrument and hit Update (or keyboard Enter) to see which data (black circles) are retained or discarded (red 'x' or '+' for first and second pass, respectively). Default values optimized for NASA's HyperSAS are shown adjacent to each box, but these may not be appropriate for other packages. Move the slider and hit update to see how these factors impact data in various portions of the spectrum. The field '% Loss (all bands)' shows how application of the current parameterization decimates the *entire spectral/temporal dataset for the given sensor, not just the band shown*.

In addition to the low-pass filters, light and dark data from each sensor can be filtered with a high and low value threshold. This is off by default, but can be very powerful for custom processing (e.g., patchy cloud elimination), and tends to be more useful in the light data rather than the dark (shutter closed). However, error associated with nonlinearity of response in HyperOCRs with dynamic integration time adjustment can also be minimized using dark thresholds. Thresholds are chosen by selecting the desired band (and hit Set Band) independently for light and dark data, and choosing a minimum and/or maximum threshold value in the appropriate boxes. Change value to "None" if a particularly threshold should be ignored. For example, to filter Li data on thresholds only for a high threshold for dark data based on 555 nm, select the Threshold checkbox, select the Li Radio button, move the slider to 555 nm, and hit Update. Now, you can enter a value (e.g. 1.0) into the lefthand "Max" textbox and hit "Update" (or keyboard Enter). The filtered data should show in blue. *Keep in mind, they will only show in the waveband for which they were set,* but like the low-pass filter, if they fall outside the thresholds in that band, that timestamp will be deleted for all bands.

Currently, to threshold data from any of the three instruments, Threshold must be checked, but leaving the min/max values as None in the other sensors will still work to ignore thresholding those sensors.

*To see the results when reviewing the threshold parameters on a file, make sure the waveband slider is on the appropriate waveband (and hit Update).*

Once the parameters have been adjusted for each sensor, they can be saved (Save Sensor Params button) to the current software configuration and to a backup configuration file for later use. This means that once you have 'tuned' these parameters for a given file, the software will be able to load the file (from the Config directory) to reference those parameters. This is useful for reprocessing; *you should only need to tune these once for each file.* If you find that a given set of deglitching parameterizations is working sufficiently well for all your L1AQC files for a given cruise, simply save them once, save the Configuration from the Configuration Window, and the software configuration will reuse them for all files (i.e. it only applies alternative values for files that were specifically saved). Saved file-specific parameterization can be viewed/editted in the CSV file named after the Configuration in the Config directory (e.g. "KORUS_anoms.csv" for the "KORUS.cfg").

For record keeping and the PDF processing report, plots of the delitching (similar to those shown in realtime) can be saved to disk. Select the waveband interval at which to save plots (e.g. at 3.3 nm resolution and 20 interval, plots are produced every 66 nm, or 48 PNG files for a typical HyperSAS system), and click Save Anomaly Plots. Results of the anomaly detection are saved to [output_directory]/Plots/L1AQC_Anoms. Data flagged for removal given the parameterizations chosen in the Configuration window are shown for the filter first pass (red box) and second pass (blue star) and thresholds (red circles only shown in the band for which they were chosen).

For convenience a shortcut to processing the currently active L1AQC file to L1B is provided (Process to L1B).

To save the current values from the Anomaly Analysis tool as the defaults for the given cruise, Save Sensor Params > Close > Save/Close the Configuration Window.


**Defaults: Currently based on EXPORTSNA DY131; shown in GUI; experimental**
**(Abe et al. 2006, Chandola et al. 2009)**
**(API Reference: https://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html)**

<!--- * A problem with instrument linear response sensitivity to integration time was recently discoveres and is under investigation.
# * ATTENTION: Do your SeaBird HyperOCR dark-shutter data often look like a stepped response, like this?
# <center><img src="Data/DarkStepResponse.png" alt="LT Dark"></center>
# If so, please contact me to learn more about this issue if you are willing/able to share your data.
-->

#### Level 1B
Dark current corrections are applied followed by instrument calibrations and then matching of timestamps and wavebands for all radiometers in the suite.

Unlike legacy processing for Satlantic/Sea-Bird HyperSAS data in ProSoft, data here are dark current corrected prior to application of the calibration factors. This allows for the option of applying default/factory calibrations or full instrument characterization in conjunction with low-level radiometric uncertainty estimation. It should be noted that when applying calibration to the dark current corrected radiometry, the offsets (a0) cancel (see ProSoftUserManual7.7 11.1.1.5 Eqns 5-6) presuming light and dark factory cals are equivalent (which they historically have been from Satlantic/Sea-Bird).

**More to come on full instrument characterization versus default/factory calibration...**

Once instrument calibration has been applied, data are interpolated to common timestamps and wavebands, optionally generating temporal plots of Li, Lt, and Es, and ancillary data to show how data were interpolated.

Each HyperOCR collects data at unique and adaptive integration intervals and requires interpolation for inter-instrument comparison. Satlantic ProSoft 7.7 software interpolates radiometric data between radiometers using the OCR with the fastest sampling rate (Sea-Bird 2017), but here we use the timestamp of the slowest-sampling radiometer (typically Lt) to minimize perterbations in interpolated data (i.e. interpolated data in HCP are always closer in time to actual sampled data) **(Brewin et al. 2016, Vandenberg 2017)**.

Each HyperOCR radiometer collects data in a unique set of wavebands nominally at 3.3 nm resolution. For merging, they must be interpolated to common wavebands. Interpolating to a different (i.e. lower) spectral resolution is also an option. No extrapolation is calculated (i.e. interpolation is between the global minimum and maximum spectral range for *all* HyperOCRs). Spectral interpolation is by univariate spline with a smoothing factor of 3, but can be manually changed to liner (see ProcessL1B_Interp.interpolateWavelength).
**(API: https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html)**

In the case of TriOS, each radiometers have its own waveband definition, specify through a polynomial function avalable in the SAM_xxxx.ini file. TriOS resolution is usually really close to 3.3 nm but can slightly varies depending of this polynom. The same interpolation scheme describes above for HyperOCR is used on Trios data.

*Note: only the datasets specified in ProcessL1B.py in each group will be interpolated and carried forward. For radiometers, this means that ancillary instrument data such as SPEC_TEMP and THERMAL_RESP will be dropped at L1B and beyond. See ProcessL1b_Interp.py at Perform Time Intepolation comment.*

Optional plots of Es, Li, and Lt of L1B data can be generated which show the temporal interpolation for each parameter and each waveband to the slowest sampling radiometer timestamp. They are saved in [output_directory]/Plots/L1B_Interp. Plotting is time and memory intensive, and can also add significant time to PDF report production.

*{To Do: Allow provision for above water radiometers that operate simultaneously, sequentially and/or in the same wavebands.}*

#### Level 1BQC

Process L1B to L1BQC. Further quality control filters are applied to data prior to L2 ensemble binning and reflectance calculation.

Use of the Mobley (1999) and Zhang et al. 2017 glint corrections require wind data, and Zhang (2017) also requires aerosol optical depth, salinity, and sea surface temperature. L1BQC processing also uses wind speed to filter the data for minimizing glint contamination. Since most field collections of above water radiometry are missing some or all of these anchillary parameters (though they can be input in the Ancillary file, if available), an embedded function allows the user to download model data from the NASA EARTHDATA server. These data are generated by the NASA Global Modeling and Assimilation Office (GMAO) as hourly, global 'MERRA2' HDF files at 0.5 deg (latitude) by 0.625 deg (longitude) resolution (https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/). Two files will be downloaded for each hour of data processed (total ~8.3 MB for one hour of field data) and stored in /Data/Anc. Global ancillary data files from GMAO will be reused, so it is not recommended to clear this directory unless updated models are being released by GMAO. *(Note: MERRA2 files downloaded prior to March 15, 2022 can be deleted as the file name format has changed.)*  Details for how these data are applied to above water radiometry are given below.

As of January 2020, access to these data requires a user login and password, which can be obtained here (https://oceancolor.gsfc.nasa.gov/registration). A link to register is also provided in the Configuration window at L1BQC. When the user selects 'Download Ancillary Models', pop-up windows will allow the user to enter a login and password. Once this has been done once, canceling the login pop-up dialog will force the program to use the current configuration (i.e. it is only necessary to re-enter the password if it has changed.)

These ancillary data from models will be incorporated if field data are not incorporated in the Ancillary file provided in the Main window. If field data and model data are both innaccessible for any reason, the system will use the Default values (i.e., Wind Speed, AOD, Salinity, and SST) provided in the L1BQC Configuration setup here.

Individual spectra may be filtered out for:
**Lt(NIR)>Lt(UV)**
Spectra with Lt higher in the UV (average from 780-850) than the UV (350-400) are eliminated.
*{Unable to find citation for the Lt(NIR)> Lt(UV) filter...}*

**Maximum Wind Speed**.
**Default 7 m/s (IOCCG Draft Protocols 2019; D'Alimonte pers.comm 2019); 10 m/s Mueller et al. 2003 (NASA Protocols); 15 m/s (Zibordi et al. 2009);**

**Solar Zenith Angle** may be filtered for minimum and maximum values.
**Default Min: 20 deg (Zhang et al 2017); Default Max: 60 deg (Brewin et al. 2016)**

**Spectral Outlier Filter** may be applied to remove noisy data prior to binning. This simple filter examines only the spectra of Es, Li, and Lt from 400 - 700 nm, above which the data are noisy in both devices. Using the standard deviation of the normalized spectra for the entire sample ensemble, together with a multiplier to establish an "envelope" of acceptable values, spectra with data outside the envelop in any band are rejected. Currently, the arbitrary filter factors are 5.0 for Es, 8.0 for Li, and 3.0 for Lt. Results of spectral filtering are saved as spectral plots in [output_directory]/Plots/L1BQC_Spectral_Filter. The filter can be optimized by studying these plots for various parameterizations of the filter.

**Meteorological flags** based on **(Ruddick et al. 2006, Mobley, 1999, Wernand et al. 2002, Garaba et al. 2012, Vandenberg 2017)** can be optionally applied to screen for undesirable data. Specifically, data are filtered for cloud cover, unusually low downwelling irradiance at **480 nm < default 2.0 uW cm^-2 nm^-1** for data likely to have been collected near dawn or dusk, or **(Es(470)/Es(680) < 1.0**), and for data likely to have high relative humidity or rain (**Es(720)/Es(370) < 1.095**). Cloud screening (**Li(750)/Es(750) >= 0.05**) is optional and not well parameterized. Clear skies are approximately 0.02 (Mobley 1999) and fully overcast are of order 0.3 (Ruddick et al. 2006). However, the Ruddick skyglint correction (below) can partially compensate for clear versus cloudy skies, so to avoid eliminating non-clear skies prior to glint correction, set this high (e.g. 1.0). Further investigation with automated sky photography for cloud cover is warranted.

TODO: Refer to [this](Provide link to deliverable 6 of FRM4SOC-Phase 2) document to see recommended QC screening in the frame of [FRM4SOC-2](https://frm4soc2.eumetsat.int/).

#### Level 2

Process L1B to L1BQC. Data are averaged within optional time interval ensembles prior to calculating the remote sensing reflectance within each ensemble. A typical field collection file for the HyperSAS SolarTracker is one hour, and the optimal ensemble periods within that hour will depend on how rapidly conditions and water-types are changing, as well as the instrument sampling rate. While the use of ensembles is optional (set to 0 to avoid averaging), it is highly recommended, as it allows for the statistical analysis required for Percent Lt calculation (radiance acceptance fraction; see below) within each ensemble, rather than %Lt across an entire (e.g. one hour) collection, and it also improves radiometric uncertainty estimation.

**Ensembles**
**Extract Cruise Stations** can be selected if station information is provided in the ancillary data file identified in the Main window. If selected, only data collected on station will be processed, and the output data/plot files will have the station number appended to their names. At current writing, stations must be numeric, not string-type. If this option is deselected, all automated data (underway and on station) will be included in the ensemble processing.

Ancillary file should include lines for both the start and stop times of the station for proper interpolation in L1B.

**Ensemble Interval** can be set to the user's requirements depending on sampling conditions and instrument rate (**default 300 sec**). Setting this to zero avoids temporal bin-averaging, preserving the common timestamps established in L1B. Processing the data without ensenble averages can be very slow, as the reflectances are calculated for each spectrum collected (i.e. nominally every 3.3 seconds of data for HyperSAS). The ensemble period is used to process the spectra within the lowest percentile of Lt(780) as defined/set below. The ensemble average spectra for Es, Li, and Lt is calculated, as well as variability in spectra within the ensemble, which is used to help estimate sample uncertainty.

**Percent Lt Calculation** Data are optionally limited to the darkest percentile of Lt data at 780 nm within the sampling interval (if binning is performed; otherwise across the entire file) to minimize the effects of surface glitter from capillary waves. The percentile chosen is sensitive to the sampling rate. The 5% default recommended in Hooker et al. 2002 was devised for a multispectral system with rapid sampling rate.
**Default: 5 % (Hooker et al. 2002, Zibordi et al. 2002, Hooker and Morel 2003); <10% (IOCCG Draft Protocols)**.
TODO can this be made compatible with Kevin's recommendation of chosing the first 5 scans?

**Skyglint/Sunglint Correction (rho)**
The value for (**Rho_sky**, sometimes called the Fresnel factor) can be estimated using various approaches in order to correct for glint **(Mobley 1999, Mueller et al. 2003 (NASA Protocols))**. It is adjusted for wind speed and solar-senzor geometries. The default wind speed (U) should be set by the user depending on in situ conditions, for instances when the ancillary data and models are not available (see L1BQC above, and further explanation below). The Mobley 1999 correction does not account for the spectral dependence **(Lee et al. 2010, Gilerson et al. 2018)** or polarization sensitivity **(Harmel et al. 2012, Mobley 2015, Hieronymi 2016, D'Alimonte and Kajiyama 2016, Foster and Gilerson 2016, Gilerson et al. 2018)** in Rho_sky. Uncertainty in Rho_sky (Rho_sky_Delta) is estimated from Ruddick et al. 2006 at +/- 0.003. The tabulated LUT used for the Mobley 1999 glint correction derived from **Mobley, 1999, Appl Opt 38, page 7445, Eq. 4** and can be found in the /Data directory as text or HDF5 data.

*{TODO: Uncertainty estimates for rho in M99 are no longer current (vastly overestimated) since the incorporation of the full LUT 2021-11-17.)}*

The **Zhang et al. 2017** model explicitly accounts for spectral dependence in rho, separates the glint contribution from the sky and the sun, and accounts for polarization in the skylight term. This approach requires knowledge of environmental conditions during sampling including: wind speed, aerosol optical depth, solar and sensor azimuth and zenith angles, water temperature and salinity. To accomodate these parameters, HCP uses either the ancillary data file provided in the main window, GMAO models, or the default values set in the Configuration window as follows: field data ancillary files are screened for wind, water temperature, and salinity. These are each associated with the nearest timestamps of the radiometer suite to within one hour. Radiometer timestamps still lacking wind and aerosol data will extract it from the GMAO models, if available. Otherwise, the default values set in the Configuration window will be used as a last resort.

*{TODO: Work to optimize the processing of Zhang rho. Currently, this proceeds far more slowly in Python than Matlab. See notes in ZhangRho.py for gen_vec_quad and prob_reflection near L165}*
*{TODO: Include additional skylight/skyglint corrections, such as Groetsch et al. 2017/2020}*
*{TODO: Include a bidirectional correction to Lw based on, e.g. Lee 2011, Zibordi 2009 (for starters; ultimately the BRDF will need to be better parameterized for all conditions and water types.)}*
*{TODO: Improve uncertainty estimates (e.g. Zibordi et al. 2009). The uncertainty in rho within the Zhang model is not well constrained.}*

Remote sensing reflectance is calculated as Rrs = (Lt - rho_sky* Li) / Es (e.g. **(Mobley 1999, Mueller et al. 2003, Ruddick et al. 2006)**). Normalized water leaving radiance (nLw) is calculated as Rrs*F0, where F0 is the top of atmosphere incident radiation adjusted for the Earth-Sun distance on the day sampled. This is now estimated using the Coddington et al. (2021) TSIS-1 hybrid model.

Uncertainties in Li, Lt, and Es are estimated using the standard deviation of spectra within each ensemble (e.g. Li_sd) or full-file average if no ensembles are extracted. For the Mobley 1999 (M99) glint correction, uncertainty in Rho_sky (Rho_sky_Delta) is estimated as +/- 0.01 based on the range of model estimates for Rho_sky cited in M99 for the range of likely conditions for which it is held constant. Uncertainty in Rho_sky is otherwise estimated as +/- 0.003 from Ruddick et al. 2006 Appendix 2; intended for clear skies, though in the future variation in Rho_sky_Delta as a mutable function of sky and sea surface conditions should be better constrained when possible (i.e. further research is required). Uncertainty in Rrs (i.e. Rrs_unc) and nLw are estimated using sum of squares propagation of from Li_sd, Lt_sd, Es_sd, and Rho_sky_Delta assuming random, uncorrelated error. So, e.g.: Rrs_unc = Rrs * ( (Li_sd/Li)^2 + (Rho_sky_Delta/Rho_sky)^2 + (Lt_sd/Lt)^2 + (Es_sd/Es)^2 )^0.5

*{TODO: link to FRM4SOC2-D10 from NPL descibing the uncertainty propagation.}

Additional glint may be removed from the Rrs and nLw by subtracting the value in the NIR from the entire spectrum **(Mueller et al. 2003 (NASA Protocols))**. This approach, however, assumes neglible water-leaving radiance in the 750-800 nm range (not true of turbid waters), and ignores the spectral dependence in sky glint, and **should therefore only be used in the clearest waters and with caution**. Here, a minimum in Rrs(750-800) or nLw(750-800) is found and subtracted from the entire spectrum.

An alternate NIR residual correction can be applied based on **Ruddick et al. 2005, Ruddick et al. 2006**. This utilizes the spectral shape in water leaving reflectances in the NIR to estimate the residual glint correction for turbid waters with NIR reflectances from about 0.0001 to 0.03

Negative reflectances may be removed as follows: any spectrum with any negative reflectances between 380 nm and 700 nm is removed from the record entirely. Negative reflectances outside of this range (e.g. noisy data deeper in the NIR) are set to 0.

Spectral wavebands for a few satellite ocean color sensors can be optionally calculated using their spectral weighting functions. These will be included with the hyperspectral output in the L2 HDF files. Spectral response functions are applied to convolve the (ir)radiances prior to calculating reflectances. **(Burgghoff et al. 2020)**.

Plots of processed L2 data from each radiometer and calculated reflectances can be created and stored in [output_directory]/Plots/L2. Uncertainties are shown for each spectrum as shaded regions, and satellite bands (if selected) are superimposed on the hyperspectral data.

Select the "Derived L2 Ocean Color Products" button to choose, calculate, and plot derived biochemical and inherent optical properties using a variety of ocean color algorithms. Algorithms largely mirror those available in SeaDAS with a few additions. They include OC3M, PIC, POC, Kd490, iPAR, GIOP, QAA, and the Average Visible Wavelength (Vandermuellen et al. 2020) and GOCAD-based CDOM/Sg/DOC algorithms (Aurin et al. 2018), as well as the Rrs spectral QA score (Wei et al 2016).

To output SeaBASS/OCDB formatted text files, check the box. A subfolder within the L2 directory will be created, and separate text files will be made for Li, Lt, Es, and Rrs hyperspectral data and satellite bands, if selected. Set-up for the SeaBASS header is managed with 'Edit/Update SeaBASS Header'.

##### SeaBASS/OCDB File and Header

To output SeaBASS/OCDB formatted text files, check the box. A SeaBASS subfolder within the L2 directory will be created, and separate files generated for Li, Lt, and Es hyperspectral data.

An eponymous, linked module allows the user to collect information from the data and the processing configuration (as defined in the Configuration window) into the SeaBASS files and their headers. The module is launched by selecting the 'Edit SeaBASS Header' button in the Configuration window. A SeaBASS/OCDB header configuration file is automatically stored in the /Config directory with the name of the Configuration and a .hdr extension. Instructions are given at the top of the SeaBASS Header window. Within the SeaBASS/OCDB header window, the left column allows the user to input the fields required by SeaBASS/OCDB. Calibration files (if they have been added at the time of creation) are auto-populated. In the right hand column, the HCP parameterizations defined in the Configurations window is shown in the 'Config Comments' box, and can be editted (though this should rarely ever be necessary). Additional comments can be added in the second comments field, and the lower fields are autopopulated from each data file as it is processed. To override auto-population of the lower fields in the right column, enter the desired value here in the SeaBASS Header window.

*{TODO: Populate the left column using values in the Ancillary file, if present.}*

**PDF Reports**

Upon completion of L2 processing for each file (or lower level if that is the terminal processing level), a PDF summary report will be produced and saved in [output_directory]/Reports. The report is produced either 1) when processing fails at any level, or 2) at L2. This contains metadata, processing parameters, processing logs, and plots of QA analysis, radiometry, and derived ocean color products. These reports should be used to evaluate the choices made in the configuration and adjust them if necessary.


## References
- Abe, N., B. Zadrozny and J. Langford (2006). Outlier detection by active learning. Proceedings of the 12th ACM SIGKDD international conference on Knowledge discovery and data mining. Philadelphia, PA, USA, Association for Computing Machinery: 504–509.
- Brewin, R. J. W., G. Dall'Olmo, S. Pardo, V. van Dongen-Vogels and E. S. Boss (2016). "Underway spectrophotometry along the Atlantic Meridional Transect reveals high performance in satellite chlorophyll retrievals." Remote Sensing of Environment 183: 82-97.
- Burggraaff, O. (2020). "Biases from incorrect reflectance convolution." Optics Express 28(9): 13801-13816.
- Chandola, V., A. Banerjee and V. Kumar (2009). "Anomaly detection: A survey." ACM Comput. Surv. 41(3): Article 15.
- Coddington, O. M., Richard, E. C., Harber, D., Pilewskie, P., Woods, T. N., Chance, K., et al. (2021). The TSIS-1 Hybrid Solar Reference Spectrum. Geophysical Research Letters, 48, e2020GL091709. https://doi.org/10.1029/2020GL091709
- D’Alimonte, D. and T. Kajiyama (2016). "Effects of light polarization and waves slope statistics on the reflectance factor of the sea surface." Optics Express 24(8): 7922-7942.
- Foster, R. and A. Gilerson (2016). "Polarized transfer functions of the ocean surface for above-surface determination of the vector submarine light field." Applied Optics 55(33): 9476-9494.
- Garaba, S. P., J. Schulz, M. R. Wernand and O. Zielinski (2012). "Sunglint Detection for Unmanned and Automated Platforms." Sensors 12(9): 12545.
- Gilerson, A., C. Carrizo, R. Foster and T. Harmel (2018). "Variability of the reflectance coefficient of skylight from the ocean surface and its implications to ocean color." Optics Express 26(8): 9615-9633.
- Harmel, T., A. Gilerson, A. Tonizzo, J. Chowdhary, A. Weidemann, R. Arnone and S. Ahmed (2012). "Polarization impacts on the water-leaving radiance retrieval from above-water radiometric measurements." Applied Optics 51(35): 8324-8340.
- Hieronymi, M. (2016). "Polarized reflectance and transmittance distribution functions of the ocean surface." Optics Express 24(14): A1045-A1068.
- Hooker, S. B., G. Lazin, G. Zibordi and S. McLean (2002). "An Evaluation of Above- and In-Water Methods for Determining Water-Leaving Radiances." Journal of Atmospheric and Oceanic Technology 19(4): 486-515.
- Hooker, S. B. and A. Morel (2003). "Platform and Environmental Effects on Above-Water Determinations of Water-Leaving Radiances." Journal of Atmospheric and Oceanic Technology 20(1): 187-205.
- Lee, Z., Y.-H. Ahn, C. Mobley and R. Arnone (2010). "Removal of surface-reflected light for the measurement of remote-sensing reflectance from an above-surface platform." Optics Express 18(25): 26313-26324.
- Mobley, C. D. (1999). "Estimation of the remote-sensing reflectance from above-surface measurements." Applied Optics 38(36): 7442-7455.
- Mobley, C. D. (2015). "Polarized reflectance and transmittance properties of windblown sea surfaces." Applied Optics 54(15): 4828-4849.
- Mueller, J. L., A. Morel, R. Frouin, C. O. Davis, R. Arnone, K. L. Carder, Z. P. Lee, R. G. Steward, S. B. Hooker, C. D. Mobley, S. McLean, B. Holbert, M. Miller, C. Pietras, K. D. Knobelspiesse, G. S. Fargion, J. Porter and K. J. Voss (2003). Ocean Optics Protocols for Satellite Ocean Color Sensor Validation, Revision 4, Volume III. Ocean Optics Protocols for Satellite Ocean Color Sensor Validation. J. L. Mueller. Greenbelt, MD, NASA Goddard Space Flight Center.
- Ruddick, K., V. De Cauwer and B. Van Mol (2005). Use of the near infrared similarity reflectance spectrum for the quality control of remote sensing data, SPIE.
- Ruddick, K. G., V. De Cauwer, Y.-J. Park and G. Moore (2006). "Seaborne measurements of near infrared water-leaving reflectance: The similarity spectrum for turbid waters." Limnology and Oceanography 51(2): 1167-1179.
- Simis, S.G.H., J. Olsson (2013). "Unattended processing of shipborne hyperspectral reflectance measurements." Remote Sensing of Environment, Volume 135.
- Vandenberg, N., M. Costa, Y. Coady and T. Agbaje (2017). PySciDON: A python scientific framework for development of ocean network applications. 2017 IEEE Pacific Rim Conference on Communications, Computers and Signal Processing (PACRIM).
- Wernand, M. R. (2002). GUIDELINES FOR (SHIP BORNE) AUTO-MONITORING
OF COASTAL AND OCEAN COLOR. Ocean Optics XVI. S. Ackleson and C. Trees. Santa Fe, NM, USA.
- Zhang, X., S. He, A. Shabani, P.-W. Zhai and K. Du (2017). "Spectral sea surface reflectance of skylight." Optics Express 25(4): A1-A13.
- Zibordi, G., S. B. Hooker, J. F. Berthon and D. D'Alimonte (2002). "Autonomous Above-Water Radiance Measurements from an Offshore Platform: A Field Assessment Experiment." Journal of Atmospheric and Oceanic Technology 19(5): 808-819.
- Zibordi, G., F. Mélin, J.-F. Berthon, B. Holben, I. Slutsker, D. Giles, D. D’Alimonte, D. Vandemark, H. Feng, G. Schuster, B. E. Fabbri, S. Kaitala and J. Seppälä (2009). "AERONET-OC: A Network for the Validation of Ocean Color Primary Products." Journal of Atmospheric and Oceanic Technology 26(8): 1634-1651.
- Zibordi, G., K. J. Voss, B. Johnson and J. L. Mueller (2019). Protocols for Satellite Ocean Colour Data Validation: In Situ Optical Radiometry. IOCCG Ocean Optics and Biogeochemistry Protocols for Satellite Ocean Colour Sensor Validation. IOCCG. Dartmouth, NS, Canada, IOCCG.
