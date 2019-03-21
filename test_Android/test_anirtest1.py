from airtest.core.api import *

connect_device("android:///N8K5T16C26020898")
start_app("com.idreamsky.avg.platform")
sleep(5)
touch(Template(r"tpl1552888978667.png", record_pos=(0.02, 0.094), resolution=(1080, 1920)))
