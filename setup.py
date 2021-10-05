import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='djangocms_gallery',  
     version='0.1',
     author="Stefan van den Eertwegh",
     author_email="stefan.eertwegh@gmail.com",
     description="Gallery plugin for django-cms",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/svandeneertwegh/djangocms-gallery",
     packages=setuptools.find_packages(),
     include_package_data = True,
     install_requires=[
          'django-cms>=3.9.0',
          'django-filer>=2.1rc2'
      ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
