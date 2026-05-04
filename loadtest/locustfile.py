from locust import HttpUser, task


class CoalUser(HttpUser):

    @task
    def sensor(self):
        self.client.get("/sensor")
