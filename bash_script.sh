#! /usr/bin/env bash

#Displays files of the current directory
function display_files {
  for file in *
  do
        if [ -f $file ]
          then
                echo $file
        fi
done
}


#Stores current date and time
DATE_TIME=`date`

display_files
echo $DATE_TIME
