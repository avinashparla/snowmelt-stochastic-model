import cdsapi
import os

# =========================
# CONFIGURATION
# =========================

OUTPUT_DIR = r"P:\snowmelt_stochastic_model\data\raw"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "era5_chandra_temp_2018_2022.nc")

AREA = [
    33.0,  # North
    76.5,  # West
    32.0,  # South
    77.5   # East
]

YEARS = ['2018', '2019', '2020', '2021', '2022']

VARIABLE = '2m_temperature'

# =========================
# CREATE OUTPUT DIRECTORY
# =========================

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# DOWNLOAD DATA
# =========================

def download_era5():
    print("Starting ERA5 download...")

    c = cdsapi.Client()

    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'variable': VARIABLE,
            'year': YEARS,
            'month': [
                '01','02','03','04','05','06',
                '07','08','09','10','11','12'
            ],
            'day': [
                '01','02','03','04','05','06','07','08','09','10',
                '11','12','13','14','15','16','17','18','19','20',
                '21','22','23','24','25','26','27','28','29','30','31'
            ],
            'time': ['00:00'],
            'area': AREA,
            'format': 'netcdf'
        },
        OUTPUT_FILE
    )

    print("Download complete!")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    download_era5()