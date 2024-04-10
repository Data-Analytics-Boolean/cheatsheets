import streamlit as st
import pandas as pd

# Initial page config
st.set_page_config(
    page_title='Data Week Cheatsheet - Boolean',
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="https://coursereport-s3-production.global.ssl.fastly.net/uploads/school/logo/681/original/Pittogramma-RGB-1080-BLUE-circle.png"
)

# Main function to set up Streamlit app layout
def main(): 
    sidebar_info()
    main_tab()
    return None

# PDF downloader function
def pdf_download(name):
    # PDF download
    with open(f"data-week/pdf_cheatsheets/{name}.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="Download PDF Cheatsheet",
                        data=PDFbyte,
                        file_name=f"{name}.pdf",
                        mime='application/octet-stream', 
                        help="*Source: DataCamp*", 
                        type="primary")

# Boolean logo with link to homepage
st.markdown(
    """<a href="https://boolean.careers/?utm_source=streamlit&utm_medium=learn_more&utm_campaign=data_analytics_cheatsheet_dataweek&utm_content=pagina_home">
    <img src="https://raw.githubusercontent.com/Data-Analytics-Boolean/assets/main/boolean-logo-pill.png" width="200"></a>""",
    unsafe_allow_html=True
    )

# Sidebar info
def sidebar_info(): 
    with st.sidebar: 
        # boolean logo with link to homepage
        st.markdown(
        """<a href="https://boolean.careers/?utm_source=streamlit&utm_medium=learn_more&utm_campaign=data_analytics_cheatsheet_dataweek&utm_content=pagina_home">
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
        st.link_button("Learn more", "https://boolean.careers/corso/data-analytics?utm_source=streamlit&utm_medium=learn_more&utm_campaign=data_analytics_cheatsheet_dataweek&utm_content=pagina_corso", type="primary")   # IT 🇮🇹
        #st.link_button("Learn more UK 🇬🇧", "https://boolean.co.uk/course/part-time-data-analytics-online-course?utm_source=streamlit&utm_medium=learn_more&utm_campaign=data_analytics_cheatsheet_dataweek&utm_content=pagina_corso", type="primary")  

# Definition of second level of tabs (starting from First Tab)
def google_colab():
    #st.markdown("""<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Google_Colaboratory_SVG_Logo.svg/1200px-Google_Colaboratory_SVG_Logo.svg.png" width="100">""",
    #                unsafe_allow_html=True)
    st.subheader("Google Colaboratory")
    st.markdown("Colaboratory, or 'Colab' for short, allows one to write and run python code through the browser and is particularly suited for machine learning, \
                data analysis and training. More technically, Colab is a hosted Jupyter notebook service that requires no configuration to use while providing free \
                access to computing resources, including GPUs.")
    st.markdown("Click on the following button to access Google Colab.")
    st.link_button("Get started with Colab", "https://colab.research.google.com/", type='primary')
    st.markdown(" ")
    with st.expander(""":point_up: **You can also access Colab from your Google Drive. :orange[Click here] for instructions.**"""):
        st.markdown("> First, you'll need to install Colab in your Google Drive from the Google Workspace Marketplace.")
        st.markdown("""<img src="https://raw.githubusercontent.com/Data-Analytics-Boolean/assets/main/cheatsheets/dw_colab_01.png" width="900">""",
                    unsafe_allow_html=True)
        st.markdown("> Then, you can just create a new Google Colaboratory document just like you would create a new spreadsheet with Google Sheets.")
        st.markdown("""<img src="https://raw.githubusercontent.com/Data-Analytics-Boolean/assets/main/cheatsheets/dw_colab_02.png" width="900">""",
                    unsafe_allow_html=True)
    st.markdown("Click on the following button for an official introduction to Colab's features.")
    st.link_button("Overview of Colab", "https://colab.research.google.com/notebooks/basic_features_overview.ipynb#scrollTo=JyG45Qk3qQLS")

# Definition of second level of tabs (starting from Third Tab)
def cheatsheets(): 
    python_tab, pandas_tab, seaborn_tab = st.tabs(["python", "pandas", "seaborn"])
    
    with python_tab:
        about, c_sheet = st.tabs(["About", "Cheatsheet"])
        with about: 
            st.markdown("#### About Python")
            st.markdown("""
                        Created by the Dutch programmer Guido van Rossum and first released in 1991, \
                        [Python](https://www.python.org/) is a high-level, interpreted programming language that: 
                        - is :grey[(relatively)] **easy to learn**
                        - is **easy to read** thanks to indentation
                        - is a free, **open source** software
                        - is used for many **different purposes**, like building websites, web applications, data analysis, machine learning and much more 
                        - is in **high demand**
                        - has a great **community** of users and well written **documentation**
                        """)

            st.link_button("Read the Docs", "https://www.python.org/doc/")
        with c_sheet:
            st.markdown("#### Python Cheatsheet")
            st.caption("*Credits: this section is largely inspired by [fralfaro](https://github.com/fralfaro)'s cheatsheet.*")
            # PDF download
            pdf_download("python-basics-cheatsheet")

            col1, col2, col3 = st.columns(3)  # Create columns for layout

            ### COLUMN 1
            with col1: 
                # Hello, World!
                st.markdown('#### Hello, World!')
                st.code('''
                print("Hello, World!")
                # This is a comment
                    ''')

                # Variables and Data Types
                st.markdown('#### Variables and Data Types')
                st.code('''
                x = 5               # Integer
                y = 3.14            # Float
                name = "John"       # String
                is_student = True   # Boolean
                    ''')

                # Basic Operations
                st.markdown('#### Basic Operations')
                st.code('''
                # Perform basic arithmetic operations
                sum_result = x + y
                sub_result = x - y
                mul_result = x * y
                div_result = x / y
                    ''')

                # String Operations
                st.markdown('#### String Operations')
                st.code('''
                # String concatenation
                full_name = name + " John"

                # Formatted string
                f_string = f"Hello, {name}!"
                    ''')

                # Input and Output
                st.markdown('#### Input and Output')
                st.code('''
                # Get user input and display it
                user_input = input("Enter a number: ")
                print("You entered:", user_input)
                    ''')

                # File Handling
                st.markdown('#### File Handling')
                st.code('''
                # Read content from a file
                with open("file.txt", "r") as file:
                    content = file.read()

                # Write content to a new file
                with open("new_file.txt", "w") as new_file:
                    new_file.write("Hello, world!")
                    ''')
                
                # Error Handling
                st.markdown('#### Error Handling')
                #st.info("""
                #        When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
                #        These exceptions can be handled using the try statement.""")
                st.code('''
                # Try to perform division
                try:
                    result = x / y  # Attempt to divide x by y
                except ZeroDivisionError as e:  # If a ZeroDivisionError occurs
                    print("Cannot divide by zero")  
                    print(e)
                    ''')
                st.link_button("Read more on try-except", 
                            "https://www.w3schools.com/python/python_try_except.asp", 
                            type='primary')

            
            with col2: 
                #st.markdown("### Data Structures", 
                #            help="Data structures are the building blocks of your Python program, they each specify a particular way of organising data so it can be accessed in the most efficient way.")
                # Lists
                st.markdown('#### Lists')
                #st.info("""
                #            Lists in Python are used to store multiple items in a single variable that:
                #            - are ordered
                #            - are changeable
                #            - allow duplicate values
                #            """)

                # Creating lists
                st.markdown('Creating Lists')
                st.code('''
                # Create lists with [], elements separated by commas
                x = [1, 3, 2]
                    ''')

                # List functions and methods
                st.markdown('List Functions and Methods')
                st.code('''
                # Return a sorted copy of the list e.g., [1,2,3]
                sorted_list = sorted(x)

                x.sort()   # for inplace sorting

                # Reverse the order of elements in x e.g., [2,3,1]
                reversed_list = list(reversed(x))

                x.reverse()   # for inplace reversing

                # Count the nr. of "2" in the list
                count_2 = x.count(2)
                    ''')

                # Selecting list elements
                st.markdown('Indexing List Elements')
                st.code('''
                # Select the 0th element in the list
                element_0 = x[0]

                # Select the last element in the list
                last_element = x[-1]

                # Select 1st (inclusive) to 3rd (exclusive)
                subset_1_to_3 = x[1:3]

                # Select the 2nd to the end
                subset_2_to_end = x[2:]

                # Select 0th to 3rd (exclusive)
                subset_0_to_3 = x[:3]
                    ''')

                # Concatenating lists
                st.markdown('Concatenating Lists')
                st.code('''
                # Define the x and y lists
                x = [1, 3, 6]
                y = [10, 15, 21]

                # Concatenate lists using '+'
                concatenated_list = x + y

                # Replicate elements in a list using '*'
                replicated_list = 3 * x
                    ''')
                
                # List Comprehensions
                st.markdown('List Comprehensions')
                st.code('''
                # Create a list of squared numbers using a list comprehension
                squared_numbers = [num**2 for num in numbers]

                # Create a list of even numbers using a list comprehension with condition
                even_numbers = [num for num in numbers if num % 2 == 0]
                    ''')

                # Dictionaries
                st.markdown('#### Dictionaries')
                #st.info("""
                #        Dictionaries in Python are used to store data in a collection of `key:value` pairs which:
                #        - are ordered
                #        - are changeable
                #        - do not allow duplicates
                #        """)

                # Creating dictionaries
                st.markdown('Creating Dictionaries')
                st.code('''
                # Create a dictionary with {}
                my_dict = {'a': 1, 'b': 2, 'c': 3}

                    ''')

                # Dictionary functions and methods
                st.markdown('Dictionary Functions and Methods')
                st.code('''
                # Get the keys of a dictionary
                my_dict.keys()  # Returns dict_keys(['a', 'b', 'c'])

                # Get the values of a dictionary
                my_dict.values()  # Returns dict_values([1, 2, 3])
                
                # Get a value from a dictionary by specifying the key
                my_dict['a']  # Returns 1  
                    ''')
                
                st.link_button("More on Data Structures", 
                            "https://realpython.com/python-data-structures/", 
                            type="primary")

            with col3: 
                #st.markdown("#### :orange[Control Structures]")
                #st.info("""
                #            Control structures will be among the most important building blocks of your Python program. They analyze variables and choose directions in which to go based on predetermined conditions specified by the programmer. The basic control structures are:
                #            - **Sequential**: this is the default mode, it's just a set of statements that are executed in sequence
                #            - **Conditionals**: they are used to execute one or more statements **if** a condition is met
                #            - **Loops**: their purpose is to repeat a statement **for** a certain number of times or **while** a condition is fulfilled.
                #            """)

                # Conditional Statements
                st.markdown('#### Conditional Statements')
                st.code('''
                # Check if x is greater than y
                if x > y:
                    print("x is greater")
                # If not, check if x is less than y
                elif x < y:
                    print("y is greater")
                # If neither condition is true, they must be equal
                else:
                    print("x and y are equal")
                    ''')

                # Loops
                st.markdown('#### Loops')
                st.code('''
                # For loop
                numbers = [1, 2, 3, 4, 5]
                for num in numbers:
                    print(num)

                # While loop
                x = 5
                while x > 0:
                    print(x)
                    x -= 1
                    ''')
                st.link_button("Read more on control structures", 
                            "https://www.educative.io/answers/what-are-control-flow-statements-in-python", 
                            type='primary')
                
                # Functions
                st.markdown('#### Functions')
                #st.info("""
                #        If you find yourself writing the same lines of code more than twice, maybe it's time to write a function. \n 
                #        Functions are blocks of code to which you give a name so that you can easily execute it as many times as you want.  \n
                #        You can also pass parameters to a function, which allows you to add control and customisation to it.
                #        """)
                st.code('''
                # Define a function that takes a name parameter
                def greet(name):
                    return f"Hello, {name}!"

                # Call the greet function with the argument "Alice"
                greeting = greet("Alice")
                    ''')
                st.link_button("More on Python functions", 
                            "https://realpython.com/defining-your-own-python-function/", 
                            type="primary")

                # Built-in Functions
                st.markdown('#### Built-in Functions')
                st.code('''
                # Get the length of a list
                len_fruits = len(fruits)

                # Find the maximum value in a list
                max_number = max(numbers)

                # Find the minimum value in a list
                min_number = min(numbers)
                    ''')
                #st.link_button("Python's built-in functions", 
                #            "https://docs.python.org/3/library/functions.html", 
                #            type='primary')

                # Importing Modules
                st.markdown('#### Importing Libraries and Modules')
                st.code('''
                import math
                sqrt_result = math.sqrt(x)  # Calculate square root using math module

                from random import randint
                random_number = randint(1, 10)  # Generate a random number between 1 and 10
                    ''')
                st.link_button("More on libraries vs modules", 
                            "https://realpython.com/lessons/scripts-modules-packages-and-libraries/", 
                            type='primary')
                

                # Classes and Objects
                st.markdown('#### Classes and Objects')
                #st.info("""
                #        Python is an object oriented programming language and almost everything in Python is an object, with its properties and methods. \n
                #        A Class is like an object constructor, or a "blueprint" for creating objects.
                #        """)
                st.code('''
                        class Dog:
                            def __init__(self, name, age):
                                self.name = name
                                self.age = age

                            def bark(self):
                                return "Woof!"

                        my_dog = Dog("Buddy", 3)
                        ''')
                st.link_button("Learn more on Classes", 
                            "https://realpython.com/python-classes/", 
                            type="primary")

    with pandas_tab:
        about, c_sheet = st.tabs(["About", "Cheatsheet"])
        with about: 
            st.subheader("About pandas")
            st.markdown("""
                        [Pandas](https://pandas.pydata.org/) is built on NumPy and provides easy-to-use
                        data structures and data analysis tools for the Python programming language.
                        """)
            st.link_button("Read the Docs", "https://pandas.pydata.org/docs/")

            # Pandas installation and import
            st.markdown('__Install and import Pandas__')
            st.code('$ pip install pandas')
            st.code('''
                    # Import Pandas convention
                    import pandas as pd
                    ''')

            # Pandas array creation
            st.subheader('Pandas Data Structures')
            st.markdown('__Series__')
            st.markdown("""
                        <img src="https://raw.githubusercontent.com/Data-Analytics-Boolean/assets/main/cheatsheets/pd_series.png" width="150">""", 
                        unsafe_allow_html=True)

            st.markdown('''
                        <small>A **one-dimensional** labeled array a capable of holding any data type.</small>
                        ''', unsafe_allow_html=True)

            st.code('''
                    # Create a pandas Series
                    s = pd.Series(
                        [3, -5, 7, 4],
                        index=['a', 'b', 'c', 'd']
                    )
                    ''')

            st.markdown('__DataFrame__')
            st.markdown("A **two-dimensional** labeled data structure with columns of potentially different types.")
            st.markdown("""
                        <img src="https://raw.githubusercontent.com/Data-Analytics-Boolean/assets/main/cheatsheets/pd_dataframe.png" width="400">""", 
                        unsafe_allow_html=True)

            st.code('''
            # Create a pandas DataFrame
            data = {
                'Country': ['Belgium', 'India', 'Brazil'],
                'Capital': ['Brussels', 'New Delhi', 'Brasília'],
                'Population': [11190846, 1303171035, 207847528]
            }
            df = pd.DataFrame(
                data,
                columns=['Country', 'Capital', 'Population']
            )
            ''')
        with c_sheet:
            st.markdown("#### pandas Cheatsheet")
            st.caption("*Credits: this section is largely inspired by [fralfaro](https://github.com/fralfaro)'s cheatsheet.*") 
            # PDF download
            pdf_download("python-pandas-cheatsheet")

            col1, col2, col3 = st.columns(3)  # Create columns for layout

            #######################################
            # COLUMN 1
            #######################################

            # Read and Write to CSV
            col1.subheader('Read and Write to CSV')
            col1.code('''
            # Read from CSV
            df_read = pd.read_csv(
                'file.csv',
                    header=None, 
                    nrows=5
            )

            # Write to CSV
            df.to_csv('myDataFrame.csv')
                ''')

            # Read and Write to Excel
            col1.subheader('Read and Write to Excel')
            col1.code('''
            # Read from Excel
            df_read_excel = pd.read_excel('file.xlsx')

            # Write to Excel
            df.to_excel(
                'dir/myDataFrame.xlsx', 
                sheet_name='Sheet1'
            )

            # Read multiple sheets from the same file
            xlsx = pd.ExcelFile('file.xls')
            df_from_sheet1 = pd.read_excel(xlsx, 'Sheet1')
                ''')

            # Read and Write to SQL Query or Database Table
            col1.subheader('Read and Write to SQL Query or Database Table')
            col1.code('''
            from sqlalchemy import create_engine
            engine = create_engine('sqlite:///:memory:')

            # Read from SQL Query
            pd.read_sql("SELECT * FROM my_table;", engine)

            # Read from Database Table
            pd.read_sql_table('my_table', engine)

            # Read from SQL Query using read_sql_query()
            pd.read_sql_query("SELECT * FROM my_table;", engine)

            # Write DataFrame to SQL Table
            pd.to_sql('myDf', engine)
                ''')


            # Getting Elements from Series and DataFrame
            col1.subheader('Getting Elements')
            col1.code('''
            # Get one element from a Series
            s['b']
            # Output: -5

            # Get subset of a DataFrame
            df[1:]
            # Output:
            #    Country     Capital  Population
            # 1    India   New Delhi  1303171035
            # 2   Brazil    Brasília   207847528
                ''')

            # Asking For Help
            col1.subheader('Asking For Help')
            col1.code('''
            # Display help for a function or object
            help(pd.Series.loc)
                ''')

            #######################################
            # COLUMN 2
            #######################################

            # Selecting, Boolean Indexing & Setting
            col2.subheader('Selecting, Boolean Indexing & Setting')
            col2.code('''
            # Select single value by row & 'Belgium' column
            df.iloc[[0],[0]]
            # Output: 'Belgium'

            # Select single value by row & 'Belgium' column labels
            df.loc[[0], ['Country']]
            # Output: 'Belgium'

            # Select single row of subset of rows
            df.loc[2]
            # Output:
            # Country     Brazil
            # Capital    Brasília
            # Population 207847528

            # Select a single column of subset of columns
            df.loc[:,'Capital']
            # Output:
            # 0     Brussels
            # 1    New Delhi
            # 2     Brasília

            # Boolean indexing - Series s where value is not > 1
            s[~(s > 1)]

            # Boolean indexing - s where value is <-1 or >2
            s[(s < -1) | (s > 2)]

            # Use filter to adjust DataFrame
            df[df['Population'] > 1200000000]

            # Setting index a of Series s to 6
            s['a'] = 6
                ''')

            # Dropping
            col2.subheader('Dropping')
            col2.code('''
            # Drop values from rows (axis=0)
            s.drop(['a', 'c'])

            # Drop values from columns (axis=1)
            df.drop('Country', axis=1)
                ''')

            # Sort & Rank
            col2.subheader('Sort & Rank')
            col2.code('''
            # Sort by labels along an axis
            df.sort_index()

            # Sort by the values along an axis
            df.sort_values(by='Country')

            # Assign ranks to entries
            df.rank()
                ''')

            # Applying Functions
            col2.subheader('Applying Functions')
            col2.code('''
            # Define a function
            f = lambda x: x*2

            # Apply function to DataFrame
            df.apply(f)

            # Apply function element-wise
            df.applymap(f)
                ''')

            #######################################
            # COLUMN 3
            #######################################

            # Basic Information
            col3.subheader('Basic Information')
            col3.code('''
            # Get the shape (rows, columns)
            df.shape

            # Describe index
            df.index

            # Describe DataFrame columns
            df.columns

            # Info on DataFrame
            df.info()

            # Number of non-NA values
            df.count()
                ''')

            # Summary
            col3.subheader('Summary')
            col3.code('''
            # Sum of values
            df[col].sum()

            # Cumulative sum of values
            df[col].cumsum()

            # Minimum/maximum values
            df[col].min()
            df[col].max()

            # Index of minimum/maximum values
            df[col].idxmin()
            df[col].idxmax()

            # Summary statistics
            df[col].describe()

            # Mean of values
            df[col].mean()

            # Median of values
            df[col].median()
                ''')

            # Internal Data Alignment
            col3.subheader('Internal Data Alignment')
            col3.code('''
            # Create Series with different indices
            s3 = pd.Series([7, -2, 3], index=['a', 'c', 'd'])

            # Add two Series with different indices
            result = s + s3
                ''')

            # Arithmetic Operations with Fill Methods
            col3.subheader('Arithmetic Operations with Fill Methods')
            col3.code('''
            # Perform arithmetic operations with fill methods
            result_add = s.add(s3, fill_value=0)
            result_sub = s.sub(s3, fill_value=2)
            result_div = s.div(s3, fill_value=4)
            result_mul = s.mul(s3, fill_value=3)
                ''')

    with seaborn_tab: 
        about, c_sheet = st.tabs(["About", "Cheatsheet"])
        with about: 
            st.subheader('About seaborn')
            st.markdown('''
                        [Seaborn](https://seaborn.pydata.org/index.html) is a library for making statistical graphics in Python. \
                        It builds on top of [matplotlib](https://matplotlib.org/) and integrates closely with [pandas](https://pandas.pydata.org/) data structures.
                        ''')
            st.link_button("Read the Docs", "https://seaborn.pydata.org/tutorial.html")
            # seaborn installation and import
            st.markdown('**Install and import seaborn**')
            st.code('$ pip install seaborn')
            st.code('''
                    # Import seaborn convention
                    import seaborn as sns
                    ''')
            # Anatomy of a figure
            st.markdown('''**Anatomy of a figure**  
                        Since seaborn is based on Matplotlib, it is important to understanding the anatomy of a Matplotlib **figure**, \
                        which refers to the overall canvas or window that contains one or more individual plots or subplots. 
                        ''')
            st.markdown("""
            <img src="https://raw.githubusercontent.com/Data-Analytics-Boolean/assets/main/cheatsheets/mlp_figure.png" width="600">""", 
            unsafe_allow_html=True)
            st.markdown("")
            # Example code for the workflow
            st.markdown("Get started with the following basic code snippet. ")
            st.code('''
            # Import libraries
            import matplotlib.pyplot as plt
            import seaborn as sns

            # Apply the default theme
            sns.set_theme()

            # Load an example dataset
            iris = sns.load_dataset("iris")

            # Create a scatterplot
            sns.scatterplot(
                data=iris, 
                x='sepal_length', y='sepal_width', 
                hue='species'
            )
            plt.show()
                    ''')
            st.markdown("""
                        <img src="https://raw.githubusercontent.com/Data-Analytics-Boolean/assets/main/cheatsheets/dw_colab_03.png" width="550">""", 
                        unsafe_allow_html=True)
        with c_sheet: 
            st.markdown("#### Seaborn Cheatsheet")
            st.caption("*Credits: this section is largely inspired by [datacamp](https://www.datacamp.com/cheat-sheet/python-seaborn-cheat-sheet)'s cheatsheet.*") 
            # PDF download
            pdf_download("python-seaborn-cheatsheet")
            col1, col2, col3 = st.columns(3)  # Create columns for layout

            #######################################
            # COLUMN 1
            #######################################

            # Prepare the Data
            col1.subheader('Setup and data prep')

            col1.code('''
            # import the libraries 
            # > use the conventional aliases
            import matplotlib.pyplot as plt
            import seaborn as sns
                ''')

            ## Import the data
            col1.code('''
            # let's generate a sample DataFrame
            import pandas as pd
            import numpy as np
            uniform_data = np.random.rand(10, 12)
            data = pd.DataFrame({
                      'x':np.arange(1,101), 
                      'y':np.random.normal(0,4,100)})
                ''')
            col1.code('''
            # seaborn also offers buil-in datasets
            sns.get_dataset_names()
            iris = sns.load_dataset("iris")
            flights = sns.load_dataset("flights")
            tips = sns.load_dataset("tips")
                ''')
            col1.link_button("List of built-in datasets", "https://github.com/mwaskom/seaborn-data")

            ## Figure aesthetics
            col1.subheader('Figure Aesthetics')
            col1.code('''
            # create a figure (of size 5x6 inches) and one subplot
            f, ax = plt.subplots(figsize=(5,6))
            ''')

            ## Seaborn styles
            col1.markdown("**Seaborn styles**")
            col1.code('''
            # set the seaborn defaults and 
            # the matplotlib parameters
            sns.set()
            sns.set_style("whitegrid")
            sns.set_style("ticks",
                  {"xtick.major.size":8,
                  "ytick.major.size":8})
            ''')
            col1.link_button("Aesthetics Tutorial", "https://seaborn.pydata.org/tutorial/aesthetics.html")

            ## Color palette
            col1.markdown("**Color palette**")
            col1.code('''
            # define the color palette
            sns.set_palette("husl", 3)
            
            # set your own color palette
            flatui = ["#9b59b6" "#3498db" "#95a5a6" "#e74c3c" "#34495e" "#2ecc71"]
            sns.set_palette(flatui)
            ''')
            col1.link_button("Check seaborn's color palette", "https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette")


            #######################################
            # COLUMN 2
            #######################################

            # Plotting
            col2.subheader('Plotting with seaborn')
            
            # scatterplot
            col2.markdown("""**Scatterplot**  
                          Useful to visualize the relationship between two numeric variables.""")
            col2.code('''
            # create a scatterplot
            sns.scatterplot(data=iris, 
                            x='sepal_length', 
                            y='sepal_width', 
                            hue='species')
            ''')
            
            # lineplot
            col2.markdown("""**Lineplot**  
                          Useful to understand changes in one variable as a function of time.""")
            col2.code('''
            # create a lineplot
            sns.lineplot(data=flights, 
                         x='year', 
                         y='passengers', 
                         hue='month')
            ''')
            
            # barplot
            col2.markdown("**Barplot**")
            col2.code('''
            # create a barplot
            sns.barplot(data=flights, 
                        x='month', 
                        y='passengers', 
                        ci=None, 
                        color='c')
            ''')
            col2.info("For a horizontal bar chart you can simply swap the 'x' and 'y' variables.", icon="💡")

            # countplot
            col2.markdown("""**Countplot**  
                          Useful to count of the number of observations in each category of a certain variable.""")
            col2.code('''
            # create a countplot
            sns.countplot(data=tips, 
                          y='sex', 
                          color='c')
            ''')

            # histogram
            col2.markdown("""**Histogram**  
                          Useful to visualise the distribution of one or more numeric variables.""")
            col2.code('''
            # create a histogram
            penguins = sns.load_dataset("penguins")
            sns.histplot(penguins, 
                         x="flipper_length_mm")
                      
            # overlapping histograms according to species
            sns.histplot(penguins, 
                         x="flipper_length_mm", 
                         hue="species")
            ''')

            # boxplot
            col2.markdown("""**Boxplot**  
                          Another plot to investigate distributions, it shows the three quartile values of the distribution along with extreme values.""")
            col2.code('''
            # create a boxplot
            sns.boxplot(data=penguins, 
                        x='body_mass_g')
            
            # adding a categorical variable allows 
            # you to compare distributions 
            sns.boxplot(data=penguins, 
                        x='body_mass_g', 
                        y='sex')
            ''')

            col2.link_button("More on seaborn's plotting functions", "https://seaborn.pydata.org/tutorial.html#plotting-functions")

            #######################################
            # COLUMN 3
            #######################################

            
            col3.subheader('Further Customizations')
            # Plot parameters
            col3.markdown("""**Plot parameters**""")
            col3.code('''
            plt.title("Your Title")   # add plot title
            plt.ylabel("your y label")   # adjust the label of the y-axis
            plt.xlabel("your x label")   # adjust the label of the x-axis
            plt.ylim(0,100)   # adjust the limits of the y-axis
            plt.xlim(0,10)   # adjust the limits of the x-axis
            ''')

            # Show or save plot
            col3.markdown("**Show or save plot**")
            col3.code('''
            plt.show()   # show the plot
            plt.savefig("fiure.png")   # save the plot as a figure
            plt.savefig("fiure.png", transparent=True)   # save transparent figure
            ''')

            # Close and clear
            col3.markdown("**Close and clear**")
            col3.code('''
            plt.cla()   # clear an axis
            plt.clf()   # clear an entire figure
            plt.close()   # close a window
            ''')

# Definition of first level of tabs (calling the second level tabs)
def main_tab(): 
    st.title("Cheatsheet for the Boolean Data Week", help="Click on the tabs below to explore the different sections.")
    st.markdown("""
                In the following tabs you will find: 
                - a short guide showing you how to use Python in the web using Google Colaboratory 
                - a series of cheatsheets on the most common Python commands, functions and libraries for data analysis.
                """)
    tab1, tab2 = \
        st.tabs(["Google Colab", "Cheatsheets"])
    with tab1:
        google_colab()
    with tab2:
        cheatsheets()


if __name__ == "__main__": 
    main()    
