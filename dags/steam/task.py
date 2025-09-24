from airflow.decorators import task

from scripts.extract.steam.owned_games import ExtractSteamOwnedGames


@task
def extract_steam_owned_games() -> None:
    ExtractSteamOwnedGames().run()
