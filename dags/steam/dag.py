from datetime import datetime, UTC, timedelta

from airflow.decorators import dag

from dags.steam.task import extract_steam_owned_games


@dag(
    dag_id="steam",
    description="Extract, transform and load Steam data",
    tags=["steam", "daily"],
    start_date=datetime(2025, 9, 20, tzinfo=UTC),
    schedule="@daily",
    catchup=False,
    max_active_runs=1,
    max_active_tasks=1,
    default_args={
        "owner": "alessandro.felaco",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
        "execution_timeout": timedelta(minutes=5),
    },
)
def steam() -> None:
    extract_steam_owned_games()


steam()
