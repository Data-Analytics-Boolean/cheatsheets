import streamlit as st
import pandas as pd

st.image('https://hiringplatform.boolean.careers/images/logo.png', width=200)

def st_code_block(url=None, caption=None, code=None):
    # prefill the http address for the sql-reference url
    #if not url.startswith("https"):
    #    url = f"https://www.w3schools.com/sql/{url}.asp"
    if caption: 
        st.markdown(caption)
    if code: 
        st.code(code, language="sql")
    if url: 
        if not url.startswith("https"):
            url = f"https://www.w3schools.com/sql/{url}.asp"
            st.link_button("Read the documentation", url)
        elif "wikipedia" in url: 
            st.link_button("Read more on Wikipedia", url)
        else:
            st.link_button("Read this article to learn more", url)


def database_segment():
    st.header("Different ways to store data", help="Click on the tabs below to explore the different types of databases.")
    st.markdown("Let’s start with an introduction on the definition of the several types of databases that you may encounter out there as well as their main differences.")
    db_tab, dwh_tab, dl_tab, comparison_tab = \
        st.tabs(["Database", "Data Warehouse", "Data Lake", "Comparison Table"])
    with db_tab:
        st_code_block("https://en.wikipedia.org/wiki/Database", 
                      "A database is a **structured collection of data** organised for efficient retrieval, manipulation, and storage. \
                        It serves as a central repository for storing various types of data, ranging from text and numbers to multimedia files. \
                        Databases are tailored for **transactional processing and operational tasks**.",
        )
        st.info("MySQL is a popular open-source database, it is one of the most widely used across the world.", icon="💡")

    with dwh_tab:
        st_code_block("https://en.wikipedia.org/wiki/Data_warehouse", 
                      "A data warehouse is a centralised repository that stores structured and organised data from one or more sources. \
                        It is **optimised for analytical processing and reporting**, allowing businesses to analyse large volumes of historical data to gain insights and make informed decisions.")
        st.info("Some popular options when it comes to data warehousing are Google BigQuery, Amazon Redshift, Snowflake and Microsoft SQL Server (among many others).", icon="💡")

    with dl_tab:
        st_code_block("https://en.wikipedia.org/wiki/Data_lake", 
                      "A data lake is a **large, scalable storage system** that can hold vast amounts of raw, **unstructured, and semi-structured data** in its native format. \
                        Unlike data warehouses, which require data to be structured before ingestion, data lakes accept data in its original form. \
                        Data lakes are **ideal for storing diverse data types** and supporting advanced analytics, machine learning, and data exploration.")
        st.info("Some popular data lakes are Amazon S3, Google Cloud Storage, Snowflake and Databricks (among many others).", icon="💡")

    with comparison_tab: 
        st.markdown("Use the following table as a reference guide to check out the main differences between Databases, Data Warehouses, and Data Lakes.")
        df = pd.DataFrame(data={"Database":["Organised into tables with rows and columns, following a predefined schema", "Primarily used for transactional processing and operational tasks, with a focus on structured data"], 
                                "Data Warehouse":["Structured and optimised for analytical queries, with a predefined schema design", "Designed for analytical processing and reporting, handling large volumes of structured data for BI"], 
                                "Data Lake":["Stores raw, unstructured, and semi-structured data without a predefined schema", "Suited for storing structured, semi-structured, and unstructured data, supporting advanced analytics and exploration"]}, 
                          index=["Structure", "Data Type and Usage"])
        st.table(df)
        st.link_button("Click here to learn more", "https://www.mongodb.com/databases/data-lake-vs-data-warehouse-vs-database")


