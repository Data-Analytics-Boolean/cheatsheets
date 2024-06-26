import streamlit as st
import pandas as pd

# Initial page config
st.set_page_config(
    page_title='Databases and SQL Cheat Sheet - Boolean',
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="https://coursereport-s3-production.global.ssl.fastly.net/uploads/school/logo/681/original/Pittogramma-RGB-1080-BLUE-circle.png"
)

# Main function to set up Streamlit app layout
def main(): 
    sidebar_info()
    main_tab() 
    return None

# Code block function
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

# Boolean logo with link to homepage
st.markdown(
    """<a href="https://boolean.careers/?utm_source=streamlit&utm_medium=learn_more&utm_campaign=data_analytics_cheatsheet&utm_content=pagina_home">
    <img src="https://raw.githubusercontent.com/Data-Analytics-Boolean/assets/main/boolean-logo-pill.png" width="200"></a>""",
    unsafe_allow_html=True
    )

# Sidebar info
def sidebar_info(): 
    with st.sidebar: 
        # boolean logo with link to homepage
        st.markdown(
        """<a href="https://boolean.careers/?utm_source=streamlit&utm_medium=learn_more&utm_campaign=data_analytics_cheatsheet&utm_content=pagina_home">
        <img src="https://raw.githubusercontent.com/Data-Analytics-Boolean/assets/main/boolean-logo-pill.png" width="110"></a>""",
        unsafe_allow_html=True
        )
        st.header("About Boolean")
        st.markdown("""
                    Boolean is an online, International tech Academy. 

                    Our mission is to **make training in the tech field more accessible** and smart, giving everyone the opportunity to create a career from scratch. \
                    Every day we continue developing and improving a **teaching method** that allows people to learn complete, concrete and specific concepts in a short time.

                    Transform your career in just 4 months with our **part-time course in Data Analytics**, designed to teach you how to master data analysis. \
                    
                    Enroll now to begin your journey!
                    """)
        # CTA button with link to course page
        st.link_button("Learn more", "https://boolean.careers/corso/data-analytics?utm_source=streamlit&utm_medium=learn_more&utm_campaign=data_analytics_cheatsheet&utm_content=pagina_corso", type="primary")   # IT 🇮🇹
        #st.link_button("Learn more UK 🇬🇧", "https://boolean.co.uk/course/part-time-data-analytics-online-course", type="primary")  

# Definition of second level of tabs (starting from First Tab)
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
# Definition of second level of tabs (starting from Second Tab)
def bigquery_segment():
    st.header("Google BigQuery", help="Click on the tabs below for a refresher on Google BigQuery.")
    st.markdown("Google BigQuery is a fully managed, [serverless](https://en.wikipedia.org/wiki/Serverless_computing) **data warehouse and analytics platform** provided by Google Cloud. \
                It allows you to store, analyse, and query large datasets using SQL-like queries. \
                BigQuery is designed to be scalable, fast, and cost-effective, making it suitable for handling big data workloads.")
    quickstart_tab, structure_tab, tips_tab, resources_tab = \
        st.tabs(["Quickstart", "Structure", "Tips", "Resources"])

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

    with resources_tab:
        st_code_block(caption="""
                      Below are some useful references and resources to advance your understanding: 
                      - [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs): The official documentation provided by Google is a comprehensive resource that covers all aspects of BigQuery, including getting started guides, SQL reference, best practices, and more.
                      - [Google Cloud Learning Paths](https://www.qwiklabs.com/quests/55): Google Cloud offers learning paths specifically designed for BigQuery (as well as many other Cloud services). These paths provide step-by-step guidance and hands-on labs to help you learn and practise BigQuery concepts. 
                      - [BigQuery Spotlight YT Series](https://www.youtube.com/watch?v=d3MDxC_iuaw&list=PLIivdWyY5sqLAbIdmcMwsxWg-w8Px34MS): The official Google Cloud YouTube channel offers a comprehensive video series that covers the basics of BigQuery; the topics covered include querying, loading and visualising data. 
                      """,
        )
