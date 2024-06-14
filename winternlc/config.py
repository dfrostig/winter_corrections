import os
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

code_dir = Path(__file__).parent

data_dir = code_dir.parent / "data"

# paths
example_data_dir = data_dir / "example_data"

EXAMPLE_IMG_PATH = example_data_dir / "example_science_image_mef.fits"
EXAMPLE_CORRECTED_IMG_PATH = example_data_dir / "corrected_example_science_image_mef.fits"
_corrections_dir = os.getenv("WINTERNLC_DIR")
if _corrections_dir is None:
    corrections_dir = Path.home() / "Data/winternlc/"
    logger.warning(f"No data directory set, using {corrections_dir}")
else:
    corrections_dir = Path(_corrections_dir)

corrections_dir.mkdir(parents=True, exist_ok=True)

test_directory = "/data/flats_iwr/20240610"
output_directory = data_dir / "linearity_corrections"

# variables
DEFAULT_CUTOFF = 56000