def bigquery_segment():
    st.header("Google BigQuery", help="Click on the tabs below for a refresher on Google BigQuery.")
    st.markdown("Google BigQuery is a fully managed, [serverless](https://en.wikipedia.org/wiki/Serverless_computing) **data warehouse and analytics platform** provided by Google Cloud. \
                It allows you to store, analyse, and query large datasets using SQL-like queries. \
                BigQuery is designed to be scalable, fast, and cost-effective, making it suitable for handling big data workloads.")
    quickstart_tab, structure_tab, tips_tab, references_tab = \
        st.tabs(["Quickstart", "Structure", "Tips", "References"])

    with quickstart_tab:
        st_code_block(caption="You can start exploring BigQuery for free in just a few minutes. Take advantage of BigQuery's sandbox to start loading and querying a [public dataset](https://cloud.google.com/bigquery/public-data) or your own data.",
        )
        st.markdown("")
        st.link_button("Try the BigQuery sandbox", "https://console.cloud.google.com/bigquery", type='primary')
        st.link_button("Read the documentation", "https://cloud.google.com/bigquery/docs/sandbox")
    
    with structure_tab:
        st_code_block("https://cloud.google.com/bigquery/docs/resource-hierarchy", 
                      """
                      As most services in the [Google Cloud Platform](https://cloud.google.com/), BigQuery resources are organized in a hierarchy, where data tables are organized into units called datasets, which are in turn scoped to your current GCP project. Below is a list of key concepts to keep in mind: 
                      - **Project**: it organises all your Google Cloud resources. It is the top-level container in Google Cloud; BigQuery datasets are associated with a project.
                      - **Datasets**: are containers that hold tables, views, and user-defined functions. They provide a logical grouping of related data within BigQuery.
                      - **Tables**: store the actual data in BigQuery. They can be either native or external tables. Native tables store data natively within BigQuery, while external tables reference data stored outside of BigQuery, such as in Google Cloud Storage.
                      - **View**: A virtual table defined by a SQL query. You can query views in a similar way to tables, but they do not store data themselves.
                      - **Columns**: Columns represent individual data fields within a table. Each column has a name, data type, and other optional properties.
                      - **SQL Queries**: BigQuery supports SQL-like queries for retrieving and manipulating data. You can use standard SQL or legacy SQL dialects for querying. 
                      - **Jobs**: When you execute a query or perform an operation in BigQuery, it runs as a job. Jobs can be interactive queries, batch queries, load jobs, or export jobs.
                      """
        )

    with tips_tab:
        st_code_block(caption="""
                      Some useful tips for your learning path:
                      - **Understand the concepts**: Familiarise yourself with the key concepts of BigQuery, such as datasets, tables, and SQL queries.
                      - **Explore sample datasets**: Google provides public datasets that you can explore and analyse to gain hands-on experience with BigQuery. These datasets cover various domains and can help you understand different data scenarios.
                      - **Keep practising**: Remember to experiment and practise with real-world use cases to gain a deeper understanding of its environment. The more you work with the platform, the more proficient you'll become in leveraging its capabilities.
                      - **Use the documentation and resources**: Refer to the official Google BigQuery documentation, tutorials, and sample code to learn more about specific features, best practices, and advanced topics.
                      """)
        st.link_button("Advanced: best practices on query optimisation", "https://cloud.google.com/bigquery/docs/best-practices-performance-compute")

    with references_tab:
        st_code_block(caption="""
                      Below are some useful references and resources to advance your understanding: 
                      - [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs): The official documentation provided by Google is a comprehensive resource that covers all aspects of BigQuery, including getting started guides, SQL reference, best practices, and more.
                      - [Google Cloud Learning Paths](https://www.qwiklabs.com/quests/55): Google Cloud offers learning paths specifically designed for BigQuery (as well as many other Cloud services). These paths provide step-by-step guidance and hands-on labs to help you learn and practise BigQuery concepts. 
                      - [BigQuery Spotlight YT Series](https://www.youtube.com/watch?v=d3MDxC_iuaw&list=PLIivdWyY5sqLAbIdmcMwsxWg-w8Px34MS): The official Google Cloud YouTube channel offers a comprehensive video series that covers the basics of BigQuery; the topics covered include querying, loading and visualising data. 
                      """,
        )



