import setuptools


if __name__ == '__main__':
    setuptools.setup(
        name="shoop-pugme",
        version="0.1",
        description="Pugs for your admin",
        packages=["shoop_pugme"],
        include_package_data=True,
        entry_points={"shoop.addon": "shoop_pugme=shoop_pugme"}
    )
