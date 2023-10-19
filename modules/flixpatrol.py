from modules import util
from modules.util import Failed

logger = util.logger

ids_url = "https://raw.githubusercontent.com/meisnate12/PMM-TOP10/master/top10.yml"
builders = ["flixpatrol_top"]


class FlixPatrol:
    def __init__(self, config):
        self.config = config
        self._data = None
        self._platforms = None
        self._locations = None

    @property
    def data(self):
        if self._data is None:
            self._data = self.config.load_yaml(ids_url)
        return self._data

    @property
    def platforms(self):
        if self._platforms is None:
            self._platforms = [platform for platform in self.data]
            self._platforms.sort()
        return self._platforms

    @property
    def locations(self):
        if self._locations is None:
            self._locations = []
            for platform in self.data:
                self._locations.extend([loc for loc in self.data[platform] if loc not in self._locations and loc != "world"])
            self._locations.sort()
            self._locations = ["world"] + self._locations
        return self._locations

    def validate_builder(self, method, data, is_movie):
        builder_type = "movies" if is_movie else "shows"
        if method == "flixpatrol_top" and data["location"] in self.data[data["platform"]] and builder_type in self.data[data["platform"]][data["location"]]:
            return data
        raise Failed(f"FlixPatrol Error: No {builder_type[:-1].capitalize()} Data Found for {data['platform']} in {data['location']}")

    def get_tmdb_ids(self, method, data, is_movie):
        flix_items = []
        if method == "flixpatrol_top":
            logger.info("Processing FlixPatrol Top:")
            logger.info(f"\tPlatform: {data['platform'].replace('_', ' ').title()}")
            logger.info(f"\tLocation: {data['location'].replace('_', ' ').title()}")
            logger.info(f"\tLimit: {data['limit']}")
            flix_items = self.data[data["platform"]][data["location"]]["movies" if is_movie else "shows"][:data["limit"]]
        items = [(i, "tmdb" if is_movie else "tmdb_show") for i in flix_items]
        if len(items) > 0:
            logger.info(f"Processed {len(items)} TMDb IDs")
            return items
        else:
            raise Failed(f"FlixPatrol Error: No List Items found in {data}")
