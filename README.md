# File_Sort
Simple script that organizes files into respective folders.

## How to use: Choose folder path
Enter the path of the folder you would like to organize as the value of the **folder_path** variable.

In order for the path to be found, the backslashes need to be inverted so it looks like the example path below:

    folder_path = "C:/Users/exampleuser/Videos"

## How to use: Specify how the files should be organized 
To specify how the script should organize the files and the name of the respective folder the file belongs in, edit the value of **file.split(' ')[0]** in the **"folder_name"** variable. 

For example: if you have a folder full of photos and you want to organize them by year and they have file names such as:

    2012-Family.jpg
    2017-Dog.png
    2017-Holiday.jpg
    2012-Park.jpg 
    ...
    
Set the **file split** value as:

    file.split('-')[0]
    
The script will read the file names as far as the first '-' and it will create two folders, **2017** and **2012**. In these folders will be the corresponding files with the same value.


If you wanted to organize the file by month and the files were named as:

    2012-12-Family.jpg
    2017-08-Dog.png
    2017-08-Holiday.jpg
    2012-12-Park.jpg
    ...

Set the **file.split** value as:

    file.split('-')[1]

and the script will organize the files as far as the second '-' so it will produce two folders, **08** and **12**. In these folders will be the corresponding files with the same value.