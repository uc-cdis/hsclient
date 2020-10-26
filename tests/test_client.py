import json


def test_import():
    """
    Try to import the index package.
    """
    import hsclient


def test_load1():
    """
    Test loading a Schema
    """

    jsonstring = """
    {
    "resource_type": "GenericResource",
    "resource_title": "Helium Test File for FAIR Assessment",
    "resource_id": "f7f091dc65a2432da285a7b70d07b333",
    "creator": "Ray Idaszak",
    "date_created": "07-24-2018",
    "date_last_updated": "07-31-2018",
    "public": true,
    "discoverable": true,
    "shareable": false,
    "coverages": [
        {
            "type": "point",
            "value": {
                "units": "Decimal degrees",
                "east": -79.0557,
                "north": 35.9133,
                "name": "Chapel Hill",
                "projection": "WGS 84 EPSG:4326"
            }
        }
    ],
    "immutable": false,
    "published": false,
    "bag_url": "http://beta.commonsshare.org/django_irods/download/bags/f7f091dc65a2432da285a7b70d07b333.zip",
    "science_metadata_url": "http://beta.commonsshare.org/hsapi/resource/f7f091dc65a2432da285a7b70d07b333/scimeta/",
    "resource_map_url": "http://beta.commonsshare.org/hsapi/resource/f7f091dc65a2432da285a7b70d07b333/map/",
    "resource_url": "http://beta.commonsshare.org/resource/f7f091dc65a2432da285a7b70d07b333/"
    }
    """

    from hsclient.client import HSClient
    from hsclient.client import Document

    client = HSClient("https://test.example/index")
    doc = Document(client, "f7f091dc65a2432da285a7b70d07b333", json.loads(jsonstring))
