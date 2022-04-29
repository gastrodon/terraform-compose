from typing import Dict

import pytest

from library.transform import path

cases = [
    [
        {
            "service": {
                "computer": {"path": "."},
                "cloud.computer": {"path": "."},
            }
        },
        {
            "service": {
                "computer": {"path": "/tf-compose"},
                "cloud.computer": {"path": "/tf-compose/cloud"},
            }
        },
    ],
    [
        {
            "service": {
                "computer": {"value": "@file"},
                "cloud.computer": {"value": "@file"},
            }
        },
        {
            "service": {
                "computer": {"value": "@/tf-compose/file"},
                "cloud.computer": {"value": "@/tf-compose/cloud/file"},
            }
        },
    ],
    [
        {
            "service": {
                "computer": {"backend_config": ["./backend"]},
                "cloud.computer": {"backend_config": ["./backend"]},
            }
        },
        {
            "service": {
                "computer": {"backend_config": ["/tf-compose/backend"]},
                "cloud.computer": {"backend_config": ["/tf-compose/cloud/backend"]},
            }
        },
    ],
]


@pytest.mark.parametrize("source,want", cases)
def test_absolutize(source: Dict, want: Dict, mocker):
    # os.path.realpath uses os.getcwd under the hood
    mocker.patch("os.getcwd", return_value="/tf-compose")

    assert path.absolutize(source) == want
