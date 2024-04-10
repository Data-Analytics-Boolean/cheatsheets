import streamlit as st
import pandas as pd

# Initial page config
st.set_page_config(
    page_title='Python Cheat Sheet - Boolean',
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
    with open(f"python/pdf_cheatsheets/{name}.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(label="Download PDF Cheatsheet",
                        data=PDFbyte,
                        file_name=f"{name}.pdf",
                        mime='application/octet-stream', 
                        help="*Source: DataCamp*", 
                        type="primary")

# Boolean logo with link to homepage
st.markdown(
    """<a href="https://boolean.careers/?utm_source=streamlit&utm_medium=learn_more&utm_campaign=data_analytics_cheatsheet_py&utm_content=pagina_home">
    <img src="https://raw.githubusercontent.com/Data-Analytics-Boolean/assets/main/boolean-logo-pill.png" width="200"></a>""",
    unsafe_allow_html=True
    )

# Sidebar info
def sidebar_info(): 
    with st.sidebar: 
        # boolean logo with link to homepage
        st.markdown(
        """<a href="https://boolean.careers/?utm_source=streamlit&utm_medium=learn_more&utm_campaign=data_analytics_cheatsheet_py&utm_content=pagina_home">
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
        st.link_button("Learn more", "https://boolean.careers/corso/data-analytics?utm_source=streamlit&utm_medium=learn_more&utm_campaign=data_analytics_cheatsheet_py&utm_content=pagina_corso", type="primary")   # IT 🇮🇹
        #st.link_button("Learn more UK 🇬🇧", "https://boolean.co.uk/course/part-time-data-analytics-online-course", type="primary")  

# Definition of second level of tabs (starting from First Tab)
def python_install():
    st.subheader("Python Anaconda and VS Code Installation", help="Click on the tab corresponding to your Operating System.")
    st.markdown("This guide will show you how to download Python using the Anaconda distribution and install VS Code according to your operating system. ")
    win, mac = \
        st.tabs(["Windows", "Mac/Linux"])
    with win:
        st.markdown("""
                    #### Python Installation
                    - Visit the Anaconda website at https://www.anaconda.com/products/individual and download the Anaconda Individual Edition installer for Windows.
                    - Once the download is complete, run the installer.
                    - Follow the on-screen instructions to complete the installation. Make sure to check the box that says "Add Anaconda to my PATH environment variable" during the installation process.
                    - After the installation is finished, open the Anaconda Navigator from the Start menu.
                    - In the Anaconda Navigator, you can launch Jupyter Notebooks or other Python IDEs like Spyder or JupyterLab.
                    """)
        st.link_button("Download Anaconda", "https://www.anaconda.com/products/individual")
        st.markdown("""
                    #### VS Code Installation 
                    - Visit the Visual Studio Code website at https://code.visualstudio.com/ and download the Visual Studio Code installer for Windows.
                    - Once the download is complete, run the installer.
                    - Follow the on-screen instructions to complete the installation. Leave the default settings as they are.
                    - After the installation is finished, you can launch VS Code from the Start menu.
                    - To enable Python support in VS Code, install the Python extension by Microsoft. You can do this by clicking on the Extensions icon in the sidebar (or by pressing Ctrl+Shift+X), searching for "Python," and clicking on the "Python" extension from Microsoft.
                    """)
        st.link_button("Download VS Code", "https://code.visualstudio.com/")
        st.info("That's it! After following these steps, you should have Python installed using the Anaconda distribution and VS Code ready to use for both Python scripts and Jupyter Notebooks on Windows.")

    with mac:
        st.markdown("""
                    #### Python Installation 
                    - Visit the Anaconda website at https://www.anaconda.com/products/individual and download the Anaconda Individual Edition installer for macOS.
                    - Once the download is complete, double-click the installer package to start the installation.
                    - Follow the on-screen instructions to complete the installation. Make sure to check the box that says "Add Anaconda to my PATH environment variable" during the installation process.
                    - After the installation is finished, open the Anaconda Navigator from the Applications folder.
                    - In the Anaconda Navigator, you can launch Jupyter Notebooks or other Python IDEs like Spyder or JupyterLab.
                    """)
        st.link_button("Download Anaconda", "https://www.anaconda.com/products/individual")
        st.markdown("""
                    #### VS Code Installation 
                    - Visit the Visual Studio Code website at https://code.visualstudio.com/ and download the Visual Studio Code installer for macOS.
                    - Once the download is complete, double-click the installer package to start the installation.
                    - Follow the on-screen instructions to complete the installation. Leave the default settings as they are.
                    - After the installation is finished, you can launch VS Code from the Applications folder.
                    - To enable Python support in VS Code, install the Python extension by Microsoft. You can do this by clicking on the Extensions icon in the sidebar (or by pressing Ctrl+Shift+X), searching for "Python," and clicking on the "Python" extension from Microsoft.
                    """)
        st.link_button("Download VS Code", "https://code.visualstudio.com/")
        st.info("That's it! After following these steps, you should have Python installed using the Anaconda distribution and VS Code ready to use for both Python scripts and Jupyter Notebooks on Mac.")
# Definition of second level of tabs (starting from Second Tab)
def virtual_env():
    st.subheader("Virtual environments in VS Code", help="Click on the tabs below for a refresher on virtual environments.")
    st.markdown("This section explains what virtual environments are, why they are important, and provides detailed instructions \
                on how to set them up in VS Code for both script files (`.py` extension) as well as Jupyter Notebooks (`.ipynb` extension).")
    venv_about, venv_how, venv_deactivate = \
        st.tabs(["About virtual environments", "Setup and activation", "Deactivation"])

    with venv_about:
        st.markdown("#### What are Virtual Environments?")
        st.markdown("Virtual environments are isolated Python environments that allow you to work with different \
                      sets of packages and dependencies for different projects. They provide a way to keep project-specific \
                      dependencies separate, preventing conflicts between different projects that may require different \
                      versions of the same package.",
        )
        st.link_button("Read more on virtual environments", "https://realpython.com/python-virtual-environments-a-primer/", type='primary')
    
        st.markdown("""
                    #### Why are Virtual Environments Important? 
                    1. **Dependency Management**: Virtual environments enable you to install and manage project-specific packages without interfering with other projects or the system-wide Python installation.
                    2. **Reproducibility**: By working within a virtual environment, you can ensure that your code runs consistently across different machines or for other developers working on the project.
                    3. **Easy Collaboration**: Virtual environments simplify collaboration by allowing you to share a list of project-specific dependencies. Other developers can recreate the environment using this list, ensuring everyone is on the same page.
                    """
                    )

    with venv_how:
        st.markdown("Virtual Environments work with both standard Python scripts as well as with Jupyter Notebooks, \
                    however in the latter case you'll need to install an additional package. Follow the instructions below \
                    depending on your needs and use case.")
        with st.expander("Setting up Virtual Environments in VS Code for :orange[Python Scripts]"): 
            st.markdown("#### Setting up Virtual Environments in VS Code for :orange[Script Files]")
            st.markdown("""
                        1. **Open a New Terminal**: Launch VS Code and open the integrated terminal by selecting `View -> Terminal` from the menu.
                        2. **Create a Virtual Environment**: In the terminal, navigate to the project directory where you want to set up the virtual environment. Use the following command to create a new virtual environment:  
                            ```python -m venv myenv```  
                            *Note: this command creates a new virtual environment named "myenv" in the current directory (you can replace "myenv" with the name you want to give to your environment).*
                        3. **Activate the Virtual Environment**: To activate the virtual environment, use the appropriate command for your operating system:  
                            **Windows**:  
                            `myenv\Scripts\\activate`  
                            **Mac/Linux**:   
                            `source myenv/bin/activate`  
                            *Note: once activated, you will see the name of the virtual environment in the terminal prompt.*
                        4. **Install Packages**: With the virtual environment activated, you can use pip to install packages specific to your project. For example, to install a package named "numpy," use the following command:  
                            `pip install numpy`  
                            *Note: the numpy package is now installed in your virtual environment and it can be accessed only from within it.*
                        5. **Configure VS Code to Use the Virtual Environment**:
                            - Open the command palette by selecting `View -> Command Palette` from the menu or by using the `Ctrl+Shift+P` shortcut.
                            - Search for and select the `Python: Select Interpreter` command.
                            - Choose the Python interpreter located inside your virtual environment  
                                (e.g.: `myenv\Scripts\python.exe` on Windows or `myenv/bin/python` on Mac/Linux).
                        """)
            st.link_button("Read more on Python environments in VS Code", "https://code.visualstudio.com/docs/python/environments", type='primary')

        with st.expander("Setting up Virtual Environments in VS Code for :orange[Jupyter Notebooks]"): 
            st.markdown("#### Setting up Virtual Environments in VS Code for :orange[Jupyter Notebooks]")
            st.markdown("""
                        If you are working with a Jupyter Notebook, then **steps 1 - 4 are the same as above**, however, after step 4. You will have to complete the following additional steps:
                        - **Install ipykernel and install new kernel**: With the virtual environment activated, install ipykernel using `pip` and then install a new kernel:  
                        ```pip install ipykernel```  
                        ```ipython kernel install --user --name=myenv```  
                        *Note: remember to replace `myenv` with the name of your environment.*
                        - **Configure VS Code to Use the Virtual Environment**:
                            - Open the command palette and search for the "Create: New Jupyter Notebook" command.
                            - Choose the Python interpreter located inside your virtual environment  
                                (e.g.: `myenv\Scripts\python.exe` on Windows or `myenv/bin/python` on Mac/Linux).
                            - VS Code will create a new Jupyter Notebook that uses the selected Python interpreter from your virtual environment.
                        """)
            st.link_button("Read more on Notebooks and virtual environments", "https://anbasile.github.io/posts/2017-06-25-jupyter-venv/", type='primary')
        

    with venv_deactivate:
        st.markdown("#### Deactivating a Virtual Environment")
        st.markdown("""
                    To deactivate a virtual environment in the terminal, use the following command in the terminal:  
                    `deactivate`  
                    """
                    )
        st.info("""
                - *After deactivation, the virtual environment will no longer be active, and you will return to the system's default Python environment.*  
                - *Remember to activate the virtual environment again whenever you work on the project to ensure that you are using the correct dependencies.*
                """)
# Definition of second level of tabs (starting from Third Tab)
def cheatsheets(): 
    python_tab, numpy_tab, pandas_tab, matplotlib_tab, seaborn_tab = st.tabs(["Python", "NumPy", "pandas", "Matplotlib", "seaborn"])
    
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

    with numpy_tab:
        about, c_sheet = st.tabs(["About", "Cheatsheet"])
        with about: 
            st.subheader("About NumPy")
            st.markdown("""
                        [NumPy](https://numpy.org/) is the core library for scientific computing in
                        Python. It provides a high-performance multidimensional array
                        object, and tools for working with these arrays.
                        """)
            st.link_button("Read the Docs", "https://numpy.org/devdocs/user/")
            
            # NumPy installation and import
            st.markdown('**Install and import NumPy**')
            st.code('$ pip install numpy')
            st.code('''
                    # Import NumPy convention
                    import numpy as np
                    ''')
            
            
            # NumPy array creation
            st.markdown('**NumPy Arrays**')
            st.markdown("""
                        <img src="https://raw.githubusercontent.com/Data-Analytics-Boolean/assets/main/cheatsheets/np_array.png" width="500">""",
                        unsafe_allow_html=True
                        )
            st.markdown(" ")
            st.code('''
                            # Create a 1D array
                            a = np.array([1, 2, 3])

                            # Create a 2D array with specified dtype
                            b = np.array([
                                (1.5, 2, 3),
                                (4, 5, 6)
                                ], dtype=float)

                            # Create a 3D array with specified dtype
                            c = np.array([
                                [(1.5, 2, 3), (4, 5, 6)], 
                                [(3, 2, 1), (4, 5, 6)]
                                ], dtype=float)
                            ''')
        with c_sheet: 
            st.markdown("#### NumPy Cheatsheet")
            st.caption("*Credits: this section is largely inspired by [fralfaro](https://github.com/fralfaro)'s cheatsheet.*")
            # PDF download
            pdf_download("python-numpy-cheatsheet")

            col1, col2, col3 = st.columns(3)  # Create columns for layout

            #######################################
            # COLUMN 1
            #######################################

            # Initial Placeholders
            col1.subheader('Initial Placeholders')
            col1.code('''
            # Create an array of zeros
            zeros_arr = np.zeros((3, 4))

            # Create an array of ones
            ones_arr = np.ones((2, 3, 4))

            # Create an array of evenly spaced values (step value)
            d = np.arange(10, 25, 5)

            # Create an array of evenly spaced values (number of samples)
            e = np.linspace(0, 2, 9)

            # Create a constant array
            f = np.full((2, 2), 7)

            # Create a 2X2 identity matrix
            g = np.eye(2)

            # Create an array with random values
            random_arr = np.random.random((2, 2))

            # Create an empty array
            empty_arr = np.empty((3, 2))
                ''')

            # Saving & Loading On Disk
            col1.subheader('Saving & Loading On Disk')
            col1.code('''
            # Save a NumPy array to a file
            a = np.array([1, 2, 3])
            np.save('my_array', a)

            # Save multiple NumPy arrays to a compressed file
            b = np.array([
                (1.5, 2, 3), 
                (4, 5, 6)
                ], dtype=float)
            np.savez('array.npz', a, b)

            # Load a NumPy array from a file
            loaded_array = np.load('my_array.npy')
                ''')

            # Saving & Loading Text Files
            col1.subheader('Saving & Loading Text Files')
            col1.code('''
            # Load data from a text file
            loaded_txt = np.loadtxt("myfile.txt")

            # Load data from a CSV file with specified delimiter
            loaded_csv = np.genfromtxt(
                "my_file.csv",
                delimiter=',')

            # Save a NumPy array to a text file
            a = np.array([1, 2, 3])
            np.savetxt(
                "myarray.txt", 
                a, 
                delimiter=" ")
                ''')

            # NumPy data types
            col1.subheader('NumPy Data Types')
            col1.code('''
            # Signed 64-bit integer types
            int64_type = np.int64

            # Standard double-precision floating point
            float32_type = np.float32

            # Complex numbers represented by 128 floats
            complex_type = np.complex128

            # Boolean type storing TRUE and FALSE values
            bool_type = np.bool_

            # Python object type
            object_type = np.object_

            # Fixed-length string type
            string_type = np.string_

            # Fixed-length unicode type
            unicode_type = np.unicode_
                ''')



            # Asking for help
            col1.subheader('Asking for Help')
            col1.code('''
            # Get information about a NumPy function or object
            np.info(np.ndarray.dtype)
                ''')

            #######################################
            # COLUMN 2
            #######################################

            # Inspecting array properties
            col2.subheader('Inspecting Array Properties')
            col2.code('''
            # Array dimensions
            a_shape = a.shape

            # Length of array
            a_length = len(a)

            # Number of array dimensions
            b_ndim = b.ndim

            # Number of array elements
            e_size = e.size

            # Data type of array elements
            b_dtype = b.dtype

            # Name of data type
            b_dtype_name = b.dtype.name

            # Convert an array to a different type
            b_as_int = b.astype(int)
                ''')



            # Arithmetic operations
            col2.subheader('Arithmetic Operations')
            col2.code('''
            # Subtraction
            subtraction_result = a - b
            subtraction_np = np.subtract(a, b)

            # Addition
            addition_result = b + a
            addition_np = np.add(b, a)

            # Division
            division_result = a / b
            division_np = np.divide(a, b)

            # Multiplication
            multiplication_result = a * b
            multiplication_np = np.multiply(a, b)

            # Exponentiation
            exponentiation_result = np.exp(b)

            # Square root
            sqrt_result = np.sqrt(b)

            # Sine of an array
            sin_result = np.sin(a)

            # Element-wise cosine
            cos_result = np.cos(b)

            # Element-wise natural logarithm
            log_result = np.log(a)

            # Dot product
            dot_product_result = e.dot(f)
                ''')


            # Aggregate functions
            col2.subheader('Aggregate Functions')
            col2.code('''
            # Array-wise sum
            array_sum = a.sum()

            # Array-wise minimum value
            array_min = a.min()

            # Maximum value of an array row
            row_max = b.max(axis=0)

            # Cumulative sum of the elements
            cumulative_sum = b.cumsum(axis=1)

            # Mean
            array_mean = a.mean()

            # Median
            array_median = b.median()

            # Correlation coefficient
            corr_coefficient = a.corrcoef()

            # Standard deviation
            std_deviation = np.std(b)
                ''')

            #######################################
            # COLUMN 3
            #######################################

            # Comparison operations
            col3.subheader('Comparison Operations')
            col3.code('''
            # Element-wise comparison for equality
            equality_comparison = a == b

            # Element-wise comparison for less than
            less_than_comparison = a < 2

            # Array-wise comparison using np.array_equal
            np_equal = np.array_equal(a, b)
                ''')

            # Copying arrays
            col3.subheader('Copying Arrays')
            col3.code('''
            # Create a view of the array with the same data
            array_view = a.view()

            # Create a copy of the array
            array_copy = np.copy(a)

            # Create a deep copy of the array
            array_deep_copy = a.copy()
                ''')

            # Sorting arrays
            col3.subheader('Sorting Arrays')
            col3.code('''
            # Sort an array
            a.sort()

            # Sort the elements of an array's axis
            c.sort(axis=0)
                ''')


            # Subsetting, Slicing, and Indexing
            col3.subheader('Subsetting, Slicing, and Indexing')
            col3.code('''
            # Subsetting
            element_at_2nd_index = a[2] 

            # Select the element at row 1, column 2
            element_row_1_col_2 = b[1, 2] 

            # Slicing
            sliced_a = a[0:2]

            # Select items at rows 0 and 1 in column 1
            sliced_b = b[0:2, 1]

            # Select all items at row 0
            sliced_c = b[:1] 

            # Reversed array
            reversed_a = a[::-1] 

            # Boolean Indexing
            a_less_than_2 = a[a < 2]

            # Fancy Indexing
            fancy_indexing_result = b[ 
                [1, 0, 1, 0], 
                [0, 1, 2, 0]
                ] # array([ 4. , 2. , 6. , 1.5])
            fancy_indexing_subset = b[[1, 0, 1, 0]][:, [0, 1, 2, 0]] 
                ''')

            # Array Manipulation
            col3.subheader('Array Manipulation')
            col3.code('''
            # Transposing Array
            transposed_b = np.transpose(b)
            transposed_b_T = transposed_b.T

            # Changing Array Shape
            flattened_h = h.ravel()
            reshaped_g = g.reshape(3, -2)

            # Adding/Removing Elements
            resized_h = np.resize(h, (2, 6))  # Using np.resize to avoid the error
            appended_array = np.append(h, g)
            inserted_array = np.insert(a, 1, 5)
            deleted_array = np.delete(a, [1])

            # Combining Arrays
            concatenated_arrays = np.concatenate((a, d), axis=0)
            vstacked_arrays = np.vstack((a, b))
            hstacked_arrays = np.hstack((e, f))
            column_stacked_arrays = np.column_stack((a, d))
            c_stacked_arrays = np.c_[a, d]

            # Splitting Arrays
            hsplit_array = np.hsplit(a, 3)
            vsplit_array = np.vsplit(c, 2)
                ''')

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

    with matplotlib_tab: 
        about, c_sheet = st.tabs(["About", "Cheatsheet"])
        with about: 
            st.subheader('About Matplotlib')
            st.markdown('''
                        [Matplotlib](https://matplotlib.org/) is a Python 2D plotting library which produces publication-quality 
                        figures in a variety of hardcopy formats and interactive environments across platforms.
                        ''')
            st.link_button("Read the Docs", "https://matplotlib.org/stable/index.html")
            # Matplotlib installation and import
            st.markdown('**Install and import Matplotlib**')
            st.code('$ pip install matplotlib')
            st.code('''
                    # Import Matplotlib convention
                    import matplotlib.pyplot as plt
                    ''')
            # Anatomy of a figure
            st.markdown('''**Anatomy of a figure**  
                        In Matplotlib, a figure refers to the overall canvas or window that contains one or more individual plots or subplots. 
                        Understanding the anatomy of a Matplotlib figure is crucial for creating and customizing your visualizations effectively.
                        ''')
            st.markdown("""
            <img src="https://raw.githubusercontent.com/Data-Analytics-Boolean/assets/main/cheatsheets/mlp_figure.png" width="600">""", 
            unsafe_allow_html=True)
            st.markdown("")
            # Example code for the workflow
            st.code('''
                    # Workflow
                    import matplotlib.pyplot as plt
                    
                    # Step 1: Prepare Data
                    x = [1, 2, 3, 4]  
                    y = [10, 20, 25, 30] 

                    # Step 2: Create Plot
                    fig = plt.figure()
                    ax = fig.add_subplot(111)

                    # Step 3: Plot
                    ax.plot(x, y, color='lightblue', linewidth=3)

                    # Step 4: Customized Plot
                    ax.scatter([2, 4, 6], [5, 15, 25], color='darkgreen', marker='^')
                    ax.set_xlim(1, 6.5)

                    # Step 5: Save Plot
                    plt.savefig('foo.png')

                    # Step 6: Show Plot
                    plt.show()
                    ''')
        with c_sheet: 
            st.markdown("#### Matplotlib Cheatsheet")
            st.caption("*Credits: this section is largely inspired by [fralfaro](https://github.com/fralfaro)'s cheatsheet.*") 
            # PDF download
            pdf_download("python-matplotlib-cheatsheet")
            col1, col2, col3 = st.columns(3)  # Create columns for layout

            #######################################
            # COLUMN 1
            #######################################

            # Prepare the Data
            col1.subheader('Basic Plots ')

            ## Create a scatter plot
            col1.code('''
            # Create a scatter plot
            X = np.random.uniform(0, 1, 100)
            Y = np.random.uniform(0, 1, 100)
            plt.scatter(X, Y)
                ''')

            ## Create a bar plot
            col1.code('''
            # Create a bar plot
            X = np.arange(10)
            Y = np.random.uniform(1, 10, 10)
            plt.bar(X, Y)
                ''')

            ## Create an image plot using imshow
            col1.code('''
            # Create an image plot using imshow
            Z = np.random.uniform(0, 1, (8, 8))
            plt.imshow(Z)
                ''')

            ## Create a contour plot
            col1.code('''
            # Create a contour plot
            Z = np.random.uniform(0, 1, (8, 8))
            plt.contourf(Z)
            plt.show()
                ''')

            ## Create a pie chart
            col1.code('''
            # Create a pie chart
            Z = np.random.uniform(0, 1, 4)
            plt.pie(Z)
                ''')

            ## Create a histogram
            col1.code('''
            # Create a histogram
            Z = np.random.normal(0, 1, 100)
            plt.hist(Z)
                ''')

            ## Create an error bar plot
            col1.code('''
            # Create an error bar plot
            X = np.arange(5)
            Y = np.random.uniform(0, 1, 5)
            plt.errorbar(X, Y, Y / 4)
                ''')

            ## Create a box plot
            col1.code('''
            # Create a box plot
            Z = np.random.normal(0, 1, (100, 3))
            plt.boxplot(Z)
                ''')

            # Tweak
            col1.subheader('Tweak')

            ## Create a plot with a black solid line
            col1.code('''
            # Create a plot with a black solid line
            X = np.linspace(0, 10, 100)
            Y = np.sin(X)
            plt.plot(X, Y, color="black")
                ''')

            ## Create a plot with a dashed line
            col1.code('''
            # Create a plot with a dashed line
            X = np.linspace(0, 10, 100)
            Y = np.sin(X)
            plt.plot(X, Y, linestyle="--")
                ''')

            ## Create a plot with a thicker line
            col1.code('''
            # Create a plot with a thicker line
            X = np.linspace(0, 10, 100)
            Y = np.sin(X)
            plt.plot(X, Y, linewidth=5)
                ''')

            ## Create a plot with markers
            col1.code('''
            # Create a plot with markers
            X = np.linspace(0, 10, 100)
            Y = np.sin(X)
            plt.plot(X, Y, marker="o")
                ''')

            # Save
            col1.subheader('Save')
            col1.code('''
            # Save the figure as a PNG file with higher resolution (300 dpi)
            fig.savefig("my-first-figure.png", dpi=300)

            # Save the figure as a PDF file
            fig.savefig("my-first-figure.pdf")
                ''')

            #######################################
            # COLUMN 2
            #######################################

            # Markers
            col2.subheader('Organize')

            ## Create a plot with two lines on the same axes
            col2.code('''
            # Create a plot with two lines on the same axes
            X = np.linspace(0, 10, 100)
            Y1, Y2 = np.sin(X), np.cos(X)
            plt.plot(X, Y1, X, Y2)
                ''')

            ## Create a figure with two subplots (vertically stacked)
            col2.code('''
            # Create a figure with two subplots (vertically stacked)
            X = np.linspace(0, 10, 100)
            Y1, Y2 = np.sin(X), np.cos(X)
            fig, (ax1, ax2) = plt.subplots(2, 1)
            ax1.plot(X, Y1, color="C1")
            ax2.plot(X, Y2, color="C0")
                ''')

            ## Create a figure with two subplots (horizontally aligned)
            col2.code('''
            # Create a figure with two subplots (horizontally aligned)
            X = np.linspace(0, 10, 100)
            Y1, Y2 = np.sin(X), np.cos(X)
            fig, (ax1, ax2) = plt.subplots(1, 2)
            ax1.plot(Y1, X, color="C1")
            ax2.plot(Y2, X, color="C0")
                ''')

            # Label
            col2.subheader('Label')

            ## Create data and plot a sine wave
            col2.code('''
            # Create data and plot a sine wave
            X = np.linspace(0, 10, 100)
            Y = np.sin(X)
            plt.plot(X, Y)
                ''')

            ## Modify plot properties
            col2.code('''
            # Modify plot properties
            X = np.linspace(0, 10, 100)
            Y = np.sin(X)
            plt.plot(X, Y)
            plt.title("A Sine wave")
            plt.xlabel("Time")
            plt.ylabel(None)
                ''')

            # Figure, axes & spines
            col2.subheader('Figure, axes & spines')
            col2.code('''
            # Create a 3x3 grid of subplots
            fig, axs = plt.subplots(3, 3)

            # Set face colors for specific subplots
            axs[0, 0].set_facecolor("#ddddff")
            axs[2, 2].set_facecolor("#ffffdd")
                ''')

            col2.code('''
            # Create a 3x3 grid of subplots
            fig, axs = plt.subplots(3, 3)

            # Add a grid specification and set face color for a specific subplot
            gs = fig.add_gridspec(3, 3)
            ax = fig.add_subplot(gs[0, :])
            ax.set_facecolor("#ddddff")
                ''')

            col2.code('''
            # Create a figure with a single subplot
            fig, ax = plt.subplots()

            # Remove top and right spines from the subplot
            ax.spines["top"].set_color("None")
            ax.spines["right"].set_color("None")
                ''')

            # Colors
            col2.subheader('Colors')
            col2.code('''
            # Get a list of named colors
            named_colors = plt.colormaps()  
            print("Colors:",named_colors)
                ''')

            #######################################
            # COLUMN 3
            #######################################

            # Ticks & labels
            col3.subheader('Ticks & labels')
            col3.code('''
            from matplotlib.ticker import MultipleLocator as ML
            from matplotlib.ticker import ScalarFormatter as SF

            # Create a figure with a single subplot
            fig, ax = plt.subplots()
            
            # Set minor tick locations and formatter for the x-axis
            ax.xaxis.set_minor_locator(ML(0.2))
            ax.xaxis.set_minor_formatter(SF())
            
            # Rotate minor tick labels on the x-axis
            ax.tick_params(axis='x', which='minor', rotation=90)
                ''')

            # Lines & markers
            col3.subheader('Lines & markers')
            col3.code('''
            # Generate data and create a plot
            X = np.linspace(0.1, 10 * np.pi, 1000)
            Y = np.sin(X)
            plt.plot(X, Y, "C1o:", markevery=25, mec="1.0")
                ''')

            # Scales & projections
            col3.subheader('Scales & projections')
            col3.code('''
            # Create a figure with a single subplot
            fig, ax = plt.subplots()
            
            # Set x-axis scale to logarithmic
            ax.set_xscale("log")
            
            # Plot data with specified formatting
            ax.plot(X, Y, "C1o-", markevery=25, mec="1.0")
                ''')

            # Text & ornaments
            col3.subheader('Scales & projections')
            col3.code('''
            # Create a figure with a single subplot
            fig, ax = plt.subplots()
            
            # Fill the area between horizontal lines with a curve
            ax.fill_betweenx([-1, 1], [0], [2*np.pi])
            
            # Add a text annotation to the plot
            ax.text(0, -1, r" Period $\Phi$")
                ''')

            # Legend
            col3.subheader('Legend')
            col3.code('''
            # Create a figure with a single subplot
            fig, ax = plt.subplots()
            
            # Plot sine and cosine curves with specified colors and labels
            ax.plot(X, np.sin(X), "C0", label="Sine")
            ax.plot(X, np.cos(X), "C1", label="Cosine")
            
            # Add a legend with customized positioning and formatting
            ax.legend(bbox_to_anchor=(0, 1, 1, 0.1), ncol=2, mode="expand", loc="lower left")
                ''')

            # Annotation
            col3.subheader('Annotation')
            col3.code('''
            # Create a figure with a single subplot
            fig, ax = plt.subplots()
            
            ax.plot(X, Y, "C1o:", markevery=25, mec="1.0")
            
            # Add an annotation "A" with an arrow
            ax.annotate("A", (X[250], Y[250]), (X[250], -1),
                        ha="center", va="center",
                        arrowprops={"arrowstyle": "->", "color": "C1"})
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
    st.title("Python for Data Analytics", help="Click on the tabs below to explore the different sections.")    
    tab1, tab2, tab3 = \
        st.tabs(["Python Installation", "Virtual Environments", "Cheatsheets"])
    with tab1:
        python_install()
    with tab2: 
        virtual_env()
    with tab3:
        cheatsheets()


if __name__ == "__main__": 
    main()    
