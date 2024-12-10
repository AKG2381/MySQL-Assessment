from sqlalchemy import create_engine

def connect_to_db(db_type, username, password, host, port, database):
    """
    Connects to different types of SQL databases.

    Args:
        db_type (str): Type of the database (e.g., 'mysql', 'postgresql', 'sqlite', 'mssql', 'oracle').
        username (str): Username for the database.
        password (str): Password for the database.
        host (str): Host address of the database.
        port (int): Port number of the database.
        database (str): Database name.

    Returns:
        engine: SQLAlchemy engine object or None if connection fails.
    """
    try:
        # Construct connection URL
        if db_type == 'sqlite':
            # SQLite uses file paths; username, password, host, and port are ignored
            connection_url = f"sqlite:///{database}"
        elif db_type == 'mysql':
            connection_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
        elif db_type == 'postgresql':
            connection_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
        elif db_type == 'mssql':
            connection_url = f"mssql+pyodbc://{username}:{password}@{host}:{port}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
        elif db_type == 'oracle':
            connection_url = f"oracle+cx_oracle://{username}:{password}@{host}:{port}/{database}"
        else:
            raise ValueError(f"Unsupported database type: {db_type}")

        # Create engine
        engine = create_engine(connection_url)
        # Test connection
        with engine.connect() as conn:
            print(f"Successfully connected to {db_type} database.")
        return engine
    except Exception as e:
        print(f"Failed to connect to {db_type} database: {e}")
        return None

# Example usage
if __name__ == "__main__":
    db_config = {
        "db_type": "mysql",  # Change to 'sqlite', 'postgresql', 'mssql', or 'oracle' as needed
        "username": "your_username",
        "password": "your_password",
        "host": "localhost",
        "port": 3306,  # Adjust port for your database type
        "database": "test_db"
    }
    engine = connect_to_db(**db_config)
