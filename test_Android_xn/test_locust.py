from locust import HttpLocust, TaskSet, task

# 定义用户行为
class UserBehavior(TaskSet):

    @task
    def baidu_index(self):
        self.client.post("/app/book/list")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000




    #  http://10.72.17.30/app/book/list