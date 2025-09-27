from airflow.decorators import task

from scripts.extract.steam.owned_games import ExtractSteamOwnedGames
from scripts.transform.steam.owned_games import TransformSteamOwnedGames


# Extract
@task
def extract_steam_owned_games() -> None:
    ExtractSteamOwnedGames().run()


# Transform
@task
def transform_steam_owned_games() -> None:
    TransformSteamOwnedGames().run()