def sql_segment():
    st.header("SQL Cheatsheet", help="Click on the tabs below to explore the different SQL clauses.")
    st.markdown("SQL, or Structured Query Language, is a powerful tool used for managing and manipulating relational databases. It serves as the primary means for communicating with databases, allowing users to perform various operations like retrieving, updating, inserting, and deleting data.")
    create_tab, where_tab, group_tab, order_tab, join_tab, union_tab, subq_tab, window_tab = \
        st.tabs(["SELECT", "WHERE", "GROUP BY", "ORDER BY", "JOIN", "UNION", "SUBQUERY", "WINDOW FUNCTIONS"])
    with create_tab:
        st_code_block("sql_ref_select", 
                      "The `SELECT` clause specifies which columns you want to retrieve, while the `FROM` clause indicates the table from which to retrieve the data.",
        """
        SELECT column1, column2 
        FROM table_name;
        """
        )
        st.info("What if you want to `LIMIT` the number of rows that are returned by your `SELECT` statement?", icon="👉")

        st_code_block("sql_ref_limit", 
                      "The `LIMIT` command specifies the maximum number of rows the result set will have, useful for testing queries or when only a subset of the data is needed.",
        """
        -- limit to the first 10 rows
        SELECT column1, column2
        FROM table_name 
        LIMIT 10;
        """
        )

    with where_tab:
        st_code_block("sql_ref_where", "The `WHERE` clause filters rows based on a specified condition.",
        """
        SELECT column1, column2
        FROM table_name 
        WHERE column2 > 10;
        """
        )
        st.info("The `WHERE` clause cannot be used to filter groups that have been created with a `GROUP BY`. That's what `HAVING` is for; see the `GROUP BY` tab for more on that.", icon="💡")

    with group_tab:
        st_code_block("sql_ref_group_by", 
                      "The `GROUP BY` clause groups rows sharing one or more columns’ categories so that aggregate functions can be applied to each group. It is very useful for creating summaries",
        """
        SELECT column1, COUNT(column2) 
        FROM table_name 
        GROUP BY column1;
        """
        )
        st.info('The HAVING command is used instead of WHERE with aggregate functions.', icon="👉")

        st_code_block("sql_ref_having", 
                      "To be more precise, you can use both the `WHERE` and `HAVING` clauses when you use a `GROUP BY`, however they serve different purposes: \n - The `WHERE` clause is used to filter rows before any grouping takes place. This means if you're using `GROUP BY` in your query, the `WHERE` clause filters which rows are to be included in the groupings based on the criteria you specify. \n - The `HAVING` clause is used to filter groups after they have been formed by the `GROUP BY` clause. It's essentially similar to the `WHERE` clause but is applied at a later stage in the query execution process, allowing you to specify conditions that affect the groups rather than individual rows.",
        """
        SELECT column1, COUNT(column2)
        FROM table_name
        GROUP BY column1
        HAVING COUNT(column2) > 10;
        """
        )

    with order_tab:
        st_code_block("sql_ref_order_by", "The `ORDER BY` clause sorts the result set in ascending `ASC` or descending `DESC` order. The default is `ASC`.",
        """
        SELECT column1 
        FROM table_name 
        ORDER BY column1 DESC;
        """
        )
        st.info("The `ORDER BY ` clause is applied last in query operations, ensuring the final result set is ordered, not the data being processed.", icon="💡")

    with join_tab:
        st_code_block("sql_ref_join", 
                      "The `JOIN` allows you to combines rows from two or more tables, based on a related column between them. The type of join (`INNER`, `LEFT`, `RIGHT`, `FULL OUTER`) determines how rows from the joined tables are combined and returned.",
        """
        SELECT table1.column1, table2.column2 
        FROM table1 LEFT JOIN table2 
        ON table1.common_column = table2.common_column;
        """
        )

    with union_tab:
        st_code_block("sql_ref_union", 
                      "Combines the result sets of two or more `SELECT` statements into a single result set, including only distinct values.",
        """
        SELECT column1, column2 FROM table1
        UNION
        SELECT column1, column2 FROM table2;
        """
        )
        st.info("Each `SELECT` statement within the `UNION` clause must have the same number of columns in the result sets with similar data types.", icon="💡")
        st.info("The `UNION` command autoomatically keeps only distinct values (it deduplicates rows), if you want to keep all the rows use the `UNION ALL` command.", icon="👉")
        st_code_block("sql_ref_union_all", 
                      "Combines the result sets of two or more `SELECT` statements into a single result set, including only distinct values.",
        """
        SELECT column1, column2 FROM table1
        UNION ALL
        SELECT column1, column2 FROM table2;
        """
        )

    with subq_tab:
        st_code_block("https://learnsql.com/blog/sql-subquery-for-beginners/", 
                      "A subquery is a query nested inside another query, used to perform operations that require multiple steps.",
        """
        SELECT column1 
        FROM table1
        WHERE column1 IN (SELECT other_column1 FROM table2);
        """
        )
        st.info("Subqueries are always written between parentheses, depending on the objective, they can appear in different places within the main query - usually within the `SELECT`, `FROM` or `WHERE` clauses.", icon="💡")

    with window_tab:
        st_code_block("https://www.freecodecamp.org/news/window-functions-in-sql/", "Window functions allow you to perform calculations across a set of table rows that are somehow related to the current row. Useful for running totals, moving averages, ranking and much more.",
        """
        SELECT column1, 
            SUM(column2) OVER (PARTITION BY column1) as running_total
        FROM table_name;
        """
        )
        st.info("The `PARTITION BY` attribute is optional but useful for dividing the result set into partitions to apply the window function independently to each partition.", icon="💡")


def super_tab(): 
    st.title("Databases and SQL", help="Click on the tabs below to explore the different sections.")
    tab1, tab2, tab3 = \
        st.tabs(["Types of Databases", "Google BigQuery", "SQL Cheatsheet"])
    with tab1:
        database_segment()
    with tab2: 
        bigquery_segment()
    with tab3:
        sql_segment()

super_tab()
        
