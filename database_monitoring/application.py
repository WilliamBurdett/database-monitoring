from database_monitoring.prefect_overriding.flow import MyFlow


def main() -> MyFlow:
    with MyFlow("monitor-database") as flow:
        pass
    return flow


if __name__ == "__main__":
    f = main()
    f.run()
