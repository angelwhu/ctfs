ps aux | grep 'bot.py' | awk '{print $2}'|xargs kill -9
killall Xvfb 
nohup python -u '/home/ubuntu/Document/docker/student_problem_xss1/bot/bot.py' >> '/home/ubuntu/Document/docker/student_problem_xss1/bot/nohup.out' 2>&1 &
nohup python -u '/home/ubuntu/Document/docker/student_problem_xss1/bot/xss2/bot.py' >> '/home/ubuntu/Document/docker/student_problem_xss1/bot/xss2/nohup.out' 2>&1 &
