#!/usr/bin/env python3
""" DB query functions for the DT FL DB Application. """

# Imports - Python Standard Library
from typing import List
import sqlite3

# Imports - Local
from _81.DTFLDB.db_data import DBData
from _81.DTFLDB.display_banner import display_banner

# Constants
DB_EXTENSION = '.sqlite'
DB_NAME = f'dt_fail{DB_EXTENSION}'
DB_TABLE_NAME = 'history'


def query_db(
    db_name: str = DB_NAME,
    get_all_records: bool = False,
    query_filter: str = ''
) -> List[DBData]:
    """ Query a DB table for a specific value.

        Args:
            db_name (str, optional):
                Name of the db file.  Automatically adds the ".db"
                extension, if not found.  Default value is the value of
                the DB_NAME constant.'

            get_all_records (bool, optional):
                Type of query to run.  Must be True or False.
                Default is True.

            query_filter (str, optional):
                Filter to apply to the query.  Default is an empty string.

        Returns:
            query_results (List):
                List object with raw DB entry data.
    """

    # Connect to a SQLite3 DB and query the DB table, if it exists
    with sqlite3.connect(
        database=db_name
    ) as conn:

        # Create a cursor object
        cursor = conn.cursor()

        # Run the SQL command to query the DB table for all records
        if get_all_records:
            db_query = cursor.execute(
                f'''
                    SELECT * FROM {DB_TABLE_NAME};
                '''.strip()
            )
        # Run the SQL command to query the DB table for a specific record
        else:
            db_query = cursor.execute(
                f'''
                    SELECT * FROM {DB_TABLE_NAME}
                    WHERE LOWER(name) = "{query_filter}";
                '''.strip()
            )

        # Build a list of DBData namedtuple objects for the query results
        if db_query.arraysize > 0:
            query_results = [
                DBData(
                    name=row[0],
                    inbound_interest_score=row[1],
                    outbound_interest_score=row[2],
                    num_tries=row[3],
                    fl_reason=row[4]
                )
                for row in db_query.fetchall()
            ]

        # If no records were found, return an empty list
        else:
            query_results = []

    return query_results


def display_query_results(
    query_results: List[DBData]
) -> None:
    """ Display query results.

        Args:
            query_results (List):
                List of DBData objects with raw DB entry data.
    """

    if query_results:
        msg = display_banner(
            banner_string=f'** {len(query_results)} results found **'
        )
        print(msg)

        for index, result in enumerate(
            query_results,
            start=1
        ):
            print(
                f'{index}. Name: {result.name}\n'
                f'   Inbound Score: {result.inbound_interest_score}\n'
                f'   Outbound Score: {result.outbound_interest_score}\n'
                f'   Number of Tries: {result.num_tries}\n'
                f'   Failure Reason: {result.fl_reason}\n'
            )

    return None
