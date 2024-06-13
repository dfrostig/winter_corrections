from pathlib import Path

code_dir = Path(__file__).parent

data_dir = code_dir / "data"

# paths
fits_file = data_dir / "example_data/example_science_image_mef.fits"
save_dir = data_dir / "example_data"
cor_dir = "/home/winter/GIT/winter_linearity/data/linearity_corrections"
test_directory = "/data/flats_iwr/20240610"
output_directory = data_dir / "linearity_corrections"

# variables
cutoff = 56000
