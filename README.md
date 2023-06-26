      Analytics Company Database Creation Project


This project aims to create a comprehensive database for an analytics company from scratch. The database will be designed using a data model, and the schema will be implemented in MySQL. We will go through the process of creating tables, inserting data, and performing data cleaning and analysis.

      
      Project Overview


1.	Data Model Design: We started by designing a conceptual data model for the analytics company database. This involved identifying the entities, attributes, and relationships relevant to the company's operations. The data model included entities such as Client, Project, Data Source, Data Model, Data Transformation, Analysis Method, Report, and Key Performance Indicator (KPI).
2.	Schema Creation: Based on the data model, we created the physical schema in MySQL. The schema included tables corresponding to each entity, with appropriate columns and data types. We established relationships between tables using foreign keys to maintain data integrity.
3.	Table Creation: Using SQL queries, we created tables for each entity in the MySQL database. We ensured that primary keys, foreign keys, and other constraints were defined correctly to enforce data integrity.
4.	Data Insertion: We populated the tables with dummy data to simulate real-world scenarios. For each table, we created multiple records with representative values for each column. This allowed us to have a dataset to work with during the subsequent stages.
5.	Data Cleaning and Analysis: The next step involved reading data from SQL files, cleaning the data, and performing data analysis. We utilized the pandas library in Python to read the data into data frames, clean and transform the data as needed, and extract insights or generate reports.
6.	Data Frame to Database: After data cleaning and analysis, we reinserted the processed data back into the MySQL database. This step completed the end-to-end cycle, where we started with creating the data model, building the database schema, manipulating and analyzing the data, and finally inserting the processed data back into the database.
   
        Project Structure
  	
1.    DataModel.pdf: This file contains the conceptual data model for the analytics company database, showcasing the entities, attributes, and relationships.
2.	Schema.sql: The SQL script file that includes the table creation statements for each entity in the MySQL database.
3.	DataInsertion.sql: The SQL script file containing the insert statements to populate the tables with dummy data.
4.	DataCleaning.ipynb: A Jupyter Notebook file demonstrating the process of reading data from SQL files, cleaning and analyzing the data using pandas.

        Getting Started
        
1.	Ensure you have MySQL installed and running on your local machine.
2.	Import the database schema using the provided Schema.sql file.
3.	Run the DataInsertion.sql script to populate the tables with dummy data.
4.	Open the DataCleaning.ipynb notebook in Jupyter Notebook or any compatible environment to explore the data cleaning and analysis process.
5.	Open the DataInsertion.ipynb notebook to understand how to insert processed data back into the MySQL database.
   
        Conclusion
  	
This project covers the end-to-end process of creating a database for an analytics company, starting from designing the data model to implementing the schema in MySQL, populating the tables with data, performing data cleaning and analysis using pandas, and finally reinserting the processed data back into the database. The project provides a solid foundation for managing and analyzing data in an analytics company, allowing for data-driven insights and decision-making.

