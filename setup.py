from setuptools import setup, find_packages

setup(
    name="TinyMagic",
    version="0.9",
    description="Obfuscated Copado Custom Keywords",
    author="Graham Stoner",
    packages=find_packages(),
    # include_package_data is vital to ensure the .so file is copied
    include_package_data=True,
    # zip_safe=False is required for loading native binary extensions (.so)
    zip_safe=False,
    install_requires=[
        "robotframework",
    ],
)