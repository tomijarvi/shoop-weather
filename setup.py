import setuptools


if __name__ == '__main__':
    setuptools.setup(
        name="shoop-weather",
        version="0.1",
        description="Weather for Shoopio",
        packages=["shoop_weather"],
        include_package_data=True,
        entry_points={"shoop.addon": "shoop_pugme=shoop_weather"}
    )
