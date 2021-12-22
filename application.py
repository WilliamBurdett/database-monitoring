from database_monitoring.prefect_overriding.flow import MyFlow


def setup_database(database_name: str):
    pass


def main(database_name: str) -> MyFlow:
    with MyFlow("database-monitoring") as flow:
        pass
    return flow


if __name__ == "__main__":
    f = main("")
    f.run()
