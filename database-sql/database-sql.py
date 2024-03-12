import streamlit as st




def st_code_block(url, caption=None, code=None):
    # prefill the http address for the sql-reference url
    if not url.startswith("https"):
        url = f"https://www.w3schools.com/sql/{url}.asp"
    st.markdown(caption)
    st.code(code, language="sql")
    st.link_button("Read the documentation",url)

def database_segment():
    st.header("🗄 Database", help="The gigantic storage drawer that holds many collections of your data together.")
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
        st.info("What if you want to `LIMIT` the number of rows that are returned by your `SELECT` statement?")

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
        SELECT column1 
        FROM table_name 
        WHERE condition;
        """
        )
        st.info("The `WHERE` clause cannot be used to filter groups that have been created with a `GROUP BY`. That's what `HAVING` is for; see the `GROUP BY` tab for more on that.")

    with group_tab:
        st_code_block("sql_ref_group_by", 
                      "The `GROUP BY` clause groups rows sharing one or more columns’ categories so that aggregate functions can be applied to each group. It is very useful for creating summaries",
        """
        SELECT column1, COUNT(column2) 
        FROM table_name 
        GROUP BY column1;
        """
        )
        st.error('The HAVING command is used instead of WHERE with aggregate functions.', icon="🚨")

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
        st.info("The `ORDER BY ` clause is applied last in query operations, ensuring the final result set is ordered, not the data being processed.")

    with join_tab:
        st_code_block("sql_ref_select", "",
        """
        SELECT column1, column2 
        FROM table_name;
        """
        )

    with union_tab:
        st_code_block("sql_ref_select", "",
        """
        SELECT column1, column2 
        FROM table_name;
        """
        )

    with subq_tab:
        st_code_block("sql_ref_select", "",
        """
        SELECT column1, column2 
        FROM table_name;
        """
        )

    with window_tab:
        st_code_block("sql_ref_select", "",
        """
        SELECT column1, column2 
        FROM table_name;
        """
        )

database_segment()