# Definition of second level of tabs (starting from Third Tab)
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
                      "The `JOIN` clause is a powerful tool used to combine data from two or more tables based on a specific relationship. \
                        It's like merging information from separate spreadsheets into a single, unified view. \
                        The type of join (`INNER`, `LEFT`, `RIGHT`, `FULL OUTER`) determines how rows from the joined tables are combined and returned.",
        """
        SELECT table1.column1, table2.column2 
        FROM table1 LEFT JOIN table2 
        ON table1.common_column = table2.common_column;
        """
        )
        st.markdown("##### Types of JOINs")
        st.markdown("""
                    There are different types of `JOIN` depending on how you want to handle unmatched rows:
                    - `INNER JOIN`: This is probably one of the most common types. It only includes rows where there's a match in both tables. 
                    - `LEFT JOIN`: This includes all rows from the left table (usually the "main" table), even if there's no match in the right table. Empty values (nulls) are used for unmatched rows in the right table. 
                    - `RIGHT JOIN`: Similar to `LEFT JOIN`, but includes all rows from the *right* table and fills unmatched rows in the left table with empty values.
                    - `FULL JOIN`: This combines all rows from both tables, regardless of whether there's a match. 
                    """)
        st.image('database-sql/img/joins.png')
        st.info("You can also `JOIN` a table with itself (in what is called a self `JOIN`). It can be useful especially in situations where the data presents a hierarchical relationship among its observations.", icon="💡")
        st.link_button("Read more on the four types of JOIN", "https://learnsql.com/blog/sql-joins-types-explained/")
        st.link_button("Read more on the self JOIN", "https://learnsql.com/blog/illustrated-guide-sql-self-join/")

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
# Definition of second level of tabs (starting from Fourth Tab)
def sql_extra_segment(): 
    st.header("SQL Extras", help="Click on the tabs below for some extras on SQL.")
    st.markdown("In this section you will find additional useful information, best practices and resources to enhance your understanding of SQL and boost your learning curve.")
    order_ops_tab, tips_sql_tab, mistakes_tab, resources_sql_tab = \
        st.tabs(["Order of Operations", "Tips", "Common Mistakes", "Resources"])

    with order_ops_tab:
        st_code_block(caption="""
                      Understanding the order in which SQL clauses are executed can help in writing more efficient and correct queries. The general order of execution is:
                      - `FROM` and `JOIN`: Determine the total working dataset.
                      - `WHERE`: Filters rows before grouping.
                      - `GROUP BY`: Groups rows with the same values into summary rows.
                      - `HAVING`: Filters groups created by GROUP BY.
                      - `SELECT`: Specifies which columns to display in the final result.
                      - `ORDER BY`: Sorts the final result set.
                      - `LIMIT`: Limits the number of rows returned.
                      """,
        )
        st.info("Remember, this order affects how data is processed and filtered through the query's lifecycle, influencing both the performance and the outcome of your SQL commands.", icon="💡")

    with tips_sql_tab:
        st_code_block(caption="""
                      Below are some tips to help in your learning path: 
                      - **Practice Regularly**: Consistent practice is key to mastering SQL. Work on various exercises, the public datasets repository and real-world problems to reinforce your understanding.
                      - **Understand Data Types**: Familiarise yourself with different data types (e.g., integer, string, date) as they impact SQL query construction and data manipulation.
                      - **Utilise Online Resources**: Take advantage of online tutorials, forums, and documentation to enhance your learning experience. Websites like W3Schools, Stack Overflow, and the official Google BigQuery documentation can be valuable resources.
                      """
        )

    with mistakes_tab:
        st_code_block(caption="""
                      Below are some of the common mistakes to keep in mind when writing a SQL statement:
                      - **Forgetting to specify the database**: It's important to specify the database you're working with before writing queries. Beginners may forget to include the proper database name, resulting in errors or querying the wrong database.
                      - **Misspelling column or table names**: Typos in column or table names can lead to errors. Beginners should double-check the spelling and ensure they are using the correct case (SQL is usually case-insensitive, but it's good practice to be consistent).
                      - **Missing or incorrect syntax**: SQL has specific syntax rules, and beginners may forget to include necessary keywords or use them incorrectly. For example, forgetting to include a semicolon at the end of a query or misplacing parentheses in complex conditions.
                      - **Not using aliases or table prefixes**: When joining tables or using subqueries, beginners may forget to use aliases or table prefixes to differentiate columns between tables, leading to ambiguous column references.
                      - **Improper use of WHERE and HAVING clauses**: Beginners may confuse the use of WHERE and HAVING clauses. WHERE is used to filter rows before grouping, while HAVING is used to filter grouped data. Mixing them up can lead to incorrect results.
                      """
        )

    with resources_sql_tab:
        st_code_block(caption="""
                      Below are some resources and links to help you in your learning path:
                      - [Google BigQuery documentation](https://cloud.google.com/bigquery/docs/introduction): It goes without saying, read the official documentation!
                      - [Stack Overflow](https://stackoverflow.com/questions/tagged/sql): Chances are, someone has already asked your question here.
                      - [SQLZoo](https://sqlzoo.net/): An interactive SQL tutorial with exercises.
                      - [W3Schools SQL Tutorial](https://www.w3schools.com/sql/): A comprehensive SQL tutorial with examples.
                      - [Mode Analytics SQL Tutorial](https://mode.com/sql-tutorial/): A step-by-step SQL tutorial with a focus on data analysis.
                      - [YouTube: SQL - Full Course for Beginners](https://www.youtube.com/watch?v=HXV3zeQKqGY): A video tutorial covering SQL fundamentals.
                      """
        )

# Definition of first level of tabs (calling the second level tabs)
def main_tab(): 
    st.title("Databases and SQL", help="Click on the tabs below to explore the different sections.")
    tab1, tab2, tab3, tab4 = \
        st.tabs(["Types of Databases", "Google BigQuery", "SQL Cheatsheet", "SQL Extras"])
    with tab1:
        database_segment()
    with tab2: 
        bigquery_segment()
    with tab3:
        sql_segment()
    with tab4:
        sql_extra_segment()
        
if __name__ == "__main__": 
    main()    