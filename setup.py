import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='corebytecms_gallery',  
     version='0.3',
     author="Stefan van den Eertwegh",
     author_email="stefan.eertwegh@gmail.com",
     description="Gallery plugin for djangocms",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/svandeneertwegh/corebytecms-gallery",
     packages=["corebytecms_gallery"],
     include_package_data = True,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
