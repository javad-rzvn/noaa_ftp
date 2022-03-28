# NOAA-FTP

> I needed to work with data from NOAA, so I write a code in jupyter notebook and solved my problem for viewing and downloading data.
> Then I decided to convert that code to a python package.

My Personal Website: [Water Directory](https://waterdirectory.ir/).


To import, use command below:

```bash
from noaa_ftp import NOAA
```

Available functions:
- dir()
- download()

## Get list of files and folders

```bash
noaa_dir = NOAA("ftp.ncdc.noaa.gov", 'pub/data/ghcn/daily').dir()
noaa_dir
```

## Download custom file from the directory

```bash
noaa = NOAA("ftp.ncdc.noaa.gov", 'pub/data/ghcn/daily').download('ghcnd-stations.txt')
```