#!/bin/sh
for i in `seq 1429039000 1 1429039999` 
do
	echo "------${i}------"
	key=`php random.php ${i}`
	echo  "----"${key}"-----"
	curl "ringzer0team.com/challenges/113/?k=${key}" --cookie '_ga=GA1.2.517894686.1428888833; PHPSESSID=t8kfi2r0hnkoa26ti1h8c4f9s5' > tmp.out 
	cat tmp.out | grep 'success' | grep 'password' > /dev/null 2>&1
	if [ $? -eq 0 ]
	then
		echo "success"
		break
	fi
done
		
	
	
	
