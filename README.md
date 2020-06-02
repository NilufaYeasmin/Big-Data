# Hello and Welcome to my Portfolio Folder!

This repository contains the documents of MapReduce projects that I completed as part of my Master of Data Science and Analytics program at Ryerson University.

### Mapreduce program count top 10 words in a large text corpus. 
     ** shakespeare_100.txt - The input data file to count the occurences of each word 

### Run Hadoop streaming wordcount
[root@sandbox lab]# hadoop jar /usr/hdp/2.4.0.0-169/hadoop-mapreduce/hadoopstreaming-
2.7.1.2.4.0.0-169.jar -file /root/lab/ mapper_word_counts.py -mapper mapper_word_counts.py -file /root/lab/ reducer_word_counts.py -reducer reducer_word_counts.py –input /user/root/shakespeare_100.txt -output /user/root/shakespeare_streaming_out

### View results
• [root@sandbox lab]# hadoop fs -ls /user/root/shakespeare_streaming_out

• [root@sandbox lab]# hadoop fs –cat /user/root/shakespeare_streaming_out/part-00000 | tail -n 15

## Mapreduce program find movie name and rating greater than 3 from the input files


        **   u.data- The dataset has 100000 ratings by 943 users on 1682 movies.
             The file has 4 tab  ("\t") separated columns.  
       
       **   u.item - Information about the items (movies); this is a tab separated file with 3 columns. 
             The first column is movie id, the second column ismovie name, and the third column is release date.
             
       **   u.join - Data from u.data and u.item combined. 
            The first column column has "A" or "B". "A" denotes u.data and "B" denotes u.item.less.
            You can use it for the Map-Reduce job for the question number 2.
            
## Execution of the program

### Run Hadoop streaming Movie Rating Count
[root@sandbox lab]# hadoop jar /usr/hdp/2.4.0.0-169/hadoop-mapreduce/hadoopstreaming-
2.7.1.2.4.0.0-169.jar -file /root/lab/ wc_mapper_movie_rating.py -mapper wc_mapper_movie_rating.py -file /root/lab/ wc_reducer_movie_rating.py -reducer wc_reducer_movie_rating.py –input /user/root/u.join -output /user/root/join_streaming_out

### View results
• [root@sandbox lab]# hadoop fs -ls /user/root/join_streaming_out

• [root@sandbox lab]# hadoop fs –cat /user/root/join_streaming_out/part-00000 | tail -n 15
            
