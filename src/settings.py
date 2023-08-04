from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Road Vehicle"
PROJECT_NAME_FULL: Optional[str] = "Road Vehicle Images Dataset"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.DbCL_1_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [
    Industry.Utilities(is_used=False),
    Industry.Automotive(is_used=False),
]
CATEGORY: Category = Category.EnergyAndUtilities()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2021

HOMEPAGE_URL: str = "https://www.kaggle.com/datasets/ashfakyeafi/road-vehicle-images-dataset"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 387318
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/road-vehicle"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://www.kaggle.com/datasets/ashfakyeafi/road-vehicle-images-dataset/download?datasetVersionNumber=1"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "car": [230, 25, 75],
    "bicycle": [60, 180, 75],
    "bus": [255, 225, 25],
    "motorbike": [0, 130, 200],
    "three wheelers -CNG-": [245, 130, 48],
    "rickshaw": [145, 30, 180],
    "truck": [70, 240, 240],
    "pickup": [240, 50, 230],
    "minivan": [210, 245, 60],
    "suv": [250, 190, 212],
    "van": [0, 128, 128],
    "auto rickshaw": [220, 190, 255],
    "human hauler": [170, 110, 40],
    "wheelbarrow": [255, 250, 200],
    "ambulance": [128, 0, 0],
    "minibus": [170, 255, 195],
    "taxi": [128, 128, 0],
    "army vehicle": [255, 215, 180],
    "scooter": [0, 0, 128],
    "policecar": [128, 128, 128],
    "garbagevan": [0, 0, 0],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = None
CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = ["Ashfak Yeafi"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = None
ORGANIZATION_URL: Optional[Union[str, List[str]]] = None

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
