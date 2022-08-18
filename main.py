# region				-----External Imports-----
from dotenv import load_dotenv
import services
import fastapi
import typing
# endregion


load_dotenv()


app = fastapi.FastAPI(
    swagger_ui_parameters={
        "displayRequestDuration": True
    }
)


@app.get(path="/nearest_businesses")
async def nearest_businesses(longitude: float,
                              latitude: float,
                              query: str)\
    -> typing.List[typing.Dict]:
    return services.google.maps\
        .find_nearest_businesses(longitude=longitude,
                                 latitude=latitude,
                                 query=query)