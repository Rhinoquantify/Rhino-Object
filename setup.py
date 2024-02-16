# -*- coding:utf-8 -*-

from distutils.core import setup


setup(
    name="RhinoObject",
    version="0.1.11",
    description="The Rhino quantify of Object",
    url="",
    author="XiNiu",
    author_email="xiniublog@163.com",
    license="GPL",
    packages=[
        "RhinoObject",
        "RhinoObject.Base",
        "RhinoObject.Rhino",
        "RhinoObject.RhinoRequest",
        "RhinoObject.Struct",
        "RhinoObject.Struct.FixedArray",
    ]
)